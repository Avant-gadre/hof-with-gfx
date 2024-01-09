import os
import glob

def merge_yaml_files_in_current_directory(output_file):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(current_directory, output_file)

    yaml_files = glob.glob(os.path.join(current_directory, '*.yml'))  # 修改此行

    with open(output_path, 'w', encoding='utf-8') as output:
        for yaml_file in yaml_files:
            with open(yaml_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                output.writelines(lines)

# 指定输出文件名
output_file = '_output.yml'

# 调用函数合并当前文件夹中的所有YAML文件到输出文件中
merge_yaml_files_in_current_directory(output_file)
