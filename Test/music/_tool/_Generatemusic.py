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

suffix_to_remove = ".ogg"

def process_ogg_files(script_folder):
    # 获取当前文件夹中所有的ogg文件
    ogg_files = [file for file in os.listdir(script_folder) if file.endswith('.ogg')] # 获取所有.ogg文件
    ogg_files_without_suffix = [os.path.splitext(ogg_file)[0] for ogg_file in ogg_files]

    ogg_files_without_suffix = [
        ogg_file.rstrip(suffix_to_remove) for ogg_file in ogg_files_without_suffix
    ]

    # 更新变量赋值顺序，确保在之前就赋值
    ogg_files = ogg_files_without_suffix

    # 获取当前文件夹的名字
    folder_name = os.path.basename(script_folder)

    # 打开输出文件
    format1_output_path = os.path.join(script_folder, f"_{folder_name}.asset")
    format2_output_path = os.path.join(script_folder, f"_{folder_name}.txt")
    format3_output_path = os.path.join(script_folder, f"_{folder_name}_l_english.yml")

    with open(format1_output_path, "w", encoding="utf-8") as format1_output_file, open(
        format2_output_path, "w", encoding="utf-8"
    ) as format2_output_file, open(
        format3_output_path, "w", encoding="utf-8"
    ) as format3_output_file:
        # 处理每个ogg文件
        for ogg_file in ogg_files:
            ogg_key = ogg_file.replace("(", "_").replace("'","_").replace(")","")

            # 生成对应的内容并写入output_format1.txt文件
            format1_output = format1.format(ogg_key, ogg_file)
            format1_output_file.write(format1_output)
            format1_output_file.write("\n")

            # 生成对应的内容并写入output_format2.txt文件
            format2_output = format2.format(ogg_key)
            format2_output_file.write(format2_output)
            format2_output_file.write("\n")

            modified3 = ogg_file.replace("_", " ")
            format3_output = ogg_key + ":" + " " + '"' + modified3 + '"'
            format3_output_file.write(format3_output)
            format3_output_file.write("\n")


if __name__ == "__main__":
    script_folder = os.path.dirname(os.path.abspath(__file__))
    process_ogg_files(script_folder)
