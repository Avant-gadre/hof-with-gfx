import re
import os

inputpath = ".\\common\\ideas\\"
outputpath = ".\\_tool\\Focusestool\\"
inputfilename = "BEL_ideas.txt"

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
for line in lines:
    # 使用正则表达式找到国策名称并修改

    if "{" in line:
        stack += 1
    if "}" in line:
        stack -= 1

    match = re.match(r"\s*(\w+)\s*=\s*{", line)
    if (
        match and stack == 3 and not match.group(1).endswith("_idea")
    ):  # 只在栈为3且不以"_idea"结尾时匹配
        new_idea_name = match.group(1)[:3] + match.group(1)[3:].lower() + "_idea"
        line = re.sub(match.group(1) + r"\b", new_idea_name, line)  # 使用\b确保匹配单词边界
    elif match and stack == 3:
        new_idea_name = match.group(1)[:3] + match.group(1)[3:].lower()
        line = re.sub(match.group(1) + r"\b", new_idea_name, line)

    if stack == 3 and "picture =" in line:
        line = line.lower()

    output_lines.append(line)


# 输出到新的txt文件
outputfilename = inputfilename[:-4] + "_modified.txt"
with open(outputpath + outputfilename, "w", encoding="utf-8") as f:
    f.writelines(output_lines)

print("处理完成，输出文件为:", outputfilename)
