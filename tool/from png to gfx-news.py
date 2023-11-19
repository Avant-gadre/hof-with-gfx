import re
import os
import io
import os.path
import core
# 路径识别


# 需要的输入：
# 路径 TAG

# TAG = input('请输入TAG：').upper()
def getPngName(tagpath):
    taglist = os.listdir(tagpath)
    # 列出所有的文件名
    return taglist


def outputNews(text):
    global interfacePath
    global TAG
    pngpath = 'gfx/event_pictures_news'
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
pngpathfirst = '..\gfx\\event_pictures_news\\'
newsnamelist = getPngName(pngpathfirst)


newsfile = 'eventnewsFate.gfx'


print('新闻图共有',len(newsnamelist),'个')
input('type any')
interfacePath = '..\interface\\'
if not os.path.exists(interfacePath):
    os.makedirs(interfacePath)

outputNews(newsnamelist)

