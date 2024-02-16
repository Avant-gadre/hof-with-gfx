import os

file_name1 = "text1.txt"
file_name2 = "text2.txt"

# 获取当前脚本文件的路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 文件路径
file_path1 = os.path.join(current_dir, file_name1)
file_path2 = os.path.join(current_dir, file_name2)

pattern = """
    {}_modify_{}_off_{}_effect = {{
        if = {{
            limit = {{
                has_dynamic_modifier = {{
                    modifier = {}
                }}
            }}
            custom_effect_tooltip = {}_modify_{}_tooltip
            add_to_variable = {{
                var = {}
                value =  var:temp_variable
                tooltip = {}_tooltip
            }}
        }}
    }}
"""

## Example
target = "ROM_army_dm"
tag = target[:3]
name = target[4:]

output_lines = []  # 用于保存处理后的内容

with open(file_path1, "r", encoding="utf-8") as file1:
    for line in file1:
        line = line.strip()
        if line.startswith(target):
            modifier_name = line[len(target) + 1 :]
            output_line = pattern.format(
                tag, name, modifier_name, target, tag, name, line, modifier_name
            )
            output_lines.append(output_line)

# 将处理后的内容写入到 text2.txt 文件中
with open(file_path2, "w", encoding="utf-8") as file2:
    file2.writelines(output_lines)
