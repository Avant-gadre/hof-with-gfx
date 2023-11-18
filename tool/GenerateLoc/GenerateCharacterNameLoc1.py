import re

# 打开文件并读取内容
path = ".//text.txt"
path1 = ".//text1.txt"


with open(path, 'r') as file:
    content = file.read()

# 定义正则表达式模式，匹配以大写字母组合开头的任意段落
pattern = r'([A-Z]++[A-Z]+[A-Z](?:_[A-Za-z]+)+): "(\w+)"'

# 匹配模式并进行替换
def replace_function(match):
    original = match.group(1)
    word = match.group(2)
    words = word.split('_')
    replacement = f'{original}: "{ " ".join(words[1:]) }"'
    return replacement

modified_content = re.sub(pattern, replace_function, content)

# 将替换后的内容写回文件
with open(path1, 'w') as file:
    file.write(modified_content)