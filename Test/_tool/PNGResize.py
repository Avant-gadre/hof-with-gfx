from PIL import Image
import os

def compress_images(input_folder, output_folder, quality=85):
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # 遍历当前文件夹中的所有PNG文件
    for filename in os.listdir(script_dir):
        if filename.endswith(".png"):
            input_file_path = os.path.join(script_dir, filename)
            output_file_path = os.path.join(script_dir, output_folder, filename)

            # 打开图像文件
            img = Image.open(input_file_path)

            # 确保输出文件夹存在
            output_folder_path = os.path.join(script_dir, output_folder)
            if not os.path.exists(output_folder_path):
                os.makedirs(output_folder_path)

            # 保存图像时进行压缩
            img.save(output_file_path, "PNG", quality=quality)

if __name__ == "__main__":
    input_folder = "."  # 当前文件夹
    output_folder = "output_folder"  # 替换为保存压缩后图片的文件夹相对路径
    target_quality = 50  # 替换为目标压缩质量，通常在0-100之间，值越小文件越小

    # 调用函数进行批量压缩
    compress_images(input_folder, output_folder, quality=target_quality)
