
import json
import os

# 从文件中读取字符字典
file_path = "D:\\Documents\\GitHub\\Test\\common\\characters\\CHI_Fate_Characters.txt"  # 替换为实际文件路径
characters = {}
with open(file_path, "r") as file:
    for line in file:
        if '=' in line:
            key, value = line.strip().split('=')
            characters[key.strip()] = {"name": value.strip()}

def transform_string(s):
    parts = s.split('_')
    parts[0] = parts[0].upper()
    for i in range(1, len(parts)):
        parts[i] = parts[i].capitalize()
    return "_".join(parts)

# 转换字典中的字符元素
for key, value in characters.items():
    characters[key]["name"] = transform_string(value["name"])

# 将转换后的字符字典写回文件
with open(file_path, "w") as file:
    for key, value in characters.items():
        file.write(f"{key} = {value['name']}\n")