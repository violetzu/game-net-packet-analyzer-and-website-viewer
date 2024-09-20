import json

def write_txt(filename,File):
    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
        for item in File:
            file.write(str(item) + "\n")


def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)