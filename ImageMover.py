import os
import shutil

# specify origion path
root_path = r'E:\BaiduNetdiskDownload\Marugaogaski'

# find all folder
for folder_name in os.listdir(root_path):
    folder_path = os.path.join(root_path, folder_name)

    # move all img in the folder to root path
    for file_name in os.listdir(folder_path):
        new_file_name = folder_name+file_name
        shutil.copyfile(os.path.join(folder_path, file_name), os.path.join(root_path, new_file_name))
    # print(os.path.isdir(folder_path))
    # exit()
