path = ".//text.txt"
path1 = ".//text1.txt"
path2 = ".//text2.txt"
path3 = ".//text3.txt"
path4 = ".//text4.txt"

target = "Generic_trait_"

with open(path1, "r") as file:
    lines = file.readlines()

with open(path2, "w") as file:
    for line in lines:
        # parts = line.split(":")  # 以冒号分割行内容
        # prefix = parts[0]  # 获取冒号前部分
        prefix = line
        prefix = prefix.strip()
        name0 = prefix[len(target) :].replace("_", " ").title().strip()
        full = " " + prefix + ":" + " " + '"' + name0 + '"'
        file.write(full + "\n")
