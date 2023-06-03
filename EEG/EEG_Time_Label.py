import numpy as np
import mne
import os

# 设置日志级别为ERROR，只打印错误消息
mne.set_log_level("ERROR")


def get_file_duration(file_path):
    # 读取EDF文件
    raw = mne.io.read_raw_edf(file_path)

    # 获取数据的总时长（以秒为单位）
    duration_sec = raw.times[-1]

    return duration_sec


def get_folder_file_durations(folder_path):
    file_list = os.listdir(folder_path)
    file_durations = {}

    for filename in file_list:
        file_extension = os.path.splitext(filename)[1]
        if file_extension == '.edf':
            try:
                file_number = int(os.path.splitext(filename)[0])
                file_path = os.path.join(folder_path, filename)
                duration_sec = get_file_duration(file_path)
                file_durations[filename] = duration_sec
            except ValueError:
                continue

    return file_durations


# 指定文件夹路径
folder_path = "E:/Data/EEG_Data2/"  # 替换为实际的文件夹路径

file_durations = get_folder_file_durations(folder_path)

# 输出每个文件的时长
for filename, duration in sorted(file_durations.items(), key=lambda x: int(os.path.splitext(x[0])[0])):
    print(f"{filename}: {duration:.2f} 秒")

# 生成并写入txt文件
output_file = "Label.txt"  # 替换为实际的输出文件路径

with open(output_file, "w") as f:
    for filename, duration in sorted(file_durations.items(), key=lambda x: int(os.path.splitext(x[0])[0])):
        total_seconds = int(duration)
        zero_seconds = min(total_seconds, 120)
        one_seconds = total_seconds - zero_seconds
        f.write("0 " * zero_seconds)
        f.write("1 " * one_seconds)
        f.write("\n")
print(f"已经将标签写入 {output_file} 文件中")
