import os

current_file_path = os.path.abspath(__file__)
folder_path = os.path.dirname(current_file_path)
file_name = "00 UKR_Fate_focus.txt"
file_path = os.path.join(folder_path, file_name)

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 处理文件内容
modified_lines = []
for line in lines:
    if 'icon =' in line:
        parts = line.split('icon =', 1)
        leading_spaces = len(line) - len(line.lstrip())
        if len(parts) > 1 and parts[1].strip().startswith('GFX_focus') and leading_spaces <= 2:
            char = "GFX_focus_GER_"
            parts[1] = parts[1][:len(char)] + parts[1][len(char):].lower()
            line = parts[0] + 'icon =' + parts[1]
    modified_lines.append(line)

# 将修改后的内容写回文件
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)