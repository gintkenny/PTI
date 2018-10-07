# NIM/Nama : 16518110/Kendrik Emkel Ginting
# Tanggal : 7 Oktober 2018
# Deskripsi : PR Praktikum Problem 01

# Program Menghitung Kombinasi Komandan Batalyon Mentor OSKM
# Spesifikasi: Menghitung kombinasi komandan batalyon mentor OSKM dengan sebanyak N calon dan K mentor

# KAMUS
# K : int banyak mentor OSKM
# N : int banyak calon danyon

# Fungsi
def faktorial(x):               # Fungsi untuk menghitung faktorial
    # Kamus Lokal
    # xfak = int hasil x!
    xfak = 1                    # Nilai awal x!, 1 agar dapat dikali
    for i in range (1, x+1):    # i bernilai antara x, (x-1), (x-2), ..., 2, 1
        xfak *= i               # xfak = x*(x-1)*(x-2)*...*2*1
    return xfak

def nck(n , k):             # Fungsi kombinasi
    return faktorial(n) // (faktorial(k) * faktorial(n-k)) # Menghitung n kombinasi k

# Algoritma
# Input
N = int(input("Masukkan N: "))  # Input nilai N
K = int(input("Masukkan K: "))  # Input nilai K

# Proses dan Output
print("Kombinasinya ada " + str(nck(N, K))) # Output banyak kombinasi komandan batalyon
