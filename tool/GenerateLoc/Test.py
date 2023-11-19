path = ".//text.txt"
path1 = ".//text1.txt"
path2 = ".//text2.txt"
path3 = ".//text3.txt"
path4 = ".//text4.txt"

with open(path1,'r') as file:
    lines = file.readlines()

# with open(path2, 'w') as file:
#     for line in lines:
#         if 'desc' in line.lower() or not line[:3].isupper():  # 忽略大小写检查是否包含'desc'
#             file.write('\n')  # 如果包含'desc'，写入空行
#         else:
#             file.write(line)  # 否则写入原始行内容

# with open(path2,'r') as file:
#     lines = file.readlines()

with open(path2, 'w') as file:

    for line in lines:
        line1 = line.strip()
        name0 = line1[4:].replace("_", " ").title()
        full = line1+":"+" "+"\""+name0+"\""
        full.strip()
        file.write(full+"\n")