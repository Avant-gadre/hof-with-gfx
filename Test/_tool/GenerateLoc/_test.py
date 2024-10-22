import os
# 获取当前 Python 脚本的文件路径
current_file_path = os.path.abspath(__file__)

# 获取包含该文件的文件夹路径
folder_path = os.path.dirname(current_file_path)

# 列出当前文件夹所有文件
files = os.listdir(folder_path)

for file_name in files:
    # 构建文件的完整路径
    file_path = os.path.join(folder_path, file_name)
    
    # 检查是否是文件且是.png文件
    if os.path.isfile(file_path) and file_name.lower().endswith('.png'):
        # 1. 将文件名中的所有大写字母变为小写
        new_file_name = file_name.lower()
        
        target = "yun"

        # 2. 开头有goal_的改名为focus_generic_开头
        if new_file_name.startswith(target):
            new_file_name = 'idea_chi' + new_file_name[len(target):]

        # elif new_file_name.startswith('idea'):
        #     new_file_name = 'rom' + new_file_name[len('idea'):]
        
        # # 4. 开头既没有focus_也没有goal_的加上focus_generic_
        # elif not new_file_name.startswith('focus_') and not new_file_name.startswith('focus_generic_'):
        #     new_file_name = 'focus_generic_' + new_file_name
        
        os.rename(file_path, os.path.join(folder_path, new_file_name))
        print(f"文件 {file_name} 已重命名为 {new_file_name}")