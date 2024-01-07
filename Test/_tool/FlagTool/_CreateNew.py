import os
import shutil

# 获取脚本所在的文件夹路径
script_dir = os.path.dirname(__file__)

# 文件夹路径
folder_path = script_dir  # 将文件夹路径设置为脚本所在的文件夹路径

# 获取文件夹中所有文件
file_list = os.listdir(folder_path)

# 存储以三个大写字母命名的文件名，使用集合以避免重复
three_letter_files = set()

# 遍历文件，找到以三个大写字母命名的文件
for filename in file_list:
    if len(filename) == 7 and filename[:3].isupper():
        three_letter_files.add(filename[:3])
        print(filename[:3])

# 检查每个以三个大写字母命名的文件是否满足条件，并创建副本文件或生成 log 报告
for filename in three_letter_files:
    for suffix in [
        "_democratic.tga",
        "_communism.tga",
        "_neutrality.tga",
        "_fascism.tga",
    ]:
        if f"{filename}{suffix}" in file_list:
            if f"{filename}.tga" not in file_list:
                print(f"Error: {filename}.tga does not exist.")

        elif f"{filename}.tga" in file_list and not f"{filename}{suffix}" in file_list:
            original_file_path = os.path.join(folder_path, f"{filename}.tga")
            copy_file_path = os.path.join(folder_path, f"{filename}{suffix}")
            shutil.copyfile(original_file_path, copy_file_path)
            print(f"Created copy: {filename}{suffix}")
