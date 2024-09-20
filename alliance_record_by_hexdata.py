hex_data='8c060000001f8b08000000000004005d567b4c53571cbebdb7cef7e68ccb348bd1e4e8d4a80b94428bee251ac529203866cc9c58e182b5a5574aab023e40045ae4252f7914f1894e408ac02c95c7a6484ccc3259b22d18ff99eb7de988c63d129799ec77dacbbdd79ddc93d3f3cb77bf7ee7f73a37630641bc4710c4f6f55b990c736aca26da916c3333b6387aef665b3a13634ab5dce8d310d300b216267351434c87f54d983ac49df689dd03acb7522cea3e0796b19e68ed866504d1f42e111c936fce84198e00c757b9f9def6e3b09d5f994bac82d505500daccf5650c45458dfc2c406c45ef288cd5785d26ea16ab01a537dff2975e96d0d512fc10bbfa282ab0cafe46eb47317dab8819ad35866b39e1a4951e063266d709d0d33d288d6d3a9666b1c6337d9cac0b0b25f24d7c413844302bf781ee29e0b53af4762cb05b6ab9faf1f122f56b055572ac1ea3bd6449ef21044a5f44651d2ffd47804ef4db67f902df262350363afc893770859cdb87d4a709d05d3188e386f2f5fd0259476e5c3fec121a7a6f50941644bd85437292b0fd7a3cf689b2d672be33467578061cfdcbf359a90ab83a043458a8e8830c415f6b04597c596b3f05481a9a0338bda886112f7aae721ee19587618da4a6732b64c733dec0cba7be4664239e0ecfd94ac1888c5b64678d89aea1ad8938fef91e94e82c892b0ee3895338ca0383ddd4ee77c9e63a5edd877594c23e5742a22c6c743cec039121d8e92d9fa5b7ce360f209d81efbd542625f9449d0d18210740ef65b04ce27ce7d2a862df6b225ee02b0b53c7469b09249d5a3b342789cb006c8bfca2ebeae126b48a83d42d5037183047cb2f335c9015f3defbf1618ec09f8fd2e302ddc6f23c3082526b36e4f91636234a25893fd006d8f6598b44230a4c48c91987b329b26e6869c8cebc08084f3656c5d294e8a0f13e69006580f4ab887f74939ebc28d28ce64cf70d276b3838e63183b8d1d3d3cb12ac83c793ccb4e52561dae436c713be7ed8364e26e0e9c05d3c8b3795abd2a39c8195a39867a23624bca84212fe7bf864be05eaa8d8c54615d2f2839287af074dd35780e987012ed7eb59cda4228e72b5ea99555448621a1b02c307c9e6f3ac9fb2f9460918f1ac82fe215d123d754290aa532dc17f0bbd8f242ee7a09cee8e1da2fa94f08a554ce66a90a371ac5d226bb23d5ce64679f02c3edea7fc8e63b8a6ad39022252a1289fe36bed60b59225c1e2ec6dc590bc80495f28dad2a299188bdee123a6f8a25a7f94b6d58ca81e8abc11a9864ef704c91e146e87d1d57f8a612aee78250dd7818bb3725978852c177df5215391cb4ec8c905fc0fa5c79b0df5264d54c57294968553a0e2809f4b78843e562672dd75327365ec462fe7cd214146397de583bf5b5d4161b86410ff649ca8a9b14f6498504bc7f5739a41ec2535516f07dc3755e0cf4bb31af70660bb558c5fb0b49c9fed6e9d0765366664e9c299bb1d582a1605d1aa557c966ffd004d7373037daccd8cdc16ef7b336a86032e22f17a98a0b0ee7f78b677a85421fdb781527c88e961f351b978548f118c853b59a70b481b69a4df1a6ec7db82d75bcfa805a2d15221e3ba3546a0d68bb93d91767b6300e06974b5bc43ceab8939047cc234aee767a1db298ad56daca94c32e714f7450f121897661bc22213c0a5f2ebcbf1bee17cc3ab1e031f913dc2cb912569fa4648501b78ef2c040135fd0ce5715e26e90b6fc076a3245f138e652e59c0ef115cddcb981806f9077f7e33afcf6f2360a37855ac977ad91aa304722aeb441b89a8f792f3fbd4b6e22424ec6c3daad9581517ab493cecea0edb88792e797903309c5bd4b5f6ae4761485f8affd427e4f13fc3e923642e63915dc6f275484616887c941db637033a4ff72055bc5e43f8fb2940c84db52e8f54bb7dee892a5d452426970e3bdaaa31b11d7d02a965408436e7ea8a2014cef2c5843e1131d96788b4d0aaf2e1a377bb6b919f37ade375219a0d42901df7ca812a043e9265be2ba441cd6d9bb165149f12167e231b197928f0e8c3b18bb350d3bfde9c7f56472bc12a3dfd354950b2573aa92f3b8d8c1eea338a97609648947397daee5b5ab5cace90c0cb570f91e1ca3dbac9f4c04de7209bbe681aa3d415a557504bf286ec1870eaedce91d3ef2ae5123476075b292857029c1a5c857b8b9ee4b18db6eb0907df039942761a77da7517c00556bcb60220c2db0a95ebc5f9bab2a82971d4af82310dfd1c6b7dd6a86df4793565016950f3e5aab843f320265d30e879576c3e6447f2c89dbff69e99f6bcf2bd7b7110e15babdb7e5c076c9bff335073d0ae77f5492cab96b0a0000'


alliance_name = "迷人又可爱的"
# alliance_name = "可爱又迷人的"

import gzip
from general import read_json, write_json

def decode_data(hex_data):
    """解碼二進制數據並提取成員信息。"""
    decompressed_data = gzip.decompress(bytes.fromhex(hex_data[10:]))
    # print(decompressed_data)
    result = decompressed_data.split(b'\x00')
    result = [item for item in result if item != b'']
    alliance_member = []
    for data in result:
        if len(data) > 1 and b'\x23' in data:
            try:
                utf8_data = data[:-1].decode('utf-8').split('#')
                server = int(utf8_data[0])
                member = f'#{server if server > 9 else f"0{server}"} {utf8_data[1]}'
                alliance_member.append(member)
            except (UnicodeDecodeError, ValueError) as e:
                print(e)
                pass
    return alliance_member

def update_alliance(alliance_name, new_members):
    """更新公會成員名單。"""
    alliance = read_json('alliance.json')
    old_members = alliance.get(alliance_name, [])
    leave = [m for m in old_members if m not in new_members]
    join = [m for m in new_members if m not in old_members]
    alliance[alliance_name] = new_members
    return alliance, join, leave

alliance_member = decode_data(hex_data)
while True:
    alliance, join, leave = update_alliance(alliance_name, alliance_member)
    print(f"加入的成員: {join}")
    print(f"離開的成員: {leave}")

    
    check = input('是否儲存(Y):').strip().upper()
    if check == 'Y':
        write_json('alliance.json', alliance)
        break
    elif check == 'N':
        continue