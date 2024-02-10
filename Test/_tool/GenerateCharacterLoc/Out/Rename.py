import os

current_file_path = os.path.abspath(__file__)

# 获取包含该文件的文件夹路径
folder_path = os.path.dirname(current_file_path)

# 列出当前文件夹所有文件
files = os.listdir(folder_path)

target_type = ".png"

for file_name in files:
    # 构建文件的完整路径
    file_path = os.path.join(folder_path, file_name)

    # 检查是否是文件且是.png文件
    if os.path.isfile(file_path) and file_name.lower().endswith(target_type):
        # 构建目标文件名
        target_prefix = "Portrait_IRE_"
        target_suffix = " copy" + target_type
        new_prefix = "ire_"
        BoolLower = 0

        if file_name.startswith(target_prefix) and file_name.endswith(target_suffix):
            # 提取文件名部分（去除前缀和后缀）
            name_part = file_name[len(target_prefix) : -len(target_suffix)].lower()

            # 使用下划线分割，并首字母大写
            output_string = "_".join(word.capitalize() for word in name_part.split("_"))

            # 构建新的文件名
            new_file_name = new_prefix + output_string.lower() + target_type

            # 构建新的文件路径
            new_file_path = os.path.join(folder_path, new_file_name)

            # 重命名文件
            os.rename(file_path, new_file_path)

            print(f"文件 {file_name} 已重命名为 {new_file_name}")

        elif file_name.startswith(target_prefix):
            # 提取文件名部分（去除前缀和后缀）
            name_part = file_name[len(target_prefix) :].lower()

            # 使用下划线分割，并首字母大写
            output_string = "_".join(word.capitalize() for word in name_part.split("_"))

            # 构建新的文件名
            new_file_name = new_prefix + output_string.lower()

            # 构建新的文件路径
            new_file_path = os.path.join(folder_path, new_file_name)

            # 重命名文件
            os.rename(file_path, new_file_path)

            print(f"文件 {file_name} 已重命名为 {new_file_name}")
