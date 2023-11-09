import re
import os
import io
import os.path
import sys
import datetime
# sys.path.append('../')
import core


focusNow = os.path.join(core.focuspath,'00 RHI_Fate_focus.txt')
with open(focusNow,'r+') as f:
    focusfull = f.readlines()
for line in focusfull:
    line = re.sub(r'#.+','',line)
    # print(line)
# 搜索id
idlist = []
for line in focusfull:
    if re.match('\t\tid = ',line):
        line = line.split('=')[1]
        idlist.append(line)
outputpath = os.path.join(core.rootpath,'tool','focus_tool','RHI_loc.yml')

with open(outputpath,'w',encoding='utf-8-sig') as f2:
    f2.write('l_english:\n')
    for idname in idlist:
        id_loc = ' ' + idname.strip() + ': "placeholder"\n'
        id_desc_loc = ' ' + idname.strip() + '_desc: "placeholder"\n'

        f2.write(id_loc)
        f2.write(id_desc_loc)
