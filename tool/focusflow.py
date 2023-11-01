import re
import os
import io
import os.path

inputpath = '..\common\\national_focus\\'
outputpath = '.\\focus_flow\\'
# inputfilename = input()
inputfilename = '00 RUS_Fate_focus'
if '.txt' not in inputfilename:
    inputfilename = inputfilename + '.txt'
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
counter_leave = 0
# 遇到{ +1  遇到} -1
# counter_leave = 1 时 为id
# counter_leave = 2 且name = 时为名字
class FocusClass:
    id = ''
    relativeid = ''
    context = ''
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
    elif focusnum >0:
        focuslist.append(line)
        if counter_leave == 2 and '}' in line:
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
# print(relativelist[56])

# 统计结束，下面是排序
tempidlist = idlist
idkeylist = [0]*len(tempidlist)
tot = 0

while(1):

    # 对id进行赋值
    for id in tempidlist:
        if relativelist[tempidlist.index(id)] == '':
            continue
        else:
            idkeylist[tempidlist.index(id)] = idkeylist[tempidlist.index(relativelist[tempidlist.index(id)])] + 1
    totlast = tot
    tot = sum(idkeylist)
    delat = tot - totlast
    if delat < 1:
        break
# print(max(idkeylist))
tempidkeylist = idkeylist
for i in range(1, len(tempidkeylist)):
    for j in range(0, len(tempidkeylist)-i):
        # 判定条件
        if tempidkeylist[j] > tempidkeylist[j + 1]:
            tempidkeylist[j], tempidkeylist[j + 1] = tempidkeylist[j + 1], tempidkeylist[j]
            idlist[j], idlist[j + 1] = idlist[j + 1], idlist[j]
            fullfocuslist[j], fullfocuslist[j + 1] = fullfocuslist[j + 1], fullfocuslist[j]
# 输出
f = open(outputpath + inputfilename, 'w', encoding='utf-8')
for focuscon in fullfocuslist:

    f.write('\n'.join(focuscon))
    f.write('\n')
f.close()

