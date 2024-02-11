import re
import os

inputpath = ".\\common\\characters\\"
outputpath = ".\\_tool\\Focusestool\\"
inputfilename = "ITA_new_characters.txt"

if ".txt" not in inputfilename:
    inputfilename = inputfilename + ".txt"
if not os.path.exists(outputpath):
    os.makedirs(outputpath)

iputfullpath = inputpath + inputfilename

if not os.path.exists(iputfullpath):
    print("输入错了")
    os.system("pause")
else:
    print("对了，这玩意存在")

# 读取文件内容
with open(iputfullpath, "r+", encoding="utf-8") as f:
    lines = f.readlines()

# 处理文件流
output_lines = []
stack = 0  # 用栈来处理大括号的嵌套结构
name_value = None  # 用于存储 name = 后的内容
for line in lines:
    # 使用正则表达式找到国策名称并修改
    if "{" in line:
        stack += 1
    if "}" in line:
        stack -= 1

    match_name = re.match(r"\s*name\s*=\s*(\w+)", line)
    if match_name and stack == 2:
        name_value = match_name.group(1)

    if stack == 4 and "small =" in line:
        match_small = re.match(r"\s*small\s*=\s*(\w+)", line)
        if match_small:
            new_small_value = "GFX_idea_" + name_value.lower()
            line = re.sub(match_small.group(1), new_small_value, line)

    output_lines.append(line)

# 输出到新的txt文件
outputfilename = inputfilename[:-4] + "_modified.txt"
with open(outputpath + outputfilename, "w", encoding="utf-8") as f:
    f.writelines(output_lines)

print("处理完成，输出文件为:", outputfilename)
