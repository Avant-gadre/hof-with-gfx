import os
##读取文件
folder_path = "./_workingplace"
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

##格式
characters_string = '''
	{} = {{
		name = {}
		portraits = {{
			civilian = {{
				small = "GFX_idea_advisor_unknow_pol"
				large = GFX_Portrait_{}
			}}
			army = {{
				small = "GFX_idea_advisor_unknow_mil"
				large = GFX_Portrait_{}
			}}
		}}
		navy_leader = {{
			traits = {{
				naval_lineage
				navy_career_officer
				torpedo_expert
				cruiser_captain
			}}
			skill = 3
			attack_skill = 3
			defense_skill = 3
			maneuvering_skill = 4
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

characters_string1 = '''
	{} = {{
		name = {}
		portraits = {{
			civilian = {{
				small = "GFX_idea_advisor_unknow_pol"
				large = GFX_Portrait_{}
			}}
			army = {{
				small = "GFX_idea_advisor_unknow_mil"
				large = GFX_Portrait_{}
			}}
		}}
		army_leader = {{
			traits = {{
				naval_lineage
				navy_career_officer
				torpedo_expert
				cruiser_captain
			}}
			skill = 3
			attack_skill = 3
			defense_skill = 3
			maneuvering_skill = 4
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

with open('generatecharacter.txt', 'a') as file:
    file.truncate(0)
    for name in files_set:
        formatted_characters_string = characters_string.format(name, name, name, name, name)
        file.write(formatted_characters_string+"\n")
    file.close()

with open('generatecharacterloc.txt', 'a') as file1:
    file1.truncate(0)
    for name in files_set:
        name0 = name[4:].replace("_", " ").title()
        full = name+":"+" "+"\""+name0+"\""
        file1.write(full+"\n")
    file1.close()

with open('generatecharacterhistory.txt', 'a') as file2:
    file2.truncate(0)
    for name in files_set:
        desc = "recruit_character = "
        file2.write(desc+name+"\n")
    file2.close()
