import re
import os
import io
import os.path

# 路径识别


# 需要的输入：
# 路径 TAG
# TAG = input('请输入TAG：').upper()

def getDir(path):
    taglist = []
    taglist1 = os.listdir(path)
    for tag in taglist1:
        path1 = path + tag
        if os.path.isdir(path1):
            taglist.append(tag)
    return taglist

def getPngName(tagpath):
    taglist = os.listdir(tagpath)
    return taglist

def outpuGfx(text):
    global interfacePath
    global TAG
    pngpath = 'gfx/interface/companies/' + TAG
    txtfile = open(interfacePath + 'idea_'+ TAG + '.gfx' , 'w',encoding='UTF-8')
    # spriteTypes = {
    txtfile.write('spriteTypes = {\n')
    for txt in text:
        txt = re.sub('.png','',txt).strip()
        pngfullname = '\t\ttexturefile = \"'+pngpath+'/'+txt+'.png\"\n'
        # pngfullgfxname = '\t\tname = \"GFX_'+txt + '\"\n'
        pngfullgfxname = '\t\tname = GFX_' + txt + '\n'
        txtfile.write('\tSpriteType = {\n')
        txtfile.write(pngfullgfxname)
        txtfile.write(pngfullname)
        txtfile.write('\t}\n')
    txtfile.write('}\n')
    txtfile.close()
    print(TAG,"idea.gfx文件已输出")

pngpathfirst = '..\gfx\interface\companies\\'
taglist = getDir(pngpathfirst)
print('将生成以下tag民族精神的gfx文件')
print(taglist)
input('')

interfacePath = '..\interface\companies\\'

if not os.path.exists(interfacePath):
    os.makedirs(interfacePath)

for TAG in taglist:
    pngpath = pngpathfirst + TAG
    gfxfilename = interfacePath + 'idea_' + TAG + '.gfx'
    pnglist = getPngName(pngpath)
    outpuGfx(pnglist)

    # for tag in taglist:
    #     print(tag)
    print(TAG,'共有',len(pnglist),'个图标')
# input('')
