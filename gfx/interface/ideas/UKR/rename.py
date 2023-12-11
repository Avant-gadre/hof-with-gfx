import os

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

        new_file_name = file_name
        
        targetname = "idea_pol_"
    
        targetname1 = "idea_generic_"

        targetname2 = "idea_ukr_"

       
        if new_file_name.startswith(targetname):
            new_file_name1 = targetname2 + new_file_name[len(targetname):].lower()
            new_file_name = new_file_name1
            os.rename(file_path, os.path.join(folder_path, new_file_name))
            print(f"文件 {file_name} 已重命名为 {new_file_name}")

        # if not new_file_name.startswith(targetname1):
        #     new_file_name1 = targetname1 + new_file_name
        #     new_file_name = new_file_name1
        #     os.rename(file_path, os.path.join(folder_path, new_file_name))
        #     print(f"文件 {file_name} 已重命名为 {new_file_name}")



# for filename in os.listdir(folder_path):
#     if "(" in filename and ")" in filename:
#         new_filename = filename.replace(" ", "_").replace("(", "_").replace(")", "").replace("_", "", 1)
#         new_filename = new_filename.replace("(", "_").replace(")", "").replace("__", "_")
#         os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
#         print(f"文件名已更新：{filename} -> {new_filename}")
#     else:
#         print(f"文件名中不含有（1）、（2）等：{filename}")

            