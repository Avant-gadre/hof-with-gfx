import os

format1 = """
music = {{
    name = \"{}\"
    file = \"{}.ogg\"
    volume = 0.9
}}
"""

format2 = """
music = {{
    song = "{}"
    chance = {{
        factor = 1
        modifier = {{
            factor = 3
            always = no
        }}
    }}
}}
"""


def process_ogg_files(folder_path):
    # 获取当前文件夹中所有的ogg文件
    ogg_files = [file for file in os.listdir(folder_path) if file.endswith(".ogg")]

    for ogg_file in ogg_files:
        # 生成对应的文件夹名
        folder_name = ogg_file.replace(".ogg", "")

        # 生成对应的内容并写入文件夹名.asset文件
        asset_file_path = os.path.join(folder_path, f"{folder_name}.asset")
        with open(asset_file_path, "w") as asset_file:
            asset_file.write(format1.format(folder_name, folder_name))

        # 生成对应的内容并写入文件夹名.txt文件
        txt_file_path = os.path.join(folder_path, f"{folder_name}.txt")
        with open(txt_file_path, "w") as txt_file:
            txt_file.write(format2.format(folder_name))


if __name__ == "__main__":
    current_folder = os.getcwd()
    process_ogg_files(current_folder)
