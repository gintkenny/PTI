# NIM/Nama : 16518008/Basilius Agung Yason Sunarya, 16518110/Kendrik Emkel Ginting, 16518212/Ilham Rayhan, 16518314/Feroz Fernando
# Tanggal : 17 Oktober 2018 (Updated 29 Oktober 2018)
# Deskripsi : Program Proyek 1 Polinom

# Program Polinom
# Spesifikasi: Menerima input 2 polinom dari user, kemudian mencetak hasil penjumlahannya, pengurangannya, dan turunannya

# KAMUS
# p1, p2, p3 : array of integer untuk polinom 1, polinom 2, dan polinom 3
# Menu  : string pilihan menu yang dipilih user

# Fungsi dan Prosedur
def Cetak(x):   # Prosedur untuk mencetak sebuah polinom
    # Kamus Lokal
    # pertama: bool apakah pangkat tertinggi sudah dicetak
    # i: int counter
    # i1 : suku terbesar
    pertama = 0     # Untuk mencetak nilai pertama (pangkat tertinggi)
    i = 99          # i = 99 sebagai counter sesuai dengan kemungkinan pangkat tertinggi
    while ((pertama == 0) and (i >= 0)):    # Selama nilai pertama belum dicetak dan i antara 99 sampai 0, program mengulang. Program akan keluar setelah nilai pertama != 0
        if(x[i] != 0):                      # Jika koefisien polinom tidak sama dengan 0 (polinom ada),
            pertama = 1                     # Nilai pertama ditemukan dan akan dicetak
            if(i != 0) and (i != 1):        # Jika pangkat tidak sama dengan 0 dan 1,
                if(x[i] == 1):              # Jika koefisien satu
                    print("x^" + str(i), end=" ")   # Program mencetak x^i
                elif(x[i] == -1):           # Jika koefisien -1
                    print("-x^" + str(i), end=" ")  # Program mencetak -x^i
                elif(x[i] > 0):             # Jika koefisien lebih besar dari 0 dan bukan satu (jika koef 1 if sebelumnya sudah terpenuh sehingga tidak akan masuk ke elif)
                    print(str(x[i]) + "x^" + str(i), end=" ")   # Program mencetak kx^i
                elif(x[i] < 0):             # Jika koefisien lebih kecil dari 0,
                    print("-" + str(-1 * x[i]) + "x^" + str(i), end=" ") # Program mencetak -kx^i
            elif (i == 1):                  # Jika pangkat 1, dan
                if(x[i] == 1):              # Jika koefisien 1,
                    print("x", end=" ")     # Program mencetak x
                elif(x[i] == -1):           # selain itu, jika koefsien -1
                    print("-x", end=" ")    # Program mencetak -x
                elif(x[i] > 0):               # Selain itu, jika koefisien lebih besar dari 0 dan bukan satu (jika koef 1 if sebelumnya sudah terpenuh sehingga tidak akan masuk ke elif)
                    print(str(x[i]) + "x", end=" ") # Program mencetak kx
                elif(x[i] < 0):               # Selain itu, jika koefisien lebih kecil dari 0,
                    print("-" + str(-1 * x[i]) + "x", end=" ")  # Program mencetak -kx
            else:   # Jika i (pangkat) = 0
                print(str(x[i]))    # Program akan mencetak k saja
            i1 = i                  # Program akan mengingat pangkat tertinggi agar tidak tercetak lagi nanti
        i -= 1                      # i akan selalu berkurang 1 setiap program berjalan sesuai urutan

    if(pertama == 0):      # Jika pertama == 0 (polimon kosong)
        i1 = 0             # suku terbesar = 0
        print(str(x[i1]))  # Prorgam mencetak 0

    for i in range(99, -1 ,-1):     # Untuk i di antara 99 sampai -1, secara mundur
        if (x[i] != 0) and (i != i1):   # Jika koefisien tidak 0 dan pangkat tidak sama dengan i1 (pangkat yang sudah dicetak)
            if (i != 0) and (i != 1):   # Jika pangkat tidak 0 dan 1
                if (x[i] == 1):         # Jika koefisien 1
                    print("+ " + "x^" + str(i), end=" ")    # Progrm akan mencetak + x^i
                elif (x[i] == -1):      # selain itu, jika koefisien -1
                    print("- " + "x^" + str(i), end=" ")    # Program akan mencetak - x^i
                elif (x[i] > 0):        # selain itu, jika koefisien >0
                    print("+ " + str(x[i]) + "x^" + str(i), end=" ")    # Program akan mencetak + kx^i
                elif (x[i] < 0):        # Selain itu, jika koefisien <0
                    print("- " + str(-1 * x[i]) + "x^" + str(i), end=" ")   # Program akan mencetak - kx^i
            elif (i == 1):              # Jika pangkat = 1
                if (x[i] == 1):         # Jika koefisien = 1
                    print("+ " + "x", end=" ")  # Program akan mencetak + x
                elif (x[i] == -1):      # Jika koefisien = -1
                    print("- " + "x", end=" ")  # Program akan mencetak - x
                elif (x[i] > 0):        # Jika koefisien > 0
                    print("+ " + str(x[i]) + "x", end=" ")  # Program akan mencetak + kx
                elif (x[i] < 0):        # Jika koefisien < 0
                    print("- " + str(-1 * x[i]) + "x", end=" ") # Program akan mencetak - kx
            else:   # Jika pangkat = 0
                if (x[i] > 0):          # Jika koefisien lebih besar dari 0
                    print("+ " + str(x[i]), end=" ")    # Program akan mencetak + k
                elif (x[i] < 0):        # Jika koefisien lebih kecil dari 0
                    print("- " + str(-1 * x[i]), end=" ")   # Program akan mencetak - k

