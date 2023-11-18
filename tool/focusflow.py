import re
import os
import io
import os.path

inputpath = '..\common\\national_focus\\'
outputpath = '.\\focus_flow\\'
# inputfilename = input()
inputfilename = '03 ISR_Fate_focus'
if '.txt' not in inputfilename:
    inputfilename = inputfilename + '.txt'
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
counter_leave = 0
# 遇到{ +1  遇到} -1
# counter_leave = 1 时 为id
# counter_leave = 2 且name = 时为名字

def GetRelative(lines):
    temp = ''
    for line in lines:
        if 'relative_position_id' in line:
            temp = line.strip()
            temp = re.sub(r'relative_position_id','',temp).strip()
            temp = re.sub(r'=', '', temp).strip()
    return temp

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

focuslist = []
fullfocuslist = []
idlist = []
templine = ''
focusnum = 0
focusblock = ''
filestart = []
# print(lines[0])
for line in lines:
    templine = line
    if counter_leave == 1 and '}' in line :
        # 到结尾了
        continue
        # 这是一个国策的结尾
    if counter_leave == 1 and '\tfocus' in line and '{' in line:
        # 这是一个国策的开头
        focusnum += 1
        focuslist = []
        focuslist.append(line)
    elif focusnum == 0:
        filestart.append(line)
    elif focusnum > 0:
        focuslist.append(line)
        if counter_leave == 2 and '\t}' in line:
            fullfocuslist.append(focuslist)
    if counter_leave == 2 and '\tid' in line and '=' in line:
        # 这是这个国策的id
        templine = re.sub(r'\tid','',templine).strip()
        templine = re.sub(r'=', '', templine).strip()
        idlist.append(templine)
    counter_leave += line.count('{')
    counter_leave -= line.count('}')
relativelist = []
for id in idlist:
    tempfocus = fullfocuslist[idlist.index(id)]
    relativeid = GetRelative(tempfocus)
    relativelist.append(relativeid)

print(len(idlist),len(fullfocuslist),len(relativelist))
reorderlist = []
for id in idlist:
    if relativelist[idlist.index(id)] == '':
        reorderlist.append(id)
        # 把0排进去

for cont in range(len(idlist)):
    for id in idlist:
        if relativelist[idlist.index(id)] in reorderlist and id not in reorderlist:
            temp1 = relativelist[idlist.index(id)]
            i = reorderlist.index(temp1) + 1
            reorderlist.insert(i,id)
# 输出
f = open(outputpath + inputfilename, 'w', encoding='utf-8')
f.write('\n'.join(filestart))
for reorder in reorderlist:

    fo = fullfocuslist[idlist.index(reorder)]
    f.write('\n'.join(fo))
    f.write('\n')
f.write('}')
f.close()
print(reorderlist)
