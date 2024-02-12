import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 要读取的文件名
file_name1 = "text1.txt"  # 替换为你的文件名

file_name2 = "text2.txt"  # 替换为你的文件名

# 文件路径
file_path1 = os.path.join(current_dir, file_name1)

file_path2 = os.path.join(current_dir, file_name2)

target = "POL_trait_"

end = "_idea"

with open(file_path1, "r", errors="ignore") as file:
    lines = file.readlines()

lines.sort()

# ... （之前的代码）

with open(file_path2, "w", errors="ignore") as file:
    # file.truncate(0)  # 这里可能不需要清空文件内容
    for line in lines:
        line = line.strip()  # 修复了这里的逻辑错误
        modified_line = line.split(":", 1)[0]
        prefix = modified_line.strip()
        # if prefix.startswith(target):
        if prefix.endswith(end):
            name0 = (
                (prefix[len(target) :])[: -len(end)].replace("_", " ").title().strip()
            )
        else:
            name0 = (prefix[len(target) :]).replace("_", " ").title().strip()

        full = " " + prefix + ":" + " " + '"' + name0 + '"'
        full1 = " " + prefix + "_desc" + ":" + " " + '"' + name0 + '"'
        file.write(full + "\n")
        #file.write(full1 + "\n")

# ... （之后的代码）
