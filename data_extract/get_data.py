import os

from .extract_data import extract_data
from .get_np_array_data import get_np_array_data

def get_single_data(index_str):
    full_csv_dir = "data/" + index_str + ".csv"
    if not os.path.exists(full_csv_dir):
        extract_data(index_str)
    data = get_np_array_data(index_str)
    return data

def get_data():
    csi_300_data = get_single_data("000300")
    csi_a500_data = get_single_data("000510")
    star_data = get_single_data("000680")
    csi_dividend_data = get_single_data("000922")
    return csi_300_data, csi_a500_data, star_data, csi_dividend_data