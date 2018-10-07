    # NIM/Nama : 16518110/Kendrik Emkel Ginting
    # Tanggal : 7 Oktober 2018
    # Deskripsi : PR Praktikum Problem 02

    # Program Menghitung Fungsi f
    # Spesifikasi: Menghitung fungsi f sesuai dengan rumus yang diberikan pada soal

    # KAMUS
    # X : float nilai X

    # Fungsi
    def faktorial(x):               # Fungsi untuk menghitung faktorial
        # Kamus Lokal
        # xfak = int hasil x!
        xfak = 1                    # Nilai awal x!, 1 agar dapat dikali
        for i in range (1, x+1):    # i bernilai antara x, (x-1), (x-2), ..., 2, 1
            xfak *= i               # xfak = x*(x-1)*(x-2)*...*2*1
        return xfak

    def pangkat(x , y):             # Fungsi kombinasi
        # Kamus Lokal
        # xy = int hasil x pangkat y (x^y)
        xy = 1                      # Nilai awal x^y, 1 agar dapat dikali
        for i in range (1, y+1):    # Selama i bernilai 1 sampai y,
            xy *= x                 # xy dikalikan x
        return xy

    def fx(x):                   # Fungsi f(x) sesuai dengan soal
        # Kamus Lokal
        # fx = float nilai f(X)
        fx = float(0)                      # Nilai awal fungsi f(x), 0 karena penjumlahan, float karena desimal
        for k in range(51):      # Selama i antara 1 sampai 51 (notasi sigma)
            fx += pangkat(-1, k) * pangkat(x, 2 * k + 1) / faktorial(2 * k + 1)    # fx = jumlah dari nilai fx sebelumnya dengan hasil f(x)
        return fx

    # Algoritma
    # Input
    X = float(input("Masukkan X: "))  # Input nilai X

    # Proses dan Output
    print("Nilai f(X) = " + str(fx(X))) # Output banyak kombinasi komandan batalyon
