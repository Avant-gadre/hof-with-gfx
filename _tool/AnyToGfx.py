import os

dir0 = "d:\\Documents\\GitHub\\Test\\gfx\\leaders\\CHI"
dir1 = "d:\\Documents\\GitHub\\Test\\gfx\\interface\\advisor\\CHI"
def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if any(filename.endswith(ext) for ext in ('.png', '.tga', '.dds')):
            # Split the filename into parts using underscores
            parts = filename[:-4].split('_')
            
            # Capitalize the first letter of each part
            parts = [parts[0], parts[1].lower()] + [part.lower() for part in parts[3:]]
            # Create the new filename
            new_filename = '_'.join(parts) + '.png'
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


#if __name__ == "__main__":
    #directory = dir1
    #rename_files_in_directory(directory)

    import os

def batch_rename_to_lowercase(directory):
    # 获取目录中的所有文件名
    file_list = os.listdir(directory)

    # 遍历文件列表
    for filename in file_list:
        # 构建旧路径和新路径
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, filename.lower())

        # 将文件名改为小写
        os.rename(old_path, new_path)
        print(f'Renamed: {old_path} to {new_path}')

# 指定目录路径


# 调用函数进行批量文件名改为小写
batch_rename_to_lowercase(dir1)