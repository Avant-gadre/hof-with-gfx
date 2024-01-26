import os

# 获取当前脚本所在的目录
inputpath = ".\\localisation\\english\\"
outputpath = ".\\_tool\\SortTrait\\"
inputfilename = "modifiers_l_english.yml"
if ".yml" not in inputfilename:
    inputfilename = inputfilename + ".yml"
if not os.path.exists(outputpath):
    os.makedirs(outputpath)

inputfullpath = os.path.join(inputpath, inputfilename)

outputpath = os.path.join(outputpath, inputfilename)

if not os.path.exists(inputfullpath):
    print("输入错了")
    os.system("pause")
else:
    print("对了，这玩意存在")

with open(inputfullpath, "r") as file:
    # 逐行读取文件内容
    lines = file.readlines()

    lines = [line.strip() for line in file if line.strip()]

# 按照冒号前的内容进行排序
sorted_lines = sorted(lines, key=lambda line: line.split(":")[0])

# 打开文件并写入排序后的内容
with open(outputpath, "w") as file:
    file.writelines(sorted_lines)
