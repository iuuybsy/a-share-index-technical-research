import matplotlib.pyplot as plt
import numpy as np

import data_extract
import calculate

# CSI 300 Index, CSI A500 Index, STAR Composite Index, CSI Dividend Index
csi_300_data, csi_a500_data, star_data, csi_dividend_data = data_extract.get_data()  # open high low close, 1455 * 4

csi_a500_avg = 0.5 * (csi_a500_data[:, 1] + csi_a500_data[:, 2])
csi_a500_norm = calculate.normalize(csi_a500_avg)

cash_ori = 1000.0
cash = cash_ori
invest_num = 100.0
shares = 0.0

buy_threshold = -0.05
buy_gap = 5
sell_threshold = 0.03
sell_gap = 5
ma_ref = 120

sell_ratio = 0.05

csi_a500_norm_ma = calculate.cal_ma(ma_ref, csi_a500_norm)
total_asset = np.zeros(csi_a500_norm.shape[0])
last_buy_index = 0
last_sell_index = 0
for i in range(csi_a500_norm.shape[0]):
    if cash > 1e-8 and csi_a500_norm[i] < csi_a500_norm_ma[i] * (1 + buy_threshold) and i - last_buy_index >= buy_gap:
        invest_cash = min(cash_ori / invest_num, cash)
        shares += invest_cash / csi_a500_norm[i]
        cash -= invest_cash
        last_buy_index = i
    elif csi_a500_norm[i] > csi_a500_norm_ma[i] * (1 + sell_threshold) and i - last_sell_index >= sell_gap:
        cash += shares * sell_ratio * csi_a500_norm[i]
        shares *= 1 - sell_ratio
        last_sell_index = i
    total_asset[i] = (cash + csi_a500_norm[i] * shares) / cash_ori

plt.figure()
plt.plot(csi_a500_norm, color='blue', linewidth=1, label="csi_a500_norm")
plt.plot(csi_a500_norm_ma, color='red', linewidth=1, label="ma")
plt.plot(total_asset, color='green', linewidth=1, label="asset")
plt.title("NORM DATA")
plt.xlabel("data")
plt.ylabel("val")
plt.xlim(0, csi_a500_data.shape[0])
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()
plt.show()


