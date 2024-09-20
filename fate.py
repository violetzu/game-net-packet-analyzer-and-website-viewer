import os
import easyocr
import cv2
from main_by_ocr import Data_collation ,main

directory = "picture"

def write_txt(filename,File):
    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
        for item in File:
            file.write(str(item) + "\n")
    
# 1920*1920 input
def perform_ocr():
    

    files = sorted(os.listdir(directory), key=str.lower)

    reader = easyocr.Reader(["en", "ch_sim"])
    raw_data=[]
    for filenum, filename in enumerate(files):
        # print(f'{filenum+1}')
        print(filename)
        img_path = os.path.join(directory, filename)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        result = reader.readtext(img[140:1780,600:1500], detail=0)
        raw_data.append(result)
        # try:
        #     if os.path.isfile(img_path):
        #         os.remove(img_path)
        # except Exception as e:
        #     print(f"Failed to delete {img_path}. Reason: {e}")

    return raw_data


raw_data = perform_ocr()
write_txt("raw_data",raw_data)
data = main(raw_data)
Data_collation(data)




