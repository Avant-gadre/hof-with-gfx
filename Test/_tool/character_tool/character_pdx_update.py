import re
import os
import io
import os.path
import core

# 用于将pdx的角色进行分类存放
inputpath = core.characterpath
outputpath = '../characters/output/'
if not os.path.exists(inputpath):
    os.makedirs(inputpath)
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
counter_leave = 0
# 遇到{ +1  遇到} -1
# counter_leave = 1 时 为id
# counter_leave = 2 且name = 时为名字
# 分类方式
catelist1 = ['country_leader = {','field_marshal = {','corps_commander = {','navy_leader = {']
catelist2 = ['slot = army_chief','slot = navy_chief','slot = air_chief','slot = theorist','slot = high_command','slot = political_advisor','empty_character']
catelist0 = []
catelist0.extend(catelist1)
catelist0.extend(catelist2)
characterBlock = []
#

txtlist = core.getTxtName(inputpath)

num = 0
for txtname in txtlist:
    # 读入
    txtname = '_Asian.txt'
    charactersCollection = []
    fullname = os.path.join(inputpath,txtname)

    # print(fullname)
    with open(fullname, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
    counter_leave = 0
    # 分块
    for line in lines:
        if counter_leave == 1 and ' = {' in line:
            num += 1
            # 这里是起始位置
            characterBlock = [line]
        elif num > 0 and counter_leave > 1:
            characterBlock.append(line)
            if counter_leave == 2 and '\t}' in line:
                # 这里是结束位置
                charactersCollection.append(characterBlock)
                # print(characterBlock)
        counter_leave += line.count('{')
        counter_leave -= line.count('}')

    # 分类
    charactersReorder = []
    for i in range(11):
        charactersReorder.append([])
    charactersCollectionSave = charactersCollection
    for character in charactersCollection:
        print(character[0])
        catestr = ''.join(character)
        cateid = 10
        for cate in catelist0:
            if cate in catestr:
                # 找到对应的种类了！
                cateid = catelist0.index(cate)
                print(cateid)
                charactersReorder[cateid].extend(character)
                break
        if cateid == 10:
            charactersReorder[10].extend(character)

    # print(charactersReorder[10])
    with open(outputpath + txtname, 'w', encoding='utf-8') as f2:
        f2.write('#' + txtname + '\n')
        for i in range(len(charactersReorder)):
            catename = catelist0[i]
            catename = re.sub(r'= {','',catename).strip()
            catename = re.sub(r'slot =', '', catename).strip()
            catename = '#' + catename + '\n'
            # print(catename)
            f2.write(catename)
            f2.write('characters = {\n')
            f2.write(''.join(charactersReorder[i]))
            f2.write('}\n')

    break


    # 输出


# print(txtlist)
# print(catelist0)