def normalize(data):
    max_val = data.max()
    norm_data = data / max_val
    return norm_data