def PolIn(x, n):    # Prosedur untuk Input Polinom x. n berguna hanya untuk proses pencetakan "Masukkan polinom ke-n..."
    # Kamus Lokal
    # IsFinished = bool apakah input sudah selesai
    # suku = int suku ke- sekian
    # nilai = int nilai dari suku tersebut
    IsFinished = 0              # Nilai awal IsFinished adalah False, karena input belum selesai
    while (IsFinished == 0):    # Selama IsFinished = False, program terus berjalan
        suku, nilai = input("Masukkan polinom ke-" + str(n) + " dengan cara mengetik <suku, koefisien> tanpa <> : " ).split(", ") # Input suku dan nilai dengan format suku, nilai
        if(int(suku) == -999):  # Jika user memasukkan suku -999
            IsFinished = 1      # IsFinished akan menjadi true dan proses input selesai
        elif((int(suku) < 0) or (int(suku) > 99)):  # Jika user memasukkan suku dengan nilai < 0 atau > 99
            print ("Suku yang Anda masukkan salah. Suku berkisar antara 0 sampai 99.")  # Pesan error akan keluar dan nilai input pun akan diabaikan
        else:                   # Jika input benar (antara 0 sampai 99),
            x[int(suku)] = int(nilai)   # Nilai dari suku akan dimasukkan ke array sesuai dengan sukunya

def Jml(x1, x2, x3):        # Fungsi untuk penjumlahan 2 polinom x1 dan x2 dengan x3 sebagai polinom hasilnya
    for i in range (100):   # Untuk i dari 0 berulang sebanyak 100 kali
        x3[i] = x1[i] + x2[i]   # Jumlah dari pangkat yang sama akan disimpan di array ketiga pada pangkat yang sama pula
    Cetak(x3)           # Program akan mencetak polinom hasil

def Kurang(x1, x2, x3):
    for i in range (100):   # Untuk i dari 0 berulang sebanyak 100 kali
        x3[i] = x1[i] - x2[i]   # Polinom pertama dikurang polinom kedua pada pangkat yang sama akan disimpan di array ketiga pada pangkat yang sama pula
    Cetak(x3)           # Program akan mencetak polinom hasil

def Turunan(x1, x3):        # Prosedur untuk mencetak turunan dari x1 yang disimpan di x3
    for i in range (99):    # Untuk i dari 1 sebanyak 99 kali [0, 98]
        x3[i] = x1[i+1] * (i+1) # Misalnya turunan dari 2x adalah 2, pada x3 disimpan di index 0 (tak berpangkat), nilainya adalah koefisien dikali pangkat dari index (pangkat) 1 di polinom awal
    Cetak(x3)               # Program akan mencetak polinom 3

