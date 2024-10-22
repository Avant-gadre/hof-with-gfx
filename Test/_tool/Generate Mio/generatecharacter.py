import os
##读取文件
folder_path = ".//_tool//GenerateCharacterLoc//portraits"

folder_path1 = ".//_tool//GenerateCharacterLoc"

output1 = os.path.join(folder_path1, 'generatecharacter.txt')
output2 = os.path.join(folder_path1, 'generatecharacterloc.txt')
output3 = os.path.join(folder_path1, 'generatecharacterhistory.txt')

files = os.listdir(folder_path)
# 要删除的特定前缀和后缀
prefix_to_remove = "Portrait_"
suffix_to_remove = ".png"  # 你想要删除的后缀，例如 ".txt"
# 处理文件名并存入集合
files_set = set()
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

##格式-海军
characters_string1 = '''
	{} = {{
		name = {}
		portraits = {{
			civilian = {{
				small = GFX_idea_advisor_unknow_pol
				large = GFX_Portrait_{}
			}}
			army = {{
				small = GFX_idea_advisor_unknow_mil
				large = GFX_Portrait_{}
			}}
		}}
		navy_leader = {{
			traits = {{
				naval_lineage
			}}
			skill = 3
			attack_skill = 3
			defense_skill = 3
			maneuvering_skill = 3
			coordination_skill = 3
		}}
		advisor = {{
			slot = navy_chief
			idea_token = {}
			ledger = navy
			cost = 100
			traits = {{
				navy_chief_reform_2
			}}
		}}
	}}
'''

##格式-陆军
characters_string = '''
	{} = {{
		name = {}
		portraits = {{
			civilian = {{
				small = GFX_idea_advisor_unknow_pol
				large = GFX_Portrait_{}
			}}
			army = {{
				small = GFX_idea_advisor_unknow_mil
				large = GFX_Portrait_{}
			}}
		}}
		corps_commander = {{
			traits = {{
                organizer
			}}
			skill = 2
			attack_skill = 2
			defense_skill = 2
			planning_skill = 2
			logistics_skill = 2
		}}
		advisor = {{
			slot = army_chief
			idea_token = {}
			ledger = army
			cost = 100
			traits = {{
				army_chief_reform_2
			}}
		}}
	}}
'''

with open(output1 , 'a') as file:
    file.truncate(0)
    for name in files_set:
        name1 = name[:4]+name[4:].lower()
        formatted_characters_string = characters_string.format(name1, name1, name, name, name1)
        file.write(formatted_characters_string+"\n")
    file.close()

with open(output2 , 'a') as file1:
    file1.truncate(0)
    for name in files_set:
        name1 = name[:4]+name[4:].lower()
        name0 = name[4:].replace("_", " ").title()
        full = name1+":"+" "+"\""+name0+"\""
        file1.write(full+"\n")
    file1.close()

with open(output3 , 'a') as file2:
    file2.truncate(0)
    for name in files_set:
        name1 = name[:4]+name[4:].lower()
        desc = "recruit_character = "
        file2.write(desc+name1+"\n")
    file2.close()
