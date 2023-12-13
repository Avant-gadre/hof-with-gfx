statement_template = '''
else_if = {{
    limit = {{
        has_idea = MEX_cedillo_tension_{0}_idea
    }}
    swap_ideas = {{
        remove_idea = MEX_cedillo_tension_{0}_idea
        add_idea = MEX_cedillo_tension_{1}_idea
    }}
}}
'''

for i in range(2 , 11):
    current_statement = statement_template.format(i, i - 1)
    print(current_statement)