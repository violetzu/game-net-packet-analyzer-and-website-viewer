import os
import easyocr
import cv2
import json
directory = "C:/wamp64/ranking/ocr version/alliance"

# alliance_name="迷人又可爱的"
# alliance_name="可爱又迷人的"
alliance_name="夜澀"
# alliance_name="ロスモンティス"

# 1920*1920 input

with open("corrections.json", "r", encoding="utf-8") as f:
    corrections = json.load(f)

def perform_ocr():
    files = sorted(os.listdir(directory))
    reader = easyocr.Reader(["en","ch_sim"])
    member=[]
    for filenum, filename in enumerate(files):
        print(f'{filenum+1}')
        # img_path = os.path.join(directory, filename)
        img_path = f'{directory}/{filename}'
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        # result = reader.readtext(img[250:1840,1060:1500], detail=0)
        result = reader.readtext(img, detail=0)

        for i in result:
            # print(i)
            if "#" in i:
                sever=int(i.split('#')[0].strip().replace("I","1").replace("G","6"))
                name = f"#{sever if sever>9 else f"0{sever}"} {i.split('#')[-1].strip()}"
                corrections_name = corrections.get(name, name)
                # .replace(' ', '')
                if corrections_name not in member:
                    member.append(corrections_name)  
                else:
                    pass

    return member

member = perform_ocr()

def main(member):
    with open('../alliance.json', 'r', encoding='utf-8') as file:
        alliance = json.load(file)

    old_member = alliance[alliance_name]
    alliance[alliance_name] = member

    leave=[]
    join=[]
    for i in old_member:
        if i not in member:
            leave.append(i)

    for i in member:
        if i not in old_member:
            join.append(i)

    print(f"join{join}")
    print(f"leave{leave}")
    return alliance


while True:
    alliance=main(member)
    check=str(input('是否儲存(Y):'))
    if check=='Y':
        with open('../alliance.json', 'w', encoding='utf-8') as file:
            json.dump(alliance, file, ensure_ascii=False, indent=4)
            break
    elif check=='N':
        continue

# print(member)