import os

# 获取当前脚本文件的路径
script_path = os.path.abspath(__file__)

# 定义目标文件的相对路径（相对于脚本文件所在目录）
output_path = "text2.txt"
output_full_path = os.path.join(os.path.dirname(script_path), output_path)

# statement模板
statement_template = """
else_if = {{
    limit = {{
        has_idea = {target}_{0}_idea
    }}
    swap_ideas = {{
        remove_idea = {target}_{0}_idea
        add_idea =  {target}_{1}_idea
    }}
}}
"""

target = "ENG_global_defense"

with open(output_full_path, "w") as file:
    for i in range(0, 11):
        current_statement = statement_template.format(i , i+1 , target=target)
        file.write(current_statement)

import os
