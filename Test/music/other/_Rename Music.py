import os
import re


def capitalize_after_underscore(s):
    # 使用正则表达式分割，并下划线后的第一个字母大写
    return re.sub(r"_(\w)", lambda m: "_" + m.group(1).capitalize(), s)


def process_filename_without_brackets(filename):
    # 提取括号外的部分
    parts = re.split(r"(\([^)]*\))", filename)
    processed_parts = [
        capitalize_after_underscore(part) if "(" not in part else part for part in parts
    ]
    processed_parts[0] = processed_parts[0].capitalize()
    return "".join(processed_parts)


current_file_path = os.path.abspath(__file__)

# 获取包含该文件的文件夹路径
folder_path = os.path.dirname(current_file_path)

# 列出当前文件夹所有文件
files = os.listdir(folder_path)

target_type = ".ogg"

for file_name in files:
    # 构建文件的完整路径
    file_path = os.path.join(folder_path, file_name)

    # 检查是否是文件且是.ogg文件
    if os.path.isfile(file_path) and file_name.lower().endswith(target_type):
        # 构建目标文件名
        target_prefix = "Ent_"
        target_suffix = "11111png" + target_type
        new_prefix = ""
        BoolLower = 0

        if file_name.startswith(target_prefix) and file_name.endswith(target_suffix):
            # 提取文件名部分（去除前缀和后缀）
            name_part = file_name[len(target_prefix) : -len(target_suffix)]

            # 处理不包含括号的部分
            output_string = capitalize_after_underscore(name_part)

            # 构建新的文件名
            new_file_name = new_prefix + output_string.lower() + target_type

            # 构建新的文件路径
            new_file_path = os.path.join(folder_path, new_file_name)

            # 重命名文件
            os.rename(file_path, new_file_path)

            print(f"文件 {file_name} 已重命名为 {new_file_name}")

        elif file_name.startswith(target_prefix):
            # 提取文件名部分（去除前缀和后缀）
            name_part = file_name[len(target_prefix) :]

            name_part = name_part.replace("-", "_")

            # 处理包含括号的部分
            processed_name = process_filename_without_brackets(name_part)

            # 构建新的文件名
            new_file_name = new_prefix + processed_name

            print(processed_name)

            # 构建新的文件路径
            new_file_path = os.path.join(folder_path, new_file_name)

            # 重命名文件
            os.rename(file_path, new_file_path)

            print(f"文件 {file_name} 已重命名为 {new_file_name}")
