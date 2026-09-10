import numpy as np

def cal_ma(date_length, data):
    max_length = data.shape[0]
    if date_length > max_length:
        raise ValueError("Input date length is longer than the maximum length of data!")
    ma_data = np.zeros((max_length, 1))
    count = 0
    average = 0.0
    left_index = 0
    for i in range(max_length):
        if count < date_length:
            average = count / (count + 1) * average + data[i] / (count + 1)
            count += 1
        else:
            average = average - data[left_index] / count + data[i] / count
            left_index += 1
        ma_data[i] = average
    return ma_data

