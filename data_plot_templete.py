import matplotlib.pyplot as plt

import data_extract
import calculate

# CSI 300 Index, CSI A500 Index, STAR Composite Index, CSI Dividend Index
csi_300_data, csi_a500_data, star_data, csi_dividend_data = data_extract.get_data()  # open high low close, 1455 * 4

csi_dividend_ma120 = calculate.cal_ma(120, csi_dividend_data[:, 3])

plt.figure()
plt.plot(csi_dividend_data[:, 3], color='red', linewidth=1)
plt.plot(csi_dividend_ma120, color='blue', linewidth=1)
plt.title("CSI DIVIDEND MA120 DATA")
plt.xlabel("data")
plt.ylabel("val")
plt.xlim(0, csi_dividend_ma120.shape[0])
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

csi_300_norm = calculate.normalize(csi_300_data[:, 3])
csi_a500_norm = calculate.normalize(csi_a500_data[:, 3])
star_norm = calculate.normalize(star_data[:, 3])
csi_dividend_norm = calculate.normalize(csi_dividend_data[:, 3])

plt.figure()
plt.plot(csi_300_norm, color='red', linewidth=1, label="csi_300")
plt.plot(csi_a500_norm, color='blue', linewidth=1, label="csi_a500")
plt.plot(star_norm, color='green', linewidth=1, label="star")
plt.plot(csi_dividend_norm, color='cyan', linewidth=1, label="csi_div")
plt.title("NORM DATA")
plt.xlabel("data")
plt.ylabel("val")
plt.xlim(0, csi_300_norm.shape[0])
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='best')
plt.tight_layout()
plt.show()

