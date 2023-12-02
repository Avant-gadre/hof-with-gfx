with open('text1.txt', 'r') as file:
    lines = file.readlines()  # 逐行读取文件内容

# 修改每行内容并写入同一文件
with open('text2.txt', 'a') as file:
    file.truncate(0)
    for line in lines:
        line.strip()
        parts = line.split(':')  # 以冒号分割行内容
        prefix = parts[0]  # 获取冒号前部分
        suffix = parts[1]  # 获取冒号后部分
        modified_line = f"{prefix}_desc: \"Placeholder\""
        file.write(" "+line)
        file.write(" "+modified_line+"\n"+"\n")



