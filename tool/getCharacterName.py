import re
import os
import io
import os.path

inputpath = '..\common\\characters\\'
outputpath = '.\\characterslist\\'
# inputfilename = input()
inputfilename = 'XSM_Fate_Characters'
if '.txt' not in inputfilename:
    inputfilename = inputfilename + '.txt'
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
counter_leave = 0
# 遇到{ +1  遇到} -1
# counter_leave = 1 时 为id
# counter_leave = 2 且name = 时为名字



iputfullpath = inputpath + inputfilename
if not os.path.exists(iputfullpath):
    # 检查是否存在该文件
    print('输入错了')
    os.system("pause")
else:
    print('对了，这玩意存在')
f = open(iputfullpath,'r+', encoding='utf-8')
lines = f.readlines()
f.close()

namelist = []
# print(lines[0])
for line in lines:
    if counter_leave == 1 and ' = {' in line :
        # 这一行是id
        id = re.sub(r'= {','',line).strip()
        namelist.append(id)
    counter_leave += line.count('{')
    counter_leave -= line.count('}')
f = open(outputpath + inputfilename, 'w', encoding='utf-8')
for name in namelist:
    full = 'recruit_character = ' + name + '\n'
    f.write(full)
f.close()
