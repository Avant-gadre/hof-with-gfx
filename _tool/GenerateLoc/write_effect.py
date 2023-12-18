target = "CZE_sudeten_concessions"

statement_template = """
else_if = {{
    limit = {{
        has_idea = {target}{0}_idea
    }}
    swap_ideas = {{
        remove_idea = {target}{0}_idea
        add_idea =  {target}{1}_idea
    }}
}}
"""

for i in range(1, 3):
    current_statement = statement_template.format(i, i+1, target=target)
    print(current_statement)