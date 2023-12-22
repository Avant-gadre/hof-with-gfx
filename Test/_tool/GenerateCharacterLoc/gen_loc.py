characters_string = """
	{} = {{
		type = navy
		trait_type = personality_trait
		new_commander_weight = {{
			factor = 0
		}}
	}}
"""

import os
##读取文件
folder_path = ".//_tool//GenerateCharacterLoc//portraits"

folder_path1 = ".//_tool//GenerateCharacterLoc"

output1 = os.path.join(folder_path1, 'generatecharacter.txt')
output2 = os.path.join(folder_path1, 'generatecharacterloc.txt')

files = os.listdir(folder_path)

# 要删除的特定前缀和后缀

prefix_to_remove = "trait_"
suffix_to_remove = ".png"  # 你想要删除的后缀，例如 ".txt"

# 处理文件名并存入集合
files_list = []  # 这是一个文件名列表
files_set = set(files_list) 

for file_name in files:
    # 检查文件名是否以特定前缀开头
    if file_name.startswith(prefix_to_remove):
        # 删除特定前缀
        file_name = file_name[len(prefix_to_remove):]

    # 检查文件名是否以特定后缀结尾
    if file_name.endswith(suffix_to_remove):
        # 删除特定后缀
        file_name = file_name[:-len(suffix_to_remove)]

    files_set.add(file_name)

# 对 files_set 进行排序并更新原始集合
files_set = sorted(files_set)


with open(output1 , 'a') as file:
    file.truncate(0)
    for name in files_set:
        formatted_characters_string = characters_string.format(name)
        file.write(formatted_characters_string+"\n")
    file.close()

with open(output2 , 'a') as file1:
    file1.truncate(0)
    for name in files_set:
        first_index = name.find('_')
        first_index = 0
        name0 = name[first_index:].replace("_", " ").title()
        name0 = name0.strip()
        full = prefix_to_remove + name + ":" + " " + "\"" + name0 + "\""
        file1.write(full+"\n")

    file1.close()