def Menu():                 # Prosedur menu dari program
    print("Menu Program Polinom")
    print("Menu 1: Cetak Nilai Polinom Ke-1 dan Ke-2")
    print("Menu 2: Cetak Nilai Jumlah Polinom Ke-1 dan Ke-2")
    print("Menu 3: Cetak Nilai Polinom Ke-1 Dikurangi Polinom Ke-2")
    print("Menu 4: Cetak Nilai Turunan Polinom Ke-1 dan Polinom Ke-2")
    print("Menu 0: Tutup Program")
    print("Untuk memilih menu, ketik nomor menu.")

# Algoritma
print("Program Polinom")
print("Masukkan polinom dengan format yang tersedia, jika tidak program akan error.")
print("Silakan masukkan kedua polinom Anda.")
print()

# Input
p1 = [0 for i in range (100)]   # Delarasi array polinom pertama
p2 = [0 for i in range (100)]   # Deklarasi array polinom kedua
p3 = [0 for i in range (100)]   # Deklarasi array polinom ketiga untuk hasil operasi

print("Polinom Ke-1")
print("Untuk menyudahi pemasukkan polinom, ketik suku = -999 dan koefisien sesuka Anda. Misal: -999, 0")
PolIn(p1, 1)    # Input polinom pertama
print()
print("Polinom Ke-2")
print("Untuk menyudahi pemasukkan polinom, ketik suku = -999 dan koefisien sesuka Anda. Misal: -999, 0")
PolIn(p2, 2)    # Input polinom kedua
print()

# Proses dan Output
Menu()          # Mencetak menu
menu = input("Pilih menu yang tersedia: ")  # Input menu yang dipilih
print()

while(menu != "0"):             # Selama menu yang dipilih bukan 0, program akan terus berjalan, mengingat menu 0 artinya keluar program
    if(menu == "1"):            # Jika menu yang dipilih adalah 1
        print("Polinom ke-1 yang Anda masukkan adalah:")
        Cetak(p1)               # Program akan mencetak polinom 1
        print("Polinom ke-2 yang Anda masukkan adalah:")
        Cetak(p2)               # Program akan mencetak polinom 2
        print("Pekerjaan menu ini selesai. Silakan memilih menu lain.")
        print()
    elif(menu == "2"):          # Jika menu yang dipilih adalah 2
        print("Polinom ke-1 dijumlahkan dengan Polinom ke-2 hasilnya:")
        Jml(p1, p2, p3)         # Program akan mencetak jumlah polinom 1 dan 2 yang disimpan dalam polinom 3
        print("Pekerjaan menu ini selesai. Silakan memilih menu lain.")
        print()
    elif(menu == "3"):          # Jika menu yang dipilih adalah 3
        print("Polinom ke-1 dikurangi Polinom ke-2 hasilnya:")
        Kurang(p1, p2, p3)      # Program akan mencetak polinom 1 dikurangi polinom 2 yang disimpan dalam polinom 3
        print("Pekerjaan menu ini selesai. Silakan memilih menu lain.")
        print()
    elif(menu == "4"):          # Jika menu yang dipilih adalah 4
        print("Turunan polinom ke-1 adalah:")
        Turunan(p1, p3)         # Program akan mencetak turunand dari polinom p1 yang disimpan di p3
        print("Turunan polinom ke-2 adalah:")
        Turunan(p2, p3)         # Program akan mencetak turunand dari polinom p2 yang disimpan di p3
        print("Pekerjaan menu ini selesai. Silakan memilih menu lain.")
        print()
    else:
        print("Menu yang Anda masukkan salah. Silakan pilih menu yang tersedia!")
    Menu()                      # Setelah pekerjaan selesai ditampilkan, menu ditampilkan kembali
    menu = input("Pilih menu yang tersedia: ")  # Program akan meminta user kembali menginput pilihan menu
    print()
