import gzip
import zlib
import re
from datetime import datetime, timezone
from pathlib import Path
from general import write_json,write_txt,read_json


def write_dict(dict, type, name, value):
    power_value = value if type == 0 else dict.get(name, {}).get("power")
    main_value = value if type == 1 else dict.get(name, {}).get("main_level")
    dict[name] = {"power": power_value, "main_level": main_value}

# 如果是戰力或關卡記錄完就跳出迴圈，都不是的話紀錄為名字並與之前的紀錄寫入字典
def get_ranking(player_data,cache_data,server,corrections):
    name = power = main = None
    for encode_data in cache_data:
        # 處理戰力
        try:
            # '戰力'的編碼
            if b'{\xe6\x88\x98\xe5\x8a\x9b}' in encode_data:             
                    power=encode_data[11:-3].decode('utf-8').strip().replace(' ','')                  
                    if len(power.split(',')[2]) == 2:
                        power=encode_data[11:-2].decode('utf-8').strip().replace(' ','') 
                    elif len(power.split(',')[2]) == 1:
                        power=encode_data[11:-1].decode('utf-8').strip().replace(' ','') 
                    elif not power.split(',')[2]:
                        power=encode_data[11:].decode('utf-8').strip().replace(' ','') 
                    continue 
            # '主線關卡'的編碼
            elif b'{\xe4\xb8\xbb\xe7\xba\xbf\xe5\x85\xb3\xe5\x8d\xa1}'in encode_data:               
                    main=encode_data[17:-3].decode('utf-8').strip().replace(' ','')                      
                    if not main.split('-')[1]:
                        main=encode_data[17:-1].decode('utf-8').strip().replace(' ','')
                    continue                
        except (UnicodeDecodeError,IndexError) as e:
            print(e)
            continue
     
        for j in [-2,-1,-3]:
            try:                 
                # 如果下一字是中文起始
                if j ==-3 and 224<=encode_data[j] <=233:
                    name = f'#{server if server>9 else f"0{server}"} {encode_data.decode("utf-8").replace('<','')}'                                      
                else:
                    name = f'#{server if server>9 else f"0{server}"} {encode_data[:j].decode("utf-8").replace('<','')}'     
                name=corrections.get(name, name)
                break
            except UnicodeDecodeError:
                # 到最後一個都檢查不出來
                if j == -3:
                    print(encode_data)
               
        write_dict(player_data, 0 if power else 1, name, power if power else main)
        name = power = main = None
                                                                                
    return player_data

def alliance_data(player_data):
    alliances = read_json("alliance.json")
    player_to_alliance = {}
    reversed_alliances = {key: alliances[key] for key in reversed(list(alliances.keys()))}
    for alliance_name, players in reversed_alliances.items():
        for player in players:
            player_to_alliance[player] = alliance_name

    for player in player_data.keys():
        player_data[player]["alliance"] = player_to_alliance.get(player)

    return player_data

def date_record(date):
    month, day = date[:2], date[2:]
    path = "data/date_options.json"
    date_options = read_json(path)

    new_date = {"value": f"2024{month}{day}", "label": f"2024/{month}/{day}"}
    if new_date not in date_options:
        date_options.insert(0, new_date)

    write_json(path, date_options)

def server_record(server):
    path="data/filter_options.json"
    filter_options = read_json(path)

    new_servers = [{"value": f"specific{i}", "label": f"#{i}"} for i in range(1, server + 1)]
    filter_options.extend([server for server in new_servers if server not in filter_options])

    write_json(path, filter_options)

def Data_collation(data, output_date):
    def safe_int(value, default=0):
        try:
            return int(value.replace(",", ""))
        except (ValueError, AttributeError):
            return default

    def sort_by_power(item):
        # 将power为空或无效的视为最低优先级，分配一个负数
        return safe_int(item[1].get("power", "-1"), default=-1)

    def sort_by_main_level(item):
        # 按main_level排序，拆分日期进行年月排序
        parts = item[1]["main_level"].split("-")
        return tuple(safe_int(part) for part in parts[:2])

    
    for type_key in ["power", "main_level"]:
        filtered_data = {k: v for k, v in data.items() if v.get(type_key)}

        if type_key == "power":
            sorted_data = dict(sorted(filtered_data.items(), key=lambda x: sort_by_power(x), reverse=True))
        else:  # for main_level
            # 先按power排序
            pre_sorted_by_power = sorted(filtered_data.items(), key=lambda x: sort_by_power(x), reverse=True)
            # 再按main_level排序
            sorted_data = dict(sorted(pre_sorted_by_power, key=lambda x: sort_by_main_level(x), reverse=True))

        file_type = "main" if type_key == "main_level" else "power"
        file_path = f"data/2024{output_date}_{file_type}.json"
        write_json(file_path, sorted_data)
       
    date_record(output_date)


def packet_analysis(player_data,packets,corrections,record_server):
    PATTERN = re.compile(rb'\x00\x00\x00(.*?)\x00', re.DOTALL)
    LOGIN_PATTERN = re.compile(rb'"serverId":(.*?),', re.DOTALL)
    # packets = sorted(packets, key=lambda x: int(x["_source"]["layers"]["tcp"]["tcp.seq_raw"]))


    server=0
    cache_data = []
    data_len = []

    for no,packet in enumerate(packets): 
        packet_data = packet["_source"]["layers"]["tcp"]['tcp.payload'].replace(":", "") 
        packet_len = int(packet["_source"]["layers"]["tcp"]['tcp.len'])
        packet_seq = int(packet["_source"]["layers"]["tcp"]["tcp.seq_raw"])
        Complete_data=None
        
        try:
            if packet_data[10:14] == '1f8b':  # Gzip 文件頭檢查
                next_packet_seq=packet_seq+packet_len
                if packet_data[-4:] == '0000':  # Gzip 結尾檢查
                    Complete_data = packet_data      
                    data_len.append(packet_len)         
                else:
                    for i in [1,-1,2,-2]:
                        possible_packet_seq = int(packets[no+i]["_source"]["layers"]["tcp"]["tcp.seq_raw"])
                        possible_packet_len = int(packets[no+i]["_source"]["layers"]["tcp"]['tcp.len'])
                        possible_packet_data = packets[no+i]["_source"]["layers"]["tcp"]['tcp.payload'].replace(":", "")
                        if possible_packet_seq == next_packet_seq and possible_packet_data[-4:] == '0000':
                        # 下一個封包結尾檢查
                            Complete_data = packet_data + possible_packet_data
                            data_len.append(possible_packet_len)
                            break

                if Complete_data is None:
                    continue
              
                # print(Complete_data)
         
                binary_data =  gzip.decompress(bytes.fromhex(Complete_data[10:]))
    

                # SCLogic_RankInfoBack
                if b'\x53\x43\x4c\x6f\x67\x69\x63\x5f\x52\x61\x6e\x6b\x49\x6e\x66\x6f\x42\x61\x63\x6b' != binary_data[8:28]:
                    continue
                
                # 搜索模式匹配
                matches = PATTERN.findall(binary_data[42:])
                # print(matches)
                if not matches:
                    continue
                
                # 將符合條件的匹配數據加入 cache_data
                cache_data += [encode_data for encode_data in matches if len(encode_data) > 1]
                
            
            elif packet_data[26:52] == '53434c6f67696e5f4c6f67696e':  # "SCLogin_Login" 標識檢查
                binary_data = bytes.fromhex(packet_data[128:168])
                # binary_data = bytes.fromhex(packet_data)
                # print(binary_data)

                server = int(LOGIN_PATTERN.search(binary_data).group(1))
                print(server,packet_seq)
                player_data = get_ranking(player_data, cache_data, server, corrections)
                data_len.append(packet_len)
                if cache_data != []:
                    record_server.append(server)
                cache_data = []

        except (OSError, IOError, EOFError) as e:
            cache_data = []
            print(f"{packet_seq} 處理 gzip 文件時發生錯誤：", e)
            print(Complete_data[10:])

        except zlib.error as e:
            print(f"Decompression error: {e}")  

    print('')
    print(f'最長:{max(data_len)} 最短{min(data_len)}')
    return player_data,record_server


if __name__ == '__main__':    
    DEBUG = False
    # output_date = datetime.now(timezone.utc).strftime("%m%d")
    output_date = '0920'

    corrections = read_json('corrections.json')
    
    player_data={}
    debug_result=[]
    data_len=[]
    record_server=[]

    packets = read_json(f'wireshark rawdata/{output_date}.json')
    player_data,record_server = packet_analysis(player_data,packets,corrections,record_server)

    packets = read_json(f'wireshark rawdata/{output_date}01.json')
    player_data,record_server = packet_analysis(player_data,packets,corrections,record_server)
    # packets = read_json(f'wireshark rawdata/{output_date}02.json')
    # player_data,record_server = packet_analysis(player_data,packets,corrections,record_server)
    # packets = read_json(f'wireshark rawdata/{output_date}03.json')
    # player_data,record_server = packet_analysis(player_data,packets,corrections,record_server)
    
    missing_servers = [i for i in range(1, max(record_server)+1) if i not in record_server]
    print(f'共{max(record_server)}區； 少{", ".join(map(str, missing_servers))}區')

    server_record(max(record_server))
    player_data=alliance_data(player_data)


    Data_collation(player_data,output_date)

    