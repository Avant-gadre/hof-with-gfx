import re
import os
import io
import os.path


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
    pngpath = 'gfx/interface/goals/' + TAG
    txtfile = open(interfacePath +'goal_'+ TAG + '.gfx' , 'w',encoding='UTF-8')
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
    print(TAG,"goal.gfx文件已输出")
def outpuShineGfx(text):
    global interfacePath
    global TAG
    pngpath = 'gfx/interface/goals/' + TAG
    txtfile = open(interfacePath +'goal_'+ TAG + '_shine.gfx', 'w',encoding='UTF-8')
    txtfile.write('spriteTypes = {\n')
    for txt in text:
        txt = re.sub('.png', '', txt).strip()
        pngfullname = '\t\ttexturefile = \"'+pngpath+'/'+txt+'.png\"\n'
        pngfullgfxname = '\t\tname = \"GFX_'+txt +'_shine'+ '\"\n'
        animationfile = '\t\t\tanimationmaskfile = \"'+pngpath+'/'+txt+'.png\"\n'
        txtfile.write('\tSpriteType = {\n')
        txtfile.write(pngfullgfxname)
        txtfile.write(pngfullname)
        txtfile.write('\t\teffectFile = "gfx/FX/buttonstate.lua"\n')

        # 第一段动画代码
        txtfile.write('\t\tanimation = {\n')
        txtfile.write(animationfile)
        txtfile.write('\t\t\tanimationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"\n')
        txtfile.write('\t\t\tanimationrotation = -90.0\n')
        txtfile.write('\t\t\tanimationlooping = no\n')
        txtfile.write('\t\t\tanimationtime = 0.75\n')
        txtfile.write('\t\t\tanimationdelay = 0\n')
        txtfile.write('\t\t\tanimationblendmode = \"add\"\n')
        txtfile.write('\t\t\tanimationtype = \"scrolling\"\n')
        txtfile.write('\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }\n')
        txtfile.write('\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }\n')
        txtfile.write('\t\t}\n')
        # 第二段动画代码
        txtfile.write('\t\tanimation = {\n')
        txtfile.write(animationfile)
        txtfile.write('\t\t\tanimationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"\n')
        txtfile.write('\t\t\tanimationrotation = 90.0\n')
        txtfile.write('\t\t\tanimationlooping = no\n')
        txtfile.write('\t\t\tanimationtime = 0.75\n')
        txtfile.write('\t\t\tanimationdelay = 0\n')
        txtfile.write('\t\t\tanimationblendmode = \"add\"\n')
        txtfile.write('\t\t\tanimationtype = \"scrolling\"\n')
        txtfile.write('\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }\n')
        txtfile.write('\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 }\n')
        txtfile.write('\t\t}\n')

        txtfile.write('\t\tlegacy_lazy_load = no\n')
        txtfile.write('\t}\n')
        txtfile.write('\n')
    txtfile.write('}\n')
    txtfile.close()
    print(TAG,"shine.gfx已输出")


pngpathfirst = '../gfx/interface/goals/'
pngpathtest = 'gfx/interface/goals/'
taglist = getDir(pngpathfirst)
print('将生成以下tag国策的gfx文件')
print(taglist)
input('按回车继续')
interfacePath = '..\interface\goals\\'
if not os.path.exists(interfacePath):
    os.makedirs(interfacePath)
    print('1')

testfile = open(interfacePath +'_goal.gfx', 'w',encoding='UTF-8')
testfile.write('####测试用\n')
testfile.write('spriteTypes = {\n')

for TAG in taglist:
    pngpath = pngpathfirst + TAG
    pngpath2 = pngpathtest + TAG
    pnglist = getPngName(pngpath)
    for txt in pnglist:
        txt = re.sub('.png','',txt).strip()
        pngfullname = '\t\ttexturefile = \"'+pngpath2+'/'+txt+'.png\"\n'
        pngfullgfxname = '\t\tname = \"GFX_'+txt + '\"\n'
        testfile.write('\tSpriteType = {\n')
        testfile.write(pngfullgfxname)
        testfile.write(pngfullname)
        testfile.write('\t}\n')
    outpuGfx(pnglist)
    outpuShineGfx(pnglist)
    print(TAG, '共有', len(pnglist), '个图标')
testfile.write('}\n')
testfile.close()
# for a in alist:
#     taglist = getPngName(pngpath)
#     outpuGfx(taglist)
#     outpuShineGfx(taglist)
#     # for tag in taglist:
#     #     print(tag)
#     print(TAG,'共有',len(taglist),'个图标')

