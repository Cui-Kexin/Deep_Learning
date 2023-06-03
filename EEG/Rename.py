import os
import re

def rename_files(folder_path):
    file_list = os.listdir(folder_path)
    file_list = [filename for filename in file_list if os.path.isfile(os.path.join(folder_path, filename))]  # 仅保留文件，排除文件夹
    file_list.sort(key=lambda x: int(re.findall(r'\d+', x)[0]) if re.findall(r'\d+', x) else 0)  # 按数字顺序排序

    counter = 1
    for filename in file_list:
        if filename.endswith(".txt") or filename.endswith(".edf"):
            file_extension = os.path.splitext(filename)[1]  # 获取文件扩展名
            new_filename = str(counter) + file_extension
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)
            counter += 1


# 指定要重命名的文件夹路径
Folder_path = "E:/Data/EEG_Data2"  # 替换为实际的文件夹路径
rename_files(Folder_path)