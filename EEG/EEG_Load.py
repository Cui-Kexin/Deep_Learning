import mne
import numpy as np
import os


def read_edf_data(folder_path):  # 加载edf文件，并将其转换为NumPy数组
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

    return all_data_array


def read_edf_label(file_path):  # 加载edf标签，并将其转换为Numpy数组

    all_label_array = []
    with open(file_path, 'r') as file:
        for line in file:
            all_label_array.append(line.strip())

    return all_label_array()


def load_eeg(folder_path_data, file_path_label):
    # 划分训练集和测试集
    all_data_array = read_edf_data(folder_path_data)
    all_label_array = read_edf_label(file_path_label)
    x_train, t_train = all_data_array[:1614], all_label_array(1614)  # 将前1614个样本作为训练集
    x_test, t_test = all_data_array[1614:], all_label_array(len(all_data_array) - 1614)  # 将剩余样本作为测试集

    return (x_train, t_train), (x_test, t_test)
