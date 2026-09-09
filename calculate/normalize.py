def normalize(data):
    close_data = data[:, 3]
    min_val = close_data.min()
    max_val = close_data.max()
    norm_data = (close_data - min_val) / (max_val - min_val)
    return norm_data
