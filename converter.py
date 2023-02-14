import os
from PIL import Image


def convert(file):
    open_path = f'./icons/{file}'
    icon = Image.open(open_path)

    new_file_name = file[:-3] + 'ico'
    # change the number if the format is not 3,
    save_path = f'./converted/{new_file_name}'
    icon.save(save_path, format='ICO')


dir_list = os.listdir('./icons')
for png in dir_list:
    convert(png)

# USAGE
# Put any image you want to convert in the icons folder, make sure to check the format letters count
# Run the program!
# incase it shows error, use bash cmd to remove that file!
