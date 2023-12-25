import os

file_name1 = "text1.txt"
file_name2 = "text2.txt"

# 获取当前脚本文件的路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 文件路径
file_path1 = os.path.join(current_dir, file_name1)
file_path2 = os.path.join(current_dir, file_name2)

set_variable = "set_variable"
template = "{} = {{ {} = 0 }}\n"

output_lines = []  # 用于保存处理后的内容

with open(file_path1, "r", encoding="utf-8") as file1:
    for line in file1:
        line = line.strip()  # 移除行末尾的换行符和空白
        output_line = template.format(set_variable, line)
        output_lines.append(output_line)

with open(file_path2, "w", encoding="utf-8") as file2:
    file2.writelines(output_lines)