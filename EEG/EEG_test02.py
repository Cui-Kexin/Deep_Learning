import mne
import numpy as np
import os

# 定义EDF文件所在文件夹的路径
folder_path = 'E:/Data/EEG_Data2'

# 获取文件夹中的所有EDF文件
edf_files = [file for file in os.listdir(folder_path) if file.endswith('.edf')]

# 创建一个空列表来存储所有EDF文件的数据
all_data = []

# 循环读取每个EDF文件
for edf_file in edf_files:
    # 构建EDF文件的完整路径
    edf_path = os.path.join(folder_path, edf_file)

    # 读取EDF文件
    raw = mne.io.read_raw_edf(edf_path)

    # 获取数据的采样频率
    sfreq = raw.info['sfreq']

    # 计算每秒的样本数
    samples_per_sec = int(sfreq)

    # 提取所有数据
    data_array = raw.get_data()

    # 分割数组并将每个数组展平成一维数组
    split_data = np.split(data_array, data_array.shape[1] // samples_per_sec, axis=1)
    flat_data = [np.reshape(arr, -1) for arr in split_data]

    # 将当前EDF文件的数据添加到all_data列表中
    all_data.extend(flat_data)

# 将all_data转换为NumPy数组
all_data_array = np.array(all_data)

# 打印数据的形状
print(f"所有EDF文件的数据形状: {all_data_array.shape}")
