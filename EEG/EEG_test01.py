import numpy as np
import mne
import os

# 读取EDF文件
edf_file = 'E:/Data/EEG_Data2/20230531145421_CuiKeXin1.edf'
raw = mne.io.read_raw_edf(edf_file)

# 提取所有数据
data_array_all = raw.get_data()
print(f"所有数据的数组为：{data_array_all.shape} ")


# 获取数据的采样频率，计算前一秒的样本数，提取前一秒的数据
sfreq = raw.info['sfreq']
print(f"采样频率为 {sfreq} Hz")
# n_samples = int(sfreq)
# data, _ = raw[:, :n_samples]
#
# # 将数据存储为数组
# data_array = data
# print(f"一秒的数组为：{data_array.shape} ")
#
# # 获取数据的总时长（以秒为单位）
# duration_sec = raw.times[-1]
# print(f"EDF文件的时长为 {duration_sec:.2f} 秒")

# 计算每秒的样本数,分割数组,将每个数组展平成一维数组
samples_per_sec = int(sfreq)
split_data = np.split(data_array_all, data_array_all.shape[1] // samples_per_sec, axis=1)
flat_split_data = [np.reshape(arr, -1) for arr in split_data]
print(f"分割后的数组数量: {len(split_data)}")
print(f"第一个数组的形状: {flat_split_data[0].shape}")