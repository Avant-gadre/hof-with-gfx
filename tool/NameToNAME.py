# 读取文件内容
local_path = 'D:\\Documents\\GitHub\\Test\\common\\characters\\CHI_Fate_Characters.txt'
# 读取文件内容
with open(local_path, 'r') as file:
    content = file.read()

# 使用正则表达式来匹配characters元素和name元素
import re

# 使用正则表达式匹配characters元素
character_blocks = re.findall(r'characters = {(.*?)}', content, re.DOTALL)

# 创建一个字典来存储替换后的内容
replacement_dict = {}

# 循环处理每个character块
for character_block in character_blocks:
    # 使用正则表达式匹配name元素和其值
    character_name_values = re.findall(r'(\w+)\s*=\s*{\s*name\s*=\s*(\w+)\s*}', character_block)
    
    # 处理每个name元素
    for character_name, name_value in character_name_values:
        # 分割name值
        parts = name_value.split('_')
        formatted_name = '_'.join([part.upper() if i == 0 else part.capitalize() for i, part in enumerate(parts)])
        
        # 存储替换后的内容到字典
        replacement_dict[name_value] = formatted_name

# 执行替换操作
for original, replacement in replacement_dict.items():
    content = content.replace(original, replacement)

# 将处理后的内容写回原文件
with open(local_path, 'w') as output_file:
    output_file.write(content)