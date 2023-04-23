import re
import csv
import os
import io
import time

currentTime = time.strftime("%Y_%m_%d", time.localtime())
# print(currentTime)
picpath = ''

outfilename = 'eventpic'+currentTime+'.gfx'  # utf-8
outpath = 'E:\MOD\py\\' + outfilename
pngpath = 'gfx/event_pictures/'
print(outfilename)

def outpuGfx(text):
    global outpath
    global pngpath
    txtfile = open(outpath, 'w',encoding='UTF-8')
    txtfile.write('spriteTypes = {\n')
    for txt in text:
        # 读入的name是带有png后缀的 此处先将后缀去掉
        pngfullname = '\t\ttexturefile = \"' + pngpath + txt + '\"\n'
        print(pngfullname)
        txt = txt.replace('.png', '')
        pngfullgfxname = '\t\tname = \"GFX_' + txt + '\"\n'
        print(pngfullgfxname)
        txtfile.write('\tspriteType = {\n')
        txtfile.write(pngfullgfxname)
        txtfile.write(pngfullname)
        txtfile.write('\t}\n')
    txtfile.write('}\n')
    txtfile.close()
    print("eventpic.gfx文件已输出")
def getNameList(pathname):
    filenames = os.listdir(pathname)
    namelist = []
    for filename in filenames:
        if '.png' in filename:
            namelist.append(filename)
    return namelist
# 读取eventpic文件名

pathhead = 'E:/modding/@test event/'
pathname = pathhead+pngpath
pngnames = getNameList(pathname)
# print(pngnames)
outpuGfx(pngnames)
# 输出到gfx文件
