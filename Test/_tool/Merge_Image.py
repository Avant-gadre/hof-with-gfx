from PIL import Image
import os

# 获取当前脚本所在的文件夹路径
current_dir = os.path.dirname(__file__)

# 读取当前文件夹下所有的PNG文件
png_files = [os.path.join(current_dir, file) for file in os.listdir(current_dir) if file.endswith('.png')]

# 按照文件名的首字母进行排序
png_files.sort()

# 计算合并后图片的行数和列数
num_rows = (len(png_files) + 9) // 10
num_cols = min(len(png_files), 10)

# 计算合并后图片的尺寸
img_width = 156
img_height = 210
margin = 10  # 设置图片之间的间距
result_width = num_cols * (img_width + margin)
result_height = num_rows * (img_height + margin)

# 创建一个空白的合并后图片
result = Image.new('RGBA', (result_width, result_height), (255, 255, 255, 255))

# 将所有图片合并到一张图片上
x_offset = 0
y_offset = 0
for i, png_file in enumerate(png_files):
    # 打开当前图片
    img = Image.open(png_file)
    
    # 计算当前图片应该放置的位置
    row = i // 10
    col = i % 10
    x_offset = col * (img_width + margin)
    y_offset = row * (img_height + margin)
    
    # 如果计算的位置超出了合并后图片的范围，则中止合并过程
    if x_offset + img_width > result_width or y_offset + img_height > result_height:
        print("错误：图片太多，无法完全合并到一张图片中。")
        break
    
    # 将当前图片粘贴到合并后图片上
    result.paste(img, (x_offset, y_offset))
    
    # 关闭当前图片
    img.close()

# 保存合并后的图片
result.save(os.path.join(current_dir, 'merged_image.png'))
