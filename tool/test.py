import re
import os
import io
import os.path

path1 = os.path.dirname(os.path.abspath(__file__))
path2 = '.\gfx\\'
if not os.path.exists(path2):
    print('path2 不存在')
path3 = '..\gfx\\'
if not os.path.exists(path3):
    print('path3 不存在')
else:
    print('path3 存在')

# print(path1)