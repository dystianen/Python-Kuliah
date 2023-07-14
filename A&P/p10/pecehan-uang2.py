def hitung_pecahan(uang):
    pecahan = [5000, 100]
    jumlah_pecahan = {}

    for p in pecahan:
        if uang >= p:
            jumlah = int(uang // p)
            jumlah_pecahan[p] = jumlah
            uang -= p * jumlah

    return jumlah_pecahan

uang = float(input("Masukkan Jumlah Uang: "))
jumlah_pecahan = hitung_pecahan(uang)

print(jumlah_pecahan)