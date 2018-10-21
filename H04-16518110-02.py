# NIM/Nama  : 16518110/Kendrik Emkel Ginting
# Tanggal   : 21 Oktober 2018
# Deskripsi : PR Data Analisis 2 H04

# Spesifikasi: Menjawab task 02 pada H04

# Kamus
# df = dataframe database
# dmakanan = data penjualan hanya makanan

# Algoritma
import pandas as pd

df = pd.read_csv("stei-c-2.csv")

# 1. Banyaknya data
print(len(df))
# 7923

# 2. Transaksi yang dilakukan oleh Tuan Yon
print(df.loc[df["nama"] == "Tuan Yon"])
#          nama tipe_barang  bulan  tahun  qty  profit
# 543  Tuan Yon  elektronik      4   2017    7   12312

# 3. Banyaknya transaksi dengan profit di atas 150.000
print(len(df.loc[df["profit"] > 150000]))
# 2051

# 4. Banyaknya transaksi dari bulan Oktober 2014 sampai April 2015
print(len(df.loc[(((df["tahun"] == 2014) & ((df["bulan"] == 10) | (df["bulan"] == 11) | (df["bulan"] == 12)) | (df["tahun"] == 2015) & ((df["bulan"] == 1) | (df["bulan"] == 2) | (df["bulan"] == 3) | (df["bulan"] == 4))))]))
# 1157

# 5. Data transaksi makanan dengan profit minimum
dmakanan = df.loc[df["tipe_barang"] == "makanan"]
print(dmakanan[dmakanan["profit"] == dmakanan.min()["profit"]])
#               nama tipe_barang  bulan  tahun  qty  profit
# 6036  Faisal Ardhy     makanan      9   2015    1   10194

# 6. Data 10 transaksi alat makan dengan profit terbesar di tahun 2017
print(((df.loc[(df["tahun"] == 2017) & (df["tipe_barang"] == "alat makan")]).sort_values(["profit"], ascending=[0]))[:10])
#                             nama tipe_barang  bulan  tahun  qty  profit
# 6750       Prayoga Aryandi Putra  alat makan      1   2017   20  199884
# 3255         Fransisco Sihombing  alat makan      1   2017   20  199749
# 5036             Syafitri Syarif  alat makan      7   2017   20  199589
# 6127        Ola Khusnul Khotimah  alat makan      7   2017   20  199433
# 2470      Albert Caesar Pasaribu  alat makan      1   2017   20  197390
# 5642      Aditya Rizki Wicaksono  alat makan      1   2017   20  195588
# 6707  I Gusti Agung Gde Bimayuda  alat makan      1   2017   20  195120
# 158               Hasyim Firdaus  alat makan      1   2017   20  194054
# 289   Nadia Putri Aulia Nasution  alat makan      2   2017   20  191874
# 5350               Martha Monica  alat makan      6   2017   19  189540

# 7. Tabel frekuensi masing-masing tahun
print(df["tahun"].value_counts())
# 2016    2021
# 2015    1999
# 2014    1984
# 2017    1919

# 8. Rata-rata profit di bulan Desember 2016
print((df.loc[(df["bulan"] == 12) & (df["tahun"] == 2016)])["profit"].mean())
# 107476.22543352601

# 9. Standar deviasi dari profit transaksi pakaian
print((df.loc[df["tipe_barang"] == "pakaian"])["profit"].std())
# 53078.68100121805

# 10. Rata-rata dari profit transaksi pakaian sebelum tahun 2016
print((df.loc[(df["tipe_barang"] == "pakaian") & df["tahun"] < 2016])["profit"].mean())
# 104615.84791114477

# 11. Koefisien korelasi dari quantity dengan profit
print(df["qty"].corr(df["profit"]))
# 0.9106504683576545
