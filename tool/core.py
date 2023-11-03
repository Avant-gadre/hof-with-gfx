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


# print(path1)
