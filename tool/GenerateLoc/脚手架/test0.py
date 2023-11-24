import fileinput
import os

current_file_path = os.path.abspath(__file__)
folder_path = os.path.dirname(current_file_path)
file_name = "00 POL_Fate_focus.txt"
file_path = os.path.join(folder_path, file_name)

# 以原位置模式打开文件，将icon = 后面的内容替换为小写形式
with fileinput.FileInput(file_path, inplace=True, backup='') as file:
    for line in file:
        if 'icon =' in line:
            parts = line.split('icon =', 1)
            leading_spaces = len(line) - len(line.lstrip())
            if leading_spaces <= 2:
                if len(parts) > 1:
                    char = "GFX_focus_GER_"
                    parts[1] = parts[1][:len(char)] + parts[1][len(char):].lower()
                    new_content = parts[0] + 'icon =' + parts[1]
                    print(new_content, end='')
                else:
                    print(line, end='')
            else:
                print(line, end='')
        else:
            print(line, end='')