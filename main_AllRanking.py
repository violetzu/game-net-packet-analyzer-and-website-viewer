import gzip
import re
from main import *
player_data={}
output_date = '1107'
packets = read_json(f'wireshark rawdata/{output_date}.json')
def get_ranking(player_data,packet_data,corrections):
    binary_data =  gzip.decompress(bytes.fromhex(packet_data[10:]))
    PATTERN = re.compile(rb'\x00\x00\x00(.*?)\x00', re.DOTALL)
    matches = PATTERN.findall(binary_data[42:])
    if matches:
        data = [encode_data for encode_data in matches if len(encode_data) > 1]

    name = power = main = None
    for encode_data in data:
        # 檢查'戰力'字串是否存在於數據中
        if b'{\xe6\x88\x98\xe5\x8a\x9b}' in encode_data: 
            try:
                # 基本解碼過程
                power = encode_data[11:-3].decode('utf-8').strip().replace(' ', '')
                # 根據逗號分割的第三部分的長度來調整解碼範圍
                if len(power.split(',')[2]) == 2:
                    power = encode_data[11:-2].decode('utf-8').strip().replace(' ', '')
                elif len(power.split(',')[2]) == 1:
                    power = encode_data[11:-1].decode('utf-8').strip().replace(' ', '')
                elif not power.split(',')[2]:
                    power = encode_data[11:].decode('utf-8').strip().replace(' ', '')
            except IndexError:
                # 如果遇到IndexError，根據逗號分割的第二部分的長度來調整解碼範圍
                if len(power.split(',')[1]) == 2:
                    power = encode_data[11:-2].decode('utf-8').strip().replace(' ', '')
                elif len(power.split(',')[1]) == 1:
                    power = encode_data[11:-1].decode('utf-8').strip().replace(' ', '')
                elif not power.split(',')[1]:
                    power = encode_data[11:].decode('utf-8').strip().replace(' ', '')

        # 檢查'主線關卡'字串是否存在於數據中
        elif b'{\xe4\xb8\xbb\xe7\xba\xbf\xe5\x85\xb3\xe5\x8d\xa1}'in encode_data:   
            try:            
                main=encode_data[17:-3].decode('utf-8').strip().replace(' ','')                   
                if not main.split('-')[1]:
                    main=encode_data[17:-1].decode('utf-8').strip().replace(' ','')             
            except IndexError: 
                main=encode_data[17:].decode('utf-8').strip().replace(' ','')

        # 獲取名字並寫入以記錄的戰力或主線
        elif b")" in encode_data:
            parts = encode_data.split(b")", 1)  # 使用 maxsplit=1 确保只分割一次
            try:
                server = int(re.findall(rb'\((\d+)', parts[0])[0])  # 使用字节模式
                encode_name = parts[1]
            except IndexError:
                continue
            # print(encode_name)
            for j in [-2,-1,-3]:
                try:                 
                    # 如果下一字是中文起始
                    if j ==-3 and 224<=encode_data[j] <=233:
                        name = f'#{server if server>9 else f"0{server}"} {encode_name.decode("utf-8").replace('<','').strip()}'                                      
                    else:
                        name = f'#{server if server>9 else f"0{server}"} {encode_name[:j].decode("utf-8").replace('<','').strip()}'     
                    name=corrections.get(name, name)
                    break
                except UnicodeDecodeError:
                    # 到最後一個都檢查不出來
                    if j == -3:
                        print(encode_name)
            # print(f'{name}{power if power else main}')
            write_dict(player_data, 0 if power else 1, name, power if power else main)
            name = power = main = None

    return player_data

corrections = read_json('corrections.json')

all_packet_data=''
for no,packet in enumerate(packets): 
    packet_data = packet["_source"]["layers"]["tcp"]['tcp.payload'].replace(":", "") 
    all_packet_data+=packet_data
    if packet_data[-4:]=='0000':
        get_ranking(player_data,all_packet_data,corrections)
        all_packet_data=''

player_data=alliance_data(player_data)
Data_collation(player_data,output_date)