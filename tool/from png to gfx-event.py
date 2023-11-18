import re
import os
import io
import os.path
import core
# 路径识别


# 需要的输入：
# 路径 TAG

# TAG = input('请输入TAG：').upper()
class eventPngBlock():
    def __init__(self, name, tag):
        self.name = name
        self.tag = tag

def getPngName(tagpath):
    taglist = os.listdir(tagpath)
    # 列出所有的文件名
    return taglist

def outputReport(eventslist):
    global interfacePath
    pngpath = 'gfx/event_pictures'
    txtfile = open(interfacePath + 'eventFate.gfx' , 'w',encoding='UTF-8')
    # spriteTypes = {
    txtfile.write('spriteTypes = {\n')
    for event in eventslist:
        txt = event.name
        tag = event.tag
        txt = re.sub('.png','',txt).strip()
        pngfullname = '\t\ttexturefile = \"'+pngpath+'/'+ tag +'/'+txt+'.png\"\n'
        pngfullgfxname = '\t\tname = \"GFX_'+txt + '\"\n'
        txtfile.write('\tSpriteType = {\n')
        txtfile.write(pngfullgfxname)
        txtfile.write(pngfullname)
        txtfile.write('\t}\n')
    txtfile.write('}\n')
    txtfile.close()
    print("report event.gfx文件已输出")

pngnames = []
tagnames = []
pngpathfirst = '..\gfx\event_pictures\\'
pngpathlist = core.getDir(pngpathfirst)
print(pngpathlist)
num = 0
for path in pngpathlist:
    pathtemp = os.path.join(pngpathfirst,path)
    temp = getPngName(pathtemp)
    # print(path,'事件图共有', len(temp), '个')
    num += len(temp)
    for name in temp:
        tempevent = eventPngBlock(name,path)
        tagnames.append(tempevent)

# print(tagnames[1].name,tagnames[1].tag)
reportfile = 'eventFate.gfx'
# reportnamelist = []
print('事件图共有',num,'个')
input('type any')
interfacePath = '..\interface\\'
if not os.path.exists(interfacePath):
    os.makedirs(interfacePath)
outputReport(tagnames)


