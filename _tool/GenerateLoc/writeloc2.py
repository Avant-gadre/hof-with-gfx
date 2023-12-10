import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 要读取的文件名
file_name1 = "text1.txt"  # 替换为你的文件名

file_name2 = "text2.txt"  # 替换为你的文件名

# 文件路径
file_path1 = os.path.join(current_dir, file_name1)

file_path2 = os.path.join(current_dir, file_name2)

target = "Generic_trait_"

with open(file_path1, "r") as file:
    lines = file.readlines()

lines.sort()

with open(file_path2, "w") as file:
    file.truncate(0)
    for line in lines:
        prefix = line.strip()  # 去除行末尾的换行符等空白字符
        name0 = prefix[len(target):].replace("_", " ").title().strip()  # 去除生成的字符串首尾空白
        full = " " + prefix + ":" + " " + '"' + name0 + '"'
        file.write(full + '\n')  # 写入行并添加换行符
