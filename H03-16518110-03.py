# NIM/Nama : 16518110/Kendrik Emkel Ginting
# Tanggal : 7 Oktober 2018
# Deskripsi : PR Praktikum Problem 03

# Program Pansangan Komposit
# Spesifikasi: Mencetak pasangan bilangan komposit dengan range A sampai B

# KAMUS
# A : int
# B : int

# Fungsi
def komposit(x):                # Fungsi untuk menentukan suatu bilangan komposit atau tidak
    # Kamus Lokal
    # IsKomposit = bool apakah bil x komposit
    # i = int counter
    IsKomposit = False          # Nilai awal IsKomposit, nilai awal false, sehingga nanti fungsi langsung berhenti ketika nilai berubah menjadi true
    i = 2                       # Nilai counter 2 agar dapat jug digunakan sebagai pembagi, jika i=1 semua bilangan dapat dibagi 1 dan IsKomposit = True pada semua bilangan
    while (i < x) and (IsKomposit == False):    # Selama i < x dan IsKomposit masih false, makan pengulangan akan berjalan
        if (x % i == 0):        # Jika x habis dibagi i, maka (lanjut ke bawah)
            IsKomposit = True   # IsKomposit True dan perulangan tidak akan berjalan lagi
        i += 1                  # counter i akan ditambah 1 setiap if selesai dilakukan
    return IsKomposit

def komposit2(x , y):
    # Kamus Lokal
    # IsKomposit2 = bool apakah bil x dan y pasangan komposit
    IsKomposit2 = False         # Nilai awal IsKomposit2, nilai awal false, akan menjadi true jika kondisi terpenuhi
    if (komposit(x)) and (komposit(y)) and (komposit(x + y)): #Syarat IsKomposit2 menjadi true sesuai soal
        IsKomposit2 = True
    return IsKomposit2

# Algoritma
# Input
A = int(input("Masukkan A: "))  # Input nilai A
B = int(input("Masukkan B: "))  # Input nilai B

# Proses dan Output
print ("Pasangan bilangan komposit:")
for i in range (A, B+1):        # Selama i bernilai A sampai B
    for j in range (A, B+1):    # dan j bernilai A sampai B
        if (komposit2(i , j) == True) and (i < j):  # Jika i dan j pasangan komposit dan i < j, maka
            print(str(i) + " " + str(j))            # program akan mencetak i dan j
