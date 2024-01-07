import os
import shutil
from PIL import Image

# 获取当前脚本所在文件夹路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 输入和输出文件夹路径
input_folder = script_dir  # Python脚本所在的文件夹路径
output_folder = os.path.join(script_dir, "medium")  # 要保存TGA文件的文件夹路径
output_folder1 = os.path.join(script_dir, "small")  # 要保存TGA文件的文件夹路径

# 清空输出文件夹
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)
os.makedirs(output_folder)

if os.path.exists(output_folder1):
    shutil.rmtree(output_folder1)
os.makedirs(output_folder1)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith(".tga"):
        # 构建TGA文件的完整路径
        tga_file_path = os.path.join(input_folder, filename)

        # 打开TGA图像文件
        tga_image = Image.open(tga_file_path)

        # 调整图像大小为41x26
        resized_image = tga_image.resize((41, 26))
        # 调整图像大小为11x7
        resized_image1 = tga_image.resize((10, 7))

        # 构建输出文件的完整路径
        output_file_path = os.path.join(output_folder, filename)
        output_file_path1 = os.path.join(output_folder1, filename)

        # 保存调整大小后的TGA图像文件到输出文件夹
        resized_image.save(output_file_path)
        resized_image1.save(output_file_path1)

        # 关闭图像文件
        tga_image.close()

print("Done")
