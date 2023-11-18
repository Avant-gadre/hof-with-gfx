import os.path
import re

import core

# 用于将character直接注册到history文件（待测试
class TagBlock:
    def __init__(self, id, context):
        self.id = id
        self.context = context

input_path1 = core.characterpath
input_path2 = core.historyeffects
# print(input_path1)
# print(input_path2)
# output_path =
# 存储character 然后检索对应的history文件
charFiles = core.getTxtName(input_path1)
# print(charFiles)
charDict = set()
for file in charFiles:
    filepath = os.path.join(input_path1,file)
    try:
        with open(filepath,'r+',encoding='utf-8') as f1:
            # print(file)
            context = f1.readlines()
            for line in context:
                if re.search('^\t[a-zA-z-Z].*=\s.?{', line):
                    charName = line.strip().split('=')[0].strip().split('#')[0].strip()
                    if charName != '':
                        charDict.add(charName)
    except:
        print(file)
# print(charDict)
charList = list(charDict)
tagDict = set()
# print(charList)
for char in charList:
    tag = char.strip().split('_')[0].upper()
    tagDict.add(tag)
# print(charList)

taglist = list(tagDict)
tagclist = []
for tagc in range(len(taglist)):
    temp = []
    tagclist.append(temp)
for char in charList:
    tag = char.strip().split('_')[0].upper()
    tagclist[taglist.index(tag)].append(char)
    # print(taglist.index(tag),tag,char)
# for tag in taglist:
#     for char in charList:
# for tag in taglist:
# for i in tagclist:
#     print(i)
# print(taglist)

class historyBlock:
    def __init__(self, id, context,ideas):
        self.tag = tag
        self.context = context
        self.context = ideas

hisFiles = core.getTxtName(input_path2)
for his in hisFiles:
    hispath = os.path.join(input_path2, his)
    try:
        with open(hispath,'r+',encoding='utf-8') as f2:
            # print(file)
            context2 = f2.readlines()
            count = 0
            idea = []
            for line in context2:
                if re.search('add_ideas.*= ?[a-zA-Z]'):
                    idea.append(line.strip().split('=')[1].strip().split('#')[0])
                    line = ''
                if re.search('add_ideas.*=.*{',line):
                    count = 1
                    line = ''
                elif count == 1 and '}' in line:
                    count = 0
                    line = ''
                elif count == 1:
                    idea.append(line.strip().split('#')[0].strip())
                    line = ''




    except:
        print(his)
    #
    # 重写为其他-character-idea 顺序