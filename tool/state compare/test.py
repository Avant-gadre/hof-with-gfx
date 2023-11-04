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

def extract_prefix(file_name):
    return int(file_name.split("-")[0])

# 指定文件夹路径
folder_path1 = './Test1'
folder_path2 = './Test2'

with open("output.txt", "w") as file:
    file.write("")

# 初始化一个空列表来存储文件名
#用前缀进行排序
file_list1 = sorted(getTxtName(folder_path1),key=extract_prefix)
file_list2 = sorted(getTxtName(folder_path2),key=extract_prefix)
##print(file_list1)

##变量
# 读取第一个文件的内容
j = min(len(file_list2),len(file_list1))
rangelist = list(range(0,j))

for num in rangelist:

    filename1 = file_list1[num]
    filename2 = file_list2[num]
    with open(os.path.join(folder_path1, filename1), 'r') as file1:
        content1 = file1.read()

    # 读取第二个文件的内容
    with open(os.path.join(folder_path2, filename2), 'r') as file2:
        content2 = file2.read()

    # 定义属性名称
    property_name = "provinces"

    # 从文件1中提取属性定义
    start_index1 = content1.find(f"{property_name} = {{")
    end_index1 = content1.find("}", start_index1)
    if start_index1 != -1 and end_index1 != -1:
        property_definition1 = content1[start_index1:end_index1 + 1]
    else:
        property_definition1 = ""

    # 从文件2中提取属性定义
    start_index2 = content2.find(f"{property_name} = {{")
    end_index2 = content2.find("}", start_index2)
    if start_index2 != -1 and end_index2 != -1:
        property_definition2 = content2[start_index2:end_index2 + 1]
    else:
        property_definition2 = ""

    # 提取属性定义中的元素
    def extract_elements(property_definition):
        if property_definition:
            elements = property_definition.split("{")[1].split("}")[0].strip().split()
            return set(elements)
        return set()

    # 提取两个属性定义中的元素
    elements1 = extract_elements(property_definition1)
    elements2 = extract_elements(property_definition2)

    # 判断是否有交集
    has_intersection = bool(elements1 & elements2)

    if not has_intersection:
        with open("output.txt", "a",encoding='utf - 8') as file:
            file.write(f'false in' + filename1 + 'and' + filename2 + '\n')
            #file.write('\n'.join(str(item) for item in elements2)+'\n')
            #file.write('\n')
            #file.write('\n'.join(str(item) for item in elements1)+'\n')
