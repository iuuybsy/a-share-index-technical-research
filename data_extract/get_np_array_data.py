import numpy as np
import pandas as pd

def get_np_array_data(index_str):
    full_dir = "data/" + index_str + ".csv"
    df = pd.read_csv(full_dir)

    data = df[['Open', 'High', 'Low', 'Close']].to_numpy(dtype=np.float64)
    return data