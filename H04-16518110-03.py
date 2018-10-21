
# coding: utf-8

# In[1]:


# NIM/Nama  : 16518110/Kendrik Emkel Ginting
# Tanggal   : 21 Oktober 2018
# Deskripsi : PR Data Analisis 3 H04

# Spesifikasi: Menjawab task 03 pada H04

# Kamus
# df = dataframe database
# dmakanan = data penjualan hanya makanan

# Algoritma
import pandas as pd


# In[2]:


df = pd.read_csv("stei-c-3.csv")
print(df)


# In[3]:


# 1. Banyaknya data
print(len(df))
# 7651


# In[4]:


# 2. Data karyawan bernama Tuan Yon
print(df.loc[df["nama"] == "Tuan Yon"])
#           nama departemen  tahun_masuk  usia  golongan     gaji
# 1204  Tuan Yon  teknologi         2017    31        10  9939125


# In[7]:


# 3. Banyaknya karyawan dengan usia kurang dari atau sama dengan 30
print(len(df.loc[df["usia"] <= 30]))
# 1287


# In[17]:


# 4. Banyaknya karyawan personalia dengan gaji di luar rentang 4 - 5 juta
print(len(df.loc[(df["gaji"] > 5000000) | (df["gaji"] < 4000000)]))
# 6806


# In[20]:


# 5. Data karyawan produksi dengan gaji maksimum
dproduksi = df.loc[df["departemen"] == "produksi"]
print(dproduksi[dproduksi["gaji"] == dproduksi.max()["gaji"]])
#              nama departemen  tahun_masuk  usia  golongan     gaji
# 3454  Nur Lawiyah   produksi         2015    31         1  9997348


# In[23]:


# 6. Data 10 karyawan teknologi dengan gaji terbanyak. Jika ada gaji yang sama banyak, urutkan dari usia yang termuda
print(((df.loc[df["departemen"] == "teknologi"]).sort_values(["gaji", "usia"], ascending=[0,1]))[:10])
#                            nama departemen  tahun_masuk  usia  golongan      gaji
# 7530     Muhammad Darma Raditya  teknologi         2017    33         1   9992908
# 2082              Imam Putranto  teknologi         2017    30         1   9960615
# 7107         Yunia Nursita Sari  teknologi         2013    36         1   9958656
# 4270    Queena Zelina Primavera  teknologi         2013    38         1   9958328
# 4779                  Muh Izhak  teknologi         2014    28         7   9951585
# 1204                   Tuan Yon  teknologi         2017    31        10   9939125
# 83      Muhammad Ikhsan Dwianto  teknologi         2014    50         1   9932879
# 1446              Farid Hidayat  teknologi         2015    45         1   9930402
# 3323      Kharisrama Trihatmoko  teknologi         2015    27         1   9906720
# 1955  Muhammad Isyraqi El Hakim  teknologi         2014    51         1   9905403


# In[25]:


# 7. Tabel frekuensi banyaknya karyawan tiap golongan
print(df["golongan"].value_counts())
# 7     808
# 8     807
# 9     788
# 3     778
# 2     761
# 6     757
# 4     755
# 10    743
# 5     738
# 1     716


# In[27]:


# 8. Tabel frekuensi banyaknya karyawan tiap departemen yang masuk sebelum tahun 2015
print((df.loc[df["tahun_masuk"] < 2015])["departemen"].value_counts())
# produksi       469
# personalia     462
# operasional    457
# teknologi      443
# marketing      431
# kreatif        424
# keuangan       416


# In[28]:


# 9. Rata-rata gaji seluruh karyawan
print(df["gaji"].mean())
# 5516954.16638348


# In[30]:


# 10. Standar deviasi usia karyawan operasional
print((df.loc[df["departemen"] == "operasional"])["usia"].std())
# 10.398036110328745


# In[39]:


# 11. Dengan apakah gaji berkorelasi? Usia, tahun masuk, atau golongan? Tuliskan koefisien korelasinya
print("Koefisien korelasi gaji dan usia adalah", df["gaji"].corr(df["usia"]))
print("Koefisien korelasi gaji dan tahun masuk adalah",df["gaji"].corr(df["tahun_masuk"]))
print("Koefisien korelasi gaji dan golongan",df["gaji"].corr(df["golongan"]))
gu = 0
gt = 0
gg = 0

if((df["gaji"].corr(df["usia"])) < 0):
   gu = df["gaji"].corr(df["usia"]) * -1
if((df["gaji"].corr(df["tahun_masuk"])) < 0):
   gt = df["gaji"].corr(df["tahun_masuk"]) * -1
if((df["gaji"].corr(df["golongan"]) < 0)):
   gg = df["gaji"].corr(df["golongan"]) * -1

if (gu > gt):
    if(gu > gg):
        print("Gaji lebih berkorelasi dengan usia.")
    elif(gu == gg):
        print("Gaji lebih berkorelasi dengan usia dan golongan")
    else:
        print("Gaji lebih berkorelasi dengan golongan")
elif (gu < gt): # gt > gu/ koef kor. gaji tahun masuk > koef kor. gaji usia
    if(gt > gg):
        print("Gaji lebih berkorelasi dengan tahun masuk.")
    elif(gt == gg):
        print("Gaji lebih berkorelasi dengan tahun masuk dan golongan")
    else:
        print("Gaji lebih berkorelasi dengan golongan.")
else: # gt = gu/ koef kor. gaji tahun masuk = koef kor. gaji usia
    if(gu < gg):
        print("Gaji lebih berkorelasi dengan golongan")
    elif(gu > gg):
        print("Gaji lebih berkorelasi dengan usia.")
    else:
        print("Gaji berkorelasi dengan usia, tahun masuk, dan golongan.")
# Koefisien korelasi gaji dan usia adalah 0.0045757914258750245
# Koefisien korelasi nilai fisika dan matematika adalah 0.0130926769691646
# Koefisien korelasi nilai fisika dan matematika adalah -0.8777694422927667

