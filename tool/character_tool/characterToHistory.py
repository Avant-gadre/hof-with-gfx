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
outpath = os.path.join(core.rootpath, 'tool','countries-histroy')
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


class historyBlock:
    def __init__(self, tag, context,advisors,character):
        self.tag = tag
        self.context = context
        self.advisors = advisors
        self.character = character

hisFiles = core.getTxtName(input_path2)
for his in hisFiles:
    hispath = os.path.join(input_path2, his)
    outfile = os.path.join(outpath,his)
    # print(outfile)
    tag = his[:3]
    try:
        with open(hispath,'r+',encoding='utf-8') as f2:
            # print(file)
            context2 = f2.readlines()
            count = 0
            advisors = []
            for line in context2:
                if re.search('activate_advisor.*= ?[a-zA-Z]',line):
                    advisors.append(line)
                    context2[context2.index(line)] = ''
                    # print(line)
                if 'recruit_character' in line:
                    context2[context2.index(line)] = ''
        characters = []
        for subtag in taglist:
            if tag == subtag:
                characters = tagclist[taglist.index(subtag)]
        tempblock = historyBlock(tag, context2, advisors,characters)

        with open(outfile,'w',encoding='utf-8') as f3:
            f3.writelines(tempblock.context)
            f3.write('####character start\n')
            for line in tempblock.character:
                f3.write('recruit_character = ' + line + '\n')
            f3.write('####character end\n')
            if len(tempblock.advisors) >0 :
                f3.write('####active advisor start\n')
                f3.writelines(tempblock.advisors)
                f3.write('####active advisor end\n')
    except:
        print('character error')

