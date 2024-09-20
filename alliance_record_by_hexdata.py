hex_data='a3060000001f8b080000000000040065567950136714dfec066febf5879d5adb1977186beb0121e1683bd36a51392456915aec81118386236b0399169c8a8a0102919b0802050151619020a18640c278b6a39d76a6b775da3a36bb9bd5daaa9dced4995afb5eb2c9aeed37bbf3cdfbe6b76fdff17bef7de61904b1882088f4d73630bb0cd959ebf545194603634cd3ef4836e6306b74d979674615c43480bc042fd3a320a6c3fe04bc2a9aab7709c313aca356b00cf7c0c98f49c795894b09e2e8428250801cfa7226bcd134e0f83a2bef1c3800e2506229b11cf64a11fafb328a980afb1c541c47b3bded42db497fd5b0bfce73048e6e4fbd40f5ce531076116ebba30cecb3e08d8da739679bd032c21d3bde00f268562e35748b082cc494eba8c08e76ab12d00cb6adad198455da616a979920cca2d2f37a49a90694da3d6c452f6b715483fc9ba2853c748120de13b12bee05b1686f6c029dae4de5ba0fb0ae4af6640bc26b3ed941ae84bd4884735b94611b342a7a75aac1b826a51604cbab57c86fb21444ad08fc29f57fc094f43a10c66f0c939765c0cafb41af30b6ea189a6dee87678fce0e62e6a9eb54aaece7d6342a6cab2a9e4ed1e7e498f4c55b8af3f5a62638baf2f7734a33842114db3bf3c9c08e998ba3fdc76c6c7315e25e99b2948c23a4ec96bd23538b29abe5ce0c70dd7ddc4423a66cdfa75f5317b3a4947d4706e1b311aea2d3750505c569ba42c6d80a07e4c3d94ab5cce48d9d41f07c786334b46fac43f01e16069bb89166a1b5a7114ebb2363a964d81bc42fd6754ad6c017ece94affe059a1a29eefed43f8a381a4003c644d5e26198647ab68b67c80738c720e277776a21b799ed910b027e4ab65f37f7c6df73bceb2631e600746fc4da19d427684b4ebbc32766868c1ddc737398078fee3933638fa76999bdc087b28971fe6458489170f85d252030f5fdd850439d7bf80cad24a24bd7f578a8c5a4d0b1dddecd0186ff70a3d356cdd09a4f5ecef6750d5ed5264deb7c8221345736523ace5b8d0f1113c08af6b9ba95c8730115ef2b83142e3a0cfdbc1ed6fb7827c2a7592dca4954a6b762e15c6826aa1af151eb6b1a105e49cc826aafc8264c6b56b1161c22644d319ac7d9c6ff564a08f87ee79a84680da44a866a564429c864ed39bb28bd799f3f3cb41bef8e2381985668ad8f217a4506ba2687f99cd37798c3f7a8877771f86a3e78f2ca2ded04a564c2e90a956d1993a6336c3e4e90b2b412edd739d246469b995f958ddf85c76deddeff38cf8dc6ecce28dbccf0396148af07d95b238ab68bea68deb9af0b93cbc750ccb27e5ab24a5a55de2c8c24c59b7014ad597b34d43ac7d14b1ccdc04aa4d16bbe577836c9d819644d11bf4058cb1c0d006d24d7b6e80d7a175f940d0bfb998bd186c769cb57a0d5bee602bace8e35bbfae2773cc411f715dec97190d564c8efadc95ece132ee7405964d49b552592a1a8d2bdb4a868b385a0dadc4682cdec0980d85f5f87de13f0a0521e9be7a49d2ad86d4d4d97cae8fb9c11edf981575cfbbd1a244829844f8acf31161ddf1f17492ceb4476f4a62989d48914b6b1f51f65bc188e07afbe78870192440b09d5d7cbb4bb0d83897851bb594a1154f7a155bb4c1961288ccac8870678d8322ab1de29b6b3184db3c914a541df2f1c1b3b2b443ef71bb85234e7f998b6d3d89adfdcbdc1872dd5249efc45e590d44d389fa7c834eab2bdc0d5123b62f3941ad1029826bda3945d80635b440e32e2626ae0b84cf967ca12c81b43489c06ba6c78a101a137f60c85f3584294c7c7d3b99679678f7eeb80c0b29b41df1efc75184d522388b48fc593808ac340ba17bf89d6ee860d8add39e71519184c4ce277e900155748eceb869f5269cae8e07e7a8cd5ac9d2c55ac9fde8589c02bc7b180601b680a706d75238dc4a442cfb47d0fd2901f793199301c97ebb243d40f6106d7e39288dc0d8287aabae486f5a831cb8f2703aa521a4fa5c9121fd1aea13ba095f63e5867b11fbe78a0172142e0c7b43ddc729e339ccf6964ea1a2c6efb5f2de9a4e38ca4bdca65c0ffb07a20d31d494007c017a150541f55a7c9e2ea1a3c1e7eae0c7bd85e844ef69a2d41cbc11e0ead4c8f8a5a1b9aa16ffc9fd4898a717eba839b2b2b8b3830acf57b88f6c654cf9018af76c58456588cd15d7cb25116193e3e1b235dcc5b9aaa082e0c15e7c575d40ee96c16fde0fc2f16a969040271b77990c3b57efd415141e8493aabd6eb20fe2111ab0e40ca9fba8e369b6c2e6f73a38773f5e35ae6e729223f3146183336365933b8e4e3733bbd30c794c1183a36fecaf3d148621b4221f28c2dec5d2fc29b77fff08960277ec2ab9d72c31f15f918ec74d790a0000'


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