import os

# 获取当前脚本文件的路径
script_path = os.path.abspath(__file__)

# 定义目标文件的相对路径（相对于脚本文件所在目录）
output_path = "text2.txt"
output_full_path = os.path.join(os.path.dirname(script_path), output_path)

# statement模板
statement_template = """
country_event = {{
	id = {target}.{0}
	title = {target}.{0}.title
	desc = {target}.{0}.desc
	immediate = {{
	}}
	picture = GFX_report_event_generic_diplomacy1
	is_triggered_only = yes
	fire_only_once = yes
	option = {{
		name = {target}.{0}.a
        trigger = {{
		}}
		ai_chance = {{
			base = 1
		}}
	}}
    option = {{
		name = {target}.{0}.b
		trigger = {{
		}}
		ai_chance = {{
			base = 1
		}}
	}}
	option = {{
		name = {target}.{0}.c
		trigger = {{
		}}
		ai_chance = {{
			base = 1
		}}
	}}
}}
"""



statement_template1 = """
news_event = {{
	id = {target}.{0}
	title = {target}.{0}.title
	desc = {target}.{0}.desc
	immediate = {{
	}}
	picture = GFX_news_event_generic_nero
	is_triggered_only = yes
	fire_only_once = yes
    major = yes
	option = {{
		name = {target}.{0}.a
		ai_chance = {{
			base = 1
		}}
	}}
	option = {{
		name = {target}.{0}.b
		trigger = {{
		}}
		ai_chance = {{
			base = 1
		}}
	}}
	option = {{
		name = {target}.{0}.c
		trigger = {{
		}}
		ai_chance = {{
			base = 1
		}}
	}}
}}
"""


target = "fra_ciel"

with open(output_full_path, "w") as file:
    for i in range(1, 6):
        current_statement = statement_template.format(i,target=target)
        file.write(current_statement)
