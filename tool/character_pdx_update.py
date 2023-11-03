import re
import os
import io
import os.path

inputpath = '..\characters\input\\'
outputpath = '.\characters\output\\'
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
counter_leave = 0
# 遇到{ +1  遇到} -1
# counter_leave = 1 时 为id
# counter_leave = 2 且name = 时为名字
# 分类方式
catelist1 = ['country_leader','field_marshal','field_marshal','corps_commander','navy_leader']
catelist2 = ['army_chief','navy_chief','air_chief','theorist','high_command','political_advisor']
catelist0 = []
catelist0.extend(catelist1)
catelist0.extend(catelist2)

# print(catelist0)