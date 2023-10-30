import re
import os
import io
import os.path

inputpath = '..\common\characters\\'
outputpath = '.\characters_name\\'
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
counter_leave = 0
# 遇到{ +1  遇到} -1
# counter_leave = 1 时 为id
# counter_leave = 2 且name = 时为名字

def getDir(path):
    # 获取所有character人名文件 按tag读取
    taglist = []
    taglist1 = os.listdir(path)
    for tag in taglist1:
        path1 = path + tag
        if os.path.isfile(path1) and '.txt' in tag :
            taglist.append(tag)
    return taglist


f = open(outputpath + 'temp.txt','w', encoding='utf-8')
f.close()
taglist = getDir(inputpath)
for tagfile in taglist:

    tagpath = inputpath + tagfile
    counter_leave = 0
    # 读取每个文件的文本 弄成array
    # 逐行读取
    tag = tagfile.strip().replace('.txt','').strip()
    tag = re.sub(r'[0-9]+','',tag).strip().replace('_Fate_Characters','').strip()
    idlist = []
    namelist = []
    f = open(tagpath,'r', encoding='utf-8')
    # print(tagpath)
    lines = f.readlines()


    for line in lines:
        if counter_leave == 1 and '=' in line:
            # 是id
            id = line.strip().replace('=','').replace('{','').strip()
            id = re.sub(r'#.*','',id)
            idlist.append(id)

        elif counter_leave == 2 and 'name' in line:
            # 是名字
            name = line.strip().replace('=','').replace('name','').strip()
            name = re.sub(r'#.*', '', name)
            namelist.append(name)

        # 计算 counter_leave
        counter_leave += line.count('{')
        counter_leave -= line.count('}')

    f.close()
    blockcode = '\n' + '#' + tag + '\n'
    print(blockcode + '\n')
    for name in namelist:
        if '_' not in name:
            print(name)
    f = open(outputpath + 'temp.txt', 'a+', encoding='utf-8')
    f.write(blockcode)
    for name in namelist:
        if '_' not in name:
            # 此处是需要本地化的文件名字
            id = idlist[namelist.index(name)]
            outline = ' ' + id + ':0 ' + name + '\n'
            f.write(outline)
    # break
    # break
        # print(taglist)
# print(path1)