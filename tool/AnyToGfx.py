import os

dir0 = "d:\\Documents\\GitHub\\Test\\gfx\\leaders\\CHI"
dir1 = "d:\\Documents\\GitHub\\Test\\gfx\\interface\\advisor\\CHI"
def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if any(filename.endswith(ext) for ext in ('.png', '.tga', '.dds')):
            # Split the filename into parts using underscores
            parts = filename[:-4].split('_')
            
            # Capitalize the first letter of each part
            parts = [parts[0], parts[1].upper()] + [part.capitalize() for part in parts[3:]]
            
            parts[0] = 'CHI'
            # Create the new filename
            new_filename = '_'.join(parts) + '.png'
            
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


if __name__ == "__main__":
    directory = dir1
    rename_files_in_directory(directory)