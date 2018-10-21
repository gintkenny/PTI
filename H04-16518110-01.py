# NIM/Nama  : 16518110/Kendrik Emkel Ginting
# Tanggal   : 21 Oktober 2018
# Deskripsi : PR Data Analisis 1 H04

# Spesifikasi: Menjawab task 01 pada H04

# Kamus
# df = dataframe database

# Algoritma
import pandas as pd

df = pd.read_csv("stei-c-1.csv")

# 1. Banyaknya data
print(len(df))
# 9615

# 2. Nilai matematika, fisika, dan kimia dari mahasiswa bernama Tuan Yon.
print(df.loc[df["nama"] == "Tuan Yon"])
#           nama fakultas  nilai_mat  nilai_fis  nilai_kim
# 4859  Tuan Yon     STEI         91         83         63

# 3. Banyaknya mahasiswa dengan nilai matematika di atas 80
print(len(df.loc[df["nilai_mat"] > 80]))
# 2708

# 4. Banyaknya mahasiswa yang mendapat nilai kurang dari 40 di matkul apapun
print(len(df.loc[(df["nilai_mat"] < 40) | (df["nilai_kim"] < 40) | (df["nilai_fis"] < 40)]))
# 4392

# 5. Banyaknya mahasiswa yang mendapat nilai terendah di fisika
print(len(df.loc[df["nilai_fis"] == (df.min()["nilai_fis"])]))
# 110

# 6. Data 10 besar peserta peraih nilai tertinggi di fisika. Jika ada yang nilainya sama, ambil mahasiswa dengan nama lebih kecil
print((df.sort_values(["nilai_fis", "nama"], ascending=[0,1]))[:10])
#                             nama fakultas  nilai_mat  nilai_fis  nilai_kim
# 9225     Abdurrahman P Hutasuhut     FTSL         77         99         81
# 5365            Adi Theodosius S     FTMD         62         99         81
# 5148            Agha Achmad Reza    SITHR         40         99         81
# 7028   Ahmad Anggriyanto Asrizal     FTMD         34         99         81
# 8790      Ahmad Sodiq El Husaini    SITHR         75         99         68
# 4074         Ahmad Yasin Rabbani    SITHR         78         99         81
# 8119        Ahmad Zahi Ulul Azmi     FTMD         69         99         81
# 2714   Aileen Alethea Widyaswara    SITHR         95         99         81
# 8416            Amelinda Bethari     FTMD         74         99         81
# 1915  Andi Aulia Sukma Pamungkas     STEI         90         99         81

# 7. Tabel frekuensi masing-masing fakultas
print(df["fakultas"].value_counts())
# FTSL     2459
# SITHR    2420
# STEI     2388
# FTMD     2348

# 8. Rata-rata dari nilai matematika semua mahasiswa
print(df["nilai_mat"].mean())
# 65.0114404576183

# 9. Standar deviasi dari nilai fisika semua mahasiswa
print(df["nilai_fis"].std())
# 25.85425684162357

# 10. Rata-rata dari nilai kimia STEI
print((df.loc[df["fakultas"] == "STEI"])["nilai_kim"].mean())
# 50.879396984924625

# 11. Dengan nilai manakah (matematika / kimia) nilai fisika berkorelasi? Berapa koefisien korelasinya?
print("Koefisien korelasi nilai fisika dan kimia adalah", df["nilai_fis"].corr(df["nilai_kim"]))
print("Koefisien korelasi nilai fisika dan matematika adalah",df["nilai_fis"].corr(df["nilai_mat"]))

if((df["nilai_fis"].corr(df["nilai_kim"])) < 0): # jika korelasi fis kim negatif
    if((df["nilai_fis"].corr(df["nilai_mat"])) < 0): # jika korelasi fis mat negatif / fis kim dan fis mat sama-sama negatif
        if((df["nilai_fis"].corr(df["nilai_kim"])) < (df["nilai_fis"].corr(df["nilai_mat"]))): # jika korelasi fis kim < fis mat maka
            print("Nilai fisika lebih berkorelasi dengan nilai kimia.") # nilai fisika lebih berkorelasi dengan nilai kimia
        else: # jika korelasi fis mat < fis kim maka
            print("Nilai fisika lebih berkorelasi dengan nilai matematika.") # nilai fis berkorelasi dengan nilai mat
    else: # jika korelasi fis mat positif
        if((-1 * (df["nilai_fis"].corr(df["nilai_kim"])))) < (df["nilai_fis"].corr(df["nilai_mat"])): # jika |korelasi fis kim| < korelasi fis mat
            print("Nilai fisika lebih berkorelasi dengan nilai matematika.") # nilai fis berkorelasi dengan nilai mat
        else: # jika |korelasi fis kim| > korelasi fis mat
            print("Nilai fisika lebih berkorelasi dengan nilai kimia.") # nilai fis berkorelasi dengan nilai mat
else: # jika korelasi fis kim positif
    if((df["nilai_fis"].corr(df["nilai_mat"])) < 0): # jika korelasi fis mat negatif
        if((df["nilai_fis"].corr(df["nilai_kim"])) < (-1 * (df["nilai_fis"].corr(df["nilai_mat"])))): # jika korelasi fis kim < |korelasi fis mat|
            print("Nilai fisika lebih berkorelasi dengan nilai matematika.") # maka nilai fisika berkorelasi dengan nilai matematika
        else: # jika korelasi fis kim > |korelasi fis mat|
            print("Nilai fisika lebih berkorelasi dengan nilai kimia.") # maka nilai fisika berkorelasi dengan nilai matematika
    else: # jika korelasi fis mat positif / fis kim dan fis mat sama-sama positif
        if((df["nilai_fis"].corr(df["nilai_kim"])) < (df["nilai_fis"].corr(df["nilai_mat"]))): # jika korelasi fis kim < fis mat
            print("Nilai fisika lebih berkorelasi dengan nilai matematika.") # maka nilai fisika berkorelasi dengan nilai matematika
        else: # jika korelasi fis kim > fis mat
            print("Nilai fisika lebih berkorelasi dengan nilai kimia.") # maka nilai fisika berkorelasi dengan nilai kimia

if((df["nilai_fis"].corr(df["nilai_kim"])) == (df["nilai_fis"].corr(df["nilai_mat"]))):
    print("Nilai fisika berkorelasi dengan nilai matematika dan kimia.")
# Koefisien korelasi nilai fisika dan kimia adalah 0.8209095252461834
# Koefisien korelasi nilai fisika dan matematika adalah -7.030486139182184e-05
# Nilai fisika lebih berkorelasi dengan nilai kimia.
