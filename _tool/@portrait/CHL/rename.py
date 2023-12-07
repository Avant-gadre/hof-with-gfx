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
        
        targetname = "Portrait_Chile_"

        targetname1 = "focus_"+targetname

       
        if new_file_name.startswith(targetname):
           ##print(new_file_name)
           new_file_name1 = "Portrait_CHL_" + new_file_name[len(targetname):]
           new_file_name = new_file_name1
           # new_file_name = new_file_name[:len(targetname1)]+new_file_name[len(targetname1):].lower()
        
        os.rename(file_path, os.path.join(folder_path, new_file_name))
        print(f"文件 {file_name} 已重命名为 {new_file_name}")

        #print(new_file_name1)