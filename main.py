import data_extract

# CSI 300 Index, CSI A500 Index, STAR Composite Index, CSI Dividend Index
csi_300_data, csi_a500_data, star_data, csi_dividend_data = data_extract.get_data()

print(csi_300_data.shape)
print(csi_a500_data.shape)
print(star_data.shape)
print(csi_dividend_data.shape)
