import pandas as pd
import warnings

def extract_data(index_str, save_dir="data/"):

    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

    full_file_dir = "data/raw_data/" + index_str + ".xlsx"
    df = pd.read_excel(full_file_dir, engine="openpyxl")


    columns_needed = ["日期Date", "开盘Open", "最高High", "最低Low", "收盘Close"]
    df_selected = df[columns_needed]
    df_selected.columns = ["Date", "Open", "High", "Low", "Close"]

    csv_filename = index_str + '.csv'

    df_selected.to_csv(save_dir + csv_filename, index=False, encoding="utf-8-sig")

    print(f"Data {index_str} has been extracted.")