import os

# 定义模板
tempa = """
text = {{
    trigger = {{
        has_country_leader_ideology = {}
    }}
    localization_key = {}
}}
"""
temp = """
	spriteType = {{
		name = "GFX_ideology_{}"
		texturefile = "gfx/interface/ideologies/Neutrality/{}.png"
	}}
"""

# 获取当前脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# 定义相对路径的文件名
input_file_path = os.path.join(script_directory, 'text1.txt')
output_file_path = os.path.join(script_directory, 'text2.txt')

# 打开输入文件以读取
with open(input_file_path, 'r') as input_file:
    # 初始化一个空文本字符串
    output_text = ""

    # 逐行读取输入文件内容
    for line in input_file:
        # 在每一行后添加到输出文本字符串，并应用模板
        filled_text = tempa.format(line.strip(), line.strip())
        output_text += filled_text

# 打开输出文件以写入
with open(output_file_path, 'w') as output_file:
    # 将整个文本字符串写入输出文件
    output_file.write(output_text)

print("文件处理完成。")
