import os

# 定义文件路径
path = ".//text.txt"
path1 = ".//text1.txt"
path2 = ".//text2.txt"
path3 = ".//text3.txt"
path4 = ".//text4.txt"

target = "GER_"

# 获取当前脚本文件的路径
script_path = os.path.abspath(__file__)

# 构建相对路径
path1 = os.path.join(os.path.dirname(script_path), path1)
path2 = os.path.join(os.path.dirname(script_path), path2)

with open(path1, "r") as file:
    lines = file.readlines()

with open(path2, "w") as file:
    for line in lines:
        prefix = line.strip()
        name0 = prefix[len(target) :].replace("_", " ").title().strip()
        full = " " + prefix + ":" + " " + '"' + name0 + '"'
        file.write(full + "\n")
