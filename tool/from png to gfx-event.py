import re
import os
import io
import os.path

# 路径识别


# 需要的输入：
# 路径 TAG

# TAG = input('请输入TAG：').upper()

def getPngName(tagpath):
    taglist = os.listdir(tagpath)
    # 列出所有的文件名
    return taglist
def diffEvent(pngnames):
    global reportnamelist
    global newsnamelist
    for pngname in pngnames:
        if 'report_event_' in pngname:
            reportnamelist.append(pngname)
        elif 'news_event_' in pngname:
            newsnamelist.append(pngname)
    # return taglist
def outputReport(text):
    global interfacePath
    pngpath = 'gfx/event_pictures'
    txtfile = open(interfacePath + 'eventFate.gfx' , 'w',encoding='UTF-8')
    # spriteTypes = {
    txtfile.write('spriteTypes = {\n')
    for txt in text:
        txt = re.sub('.png','',txt).strip()
        pngfullname = '\t\ttexturefile = \"'+pngpath+'/'+txt+'.png\"\n'
        pngfullgfxname = '\t\tname = \"GFX_'+txt + '\"\n'
        txtfile.write('\tSpriteType = {\n')
        txtfile.write(pngfullgfxname)
        txtfile.write(pngfullname)
        txtfile.write('\t}\n')
    txtfile.write('}\n')
    txtfile.close()
    print("report event.gfx文件已输出")
def outputNews(text):
    global interfacePath
    global TAG
    pngpath = 'gfx/event_pictures'
    txtfile = open(interfacePath + 'eventnewsFate.gfx' , 'w',encoding='UTF-8')
    # spriteTypes = {
    txtfile.write('spriteTypes = {\n')
    for txt in text:
        txt = re.sub('.png','',txt).strip()
        pngfullname = '\t\ttexturefile = \"'+pngpath+'/'+txt+'.png\"\n'
        pngfullgfxname = '\t\tname = \"GFX_'+txt + '\"\n'
        txtfile.write('\tSpriteType = {\n')
        txtfile.write(pngfullgfxname)
        txtfile.write(pngfullname)
        txtfile.write('\t}\n')
    txtfile.write('}\n')
    txtfile.close()
    print("news event.gfx文件已输出")
pngpathfirst = '..\gfx\event_pictures\\'
pngnames = getPngName(pngpathfirst)
reportfile = 'eventFate.gfx'
newsfile = 'eventnewsFate.gfx'
reportnamelist = []
newsnamelist = []
diffEvent(pngnames)
print('事件图共有',len(reportnamelist),'个')
print('新闻图共有',len(newsnamelist),'个')
input('type any')
interfacePath = '..\interface\\'
if not os.path.exists(interfacePath):
    os.makedirs(interfacePath)
outputReport(reportnamelist)
outputNews(newsnamelist)

