import re
import os
import io
import os.path

inputpath = 'USA_Fate_Character1.txt'
outputpath = 'text2.txt'

counter_leave = 0

f = open(inputpath,'r+', encoding='utf-8')

lines = f.readlines()

f.close()

namelist = []

for line in lines:
    if counter_leave == 1 and ' = {' in line :
        # 这一行是id
        id = re.sub(r'= {','',line).strip()
        namelist.append(id)
    counter_leave += line.count('{')
    counter_leave -= line.count('}')


f = open(outputpath , 'w', encoding='utf-8')
for name in namelist:
    desc = "recruit_character = "
    f.write(desc+name+"\n")
f.close()
