hex_data='94060000001f8b080000000000040065550950136714deec06b5dec74ced31add3fea3b653b00910c0a3758a8e8a40ec0ce255a7189d605330b1c15491f1c4008110e50ae13e8314ca2550234768b575a6dafbd06a5bdb8ed9ddac33b6b6b6763adae33db2c92ed37f76e7f1ff7c79fb8eef7d7ffa548a7a9ca2a8945549a6dd865d696bf5fb528d06933159bf33c1986e8ad7edca3833a8a0a6006439bca61605f510d899f04612aec423f48db0bd27056bdf5b70f208bd296cf5628aaa9e4f510ad8077f390d5e35011c7fcac60f749e80ed53334f50e1600b44e88d44e5b845e79a48f252a2c1b83ec5893e176e642ea629a85211c86dfc1f307e3d02b9a926e66b00ba4460cedcb0713b1dde581549d11d3019379b32d3cb61ffe2bd6ac65a4b51e522f69b9b01a798564c1c59afcfca32e8d7e98de6ec3a3889533f609ea6020b51d4c7ca90e7180de12b3afcf6137c5ea11df62f5cf98aaeb940510744cf973f60c6ed2c78a355c47fcaeef3bcc375b5f8ced9aae0c8f6dd81b03c809b45f8480e13721da526abf599069d5697f55a0bec2f156f504680cd12b1ec5dc5b89d84ae4982c96c70c15f333ebaca6000c11edc9e4b8f5bec432cf137d9d98a42c42dd8769c8ea524dc459609d5353a9af80786586b2f66bff7d334e542b01611e83b1616ca282e8af00e27ef70fbce1571ddf956387af0ee0a3a51562cd7f449e3760e72401d49d8b15cdf5091cfd30a8fe1301cce3b7454d13a4741158bfe173d3fa1c14030a858296c3ec99eadec01e049117828436a701cd0cbe580872f6ac4ba9a8acf32695a8a7288d85db64015666014d1d060a3313bc9643164211bd6e5105a210b79965dd65f35d9a633eb128dbabd7b0b617fe5cbefe93608629fe8f8fd0ea9bf51b190dda06fa8802dce856a601c05d5a3ca234034a70827b5ca103c068a977b5af074f9ad6382bbab1807666425b39492d833f9bc2cc538c2bd7ddae7e9605dd5c791849fc52996418ac1486cc9522491c8e1f474b33e7b6376a6de5c8dc13d3aa6b458a448c2ef042a3215e12a92a4df6332ee3134c2ae7be7cf4c82ac1c514ca083f3b0762ac8d16bf58d360a75a53e4f1d3fecc558eafe762a7410cb1ba2f3b455b21e4613f66c1b5bdf5e867d49d1331bc0067b785124d3ec00994022385b513c9bd7cbe6db4ae0ccb16a3e930e5107877abf55566e15e172fb59ab5ba8ab870793dc62dfab5c8330116ebf2deb24d46fa04670f5734d6ee808f5e365ad12472f98e6559a0951243212f462cf9eec645d96c9580f071f3295ca684a2af62b87a5046360ac8fbb7d63850eecd8c80dda7d4b8a40bb5c8a4083d352c45a738573d693b0dfb1fd269d63919caebc17166a895aa5269c7b54186ccac77afe7e90d6437d833312f1ab8c464b498a36916b3ec67a0ad876174eca9fe95e7a898c4663f3a4918d8511ec6a153a5d5ccd08d7df8cf08b77cf3394ac294f68251152c710b6f5243fd4c79de94435f876e03eb31f623e2862dd8d1308cdd579d9bc027eb85368e8c772740f2f63f05fc1fe7d9110804f0e10636d96e1005662cead5f68792fc2ab651aa321eca94ede5bef2f2bf35778714ccefe7b9f4ed54a5cced349da15b91459c4d6d4201f161c4951eeb648da35ed1fa524862a623659b20cf8fd67ae57323db7a44ecc785d26c32a22b455c1c396952215942b5f56a202043fbea121809d8b580df19dab13bcc5425739d75f2154b5a0d43e59798941f2047fb1a6414662c8aebbc0df7556c82fe15bdb10fed3a2cfc7e72f08373bc3421f888b267ca595f556f2b50d3e4fb17f7418a7aacfb98a41090d92eeda80ec03407b578390eff07b6dbcd7d10647bfd18f85ad95d1e3e6f10964deacdba737c757c0e682b699d1800ddebde7f53232835fe7289bdf0ad7044e6af8c32b1894802089f29e9388a18109c9b5fbc69af8ea13fc5033864cdf6c613669a51b382255aa38a8175f35ca3b6c5c5f2b62afab973083905e8e88d52c91ddec1a92ac37efca5e63c9cc44c27525a5302a4ae2e7b3b9132e54f4dbef8407fd96dedfc164400c6fce0f306ffe56597aa07325796c790feb1c44b5f8815c1ebf569d22f6af0532b585ae0f0d099503fe5c0f5bd58e84ead8d44eaf591c2014ae86eb52c84b5524516f36c79bb2f566bc31758d371419a278e27a755826fa1086bdd27f14871bab7cc4bb85c13605fd4e794f21dddaa059c6dda6a8d826d8b46df32b0f5a02f5c595f407131abca818b2756b6ac229f83361590473ac362057b8ae9927dca95cef007facc75fd883a525fc1d3ac31260032e9d5736fa1a220cb5f1e5bd307b7ef718867a6dfbd690d4e3fa0f1a080f8d6a0a0000'
hex_data=hex_data.replace(":", "")

alliance_name = "迷人又可爱的"
# alliance_name = "可爱又迷人的"
# alliance_name = "玉子烧的小屋"

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