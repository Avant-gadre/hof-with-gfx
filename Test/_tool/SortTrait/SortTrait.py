import os

# 获取当前脚本所在的目录
inputpath = ".\\common\\country_leader\\"
outputpath = ".\\_tool\\Focusestool\\"
inputfilename = "_Generic_traits.txt"

if ".txt" not in inputfilename:
    inputfilename = inputfilename + ".txt"
if not os.path.exists(outputpath):
    os.makedirs(outputpath)

inputfullpath = os.path.join(inputpath, inputfilename)

if not os.path.exists(inputfullpath):
    print("输入错了")
    os.system("pause")
else:
    print("对了，这玩意存在")

# 读取输入文件
with open(inputfullpath, "r") as input_file:
    input_str = input_file.read()

# 将输入字符串按行分割
lines = input_str.split("\n")

# 创建一个字典，用于存储每个变量的内容
variables = {}

kampf = 0  ##栈
i = 1

# 遍历每行
for line in lines:
    if "{" in line:
        kampf += 1
        if kampf == 2:
            # 读取变量名
            variable_name = line.split("=")[0].strip()

            # 提取变量内容，包含花括号内的所有内容
            start_index = i

            end_index = start_index

            # 记录括号的嵌套结构
            open_brackets = 1
            ##
            j = end_index

            # 遍历后续行，直到找到对应的反括号
            while j < len(lines):
                line = lines[j]  # 修改此处的 i 为 j
                if "{" in line:
                    open_brackets += 1
                elif "}" in line:
                    open_brackets -= 1

                if open_brackets == 0:
                    break
                j += 1

            variable_content = "\n".join(lines[start_index + 1 : j])  # 修改此处的 j - 1 为 j

            # 存储到字典中
            variables[variable_name] = variable_content

    elif "}" in line:
        kampf -= 1

    i += 1

# 按变量名排序
sorted_variables = sorted(variables.items())

# 构建输出字符串
output_str = ""
for variable_name, variable_content in sorted_variables:
    output_str += f"{variable_name} = {{\n{variable_content}\n}}\n"

# 将结果写入新文件
with open(outputpath + inputfilename, "w") as output_file:
    output_file.write(output_str)

print(f"结果已保存到文件")
