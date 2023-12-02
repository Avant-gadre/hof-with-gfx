import re
import os
import io
import os.path


# 根据文件夹，获得其中所有文件的文件名
def getDir(path):
    taglist = []
    taglist1 = os.listdir(path)
    for tag in taglist1:
        path1 = path + tag
        if os.path.isdir(path1):
            taglist.append(tag)
    return taglist


def getTxtName(path):
    # 获取指定路径内所有txt文件名
    list0 = os.listdir(path)
    listout = []
    for name in list0:
        if '.txt' in name:
            listout.append(name)
    return listout


# print(path1)

class focusBlock:
    def __init__(self, id, relativeid, context):
        self.id = id
        self.relativeid = relativeid
        self.context = context

class eventBlock:
    def __init__(self, id, trigger, context):
        self.id = id
        self.trigger = trigger
        self.context = context


rootpath = os.path.abspath(os.path.join(os.getcwd(), "../.."))
focuspath = os.path.join(rootpath, 'common','national_focus','')
decisionspath = os.path.join(rootpath, 'common','decisions','')
eventpath = os.path.join(rootpath, 'events','')
on_actionspath = os.path.join(rootpath, 'common','on_actions','')
scripted_effects = os.path.join(rootpath, 'common','scripted_effects','')
historyeffects = os.path.join(rootpath, 'history','countries','')

# print(focuspath,decisoinpath,eventpath)