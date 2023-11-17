import os.path
import re

import core

# 用于将character直接注册到history文件（待测试

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
                if re.search('^\t.*=\s.?{', line):
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
    tag = char.strip().split('_')[0]
    tagDict.add(tag)
taglist = list(tagDict)

class TagBlock:
    def __init__(self, id, context):
        self.id = id
        self.context = context

