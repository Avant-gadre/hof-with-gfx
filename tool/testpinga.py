statement_template = '''
else_if = {{
    limit = {{
        has_idea = BEY_political_status{0}_idea
    }}
    swap_ideas = {{
        remove_idea = BEY_political_status{0}_idea
        add_idea = BEY_political_status{1}_idea
    }}
}}
'''

for i in range(1, 12):
    current_statement = statement_template.format(i, i + 1)
    print(current_statement)