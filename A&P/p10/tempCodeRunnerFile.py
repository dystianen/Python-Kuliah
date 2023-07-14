def hitung_pecahan(uang):
    pecahan = [50000, 20000, 10000, 5000, 2000, 1000]
    jumlah_pecahan = [0] * len(pecahan)

    for i in range(len(pecahan)):
        if uang >= pecahan[i]:
            jumlah_pecahan[i] = uang // pecahan[i]
            uang = uang % pecahan[i]

    return jumlah_pecahan

uang = int(input("Masukkan jumlah uang: "))
jumlah_pecahan = hitung_pecahan(uang)

print("Jumlah pecahan 50000:", jumlah_pecahan[0])
print("Jumlah pecahan 20000:", jumlah_pecahan[1])
print("Jumlah pecahan 10000:", jumlah_pecahan[2])
print("Jumlah pecahan 5000:", jumlah_pecahan[3])
print("Jumlah pecahan 2000:", jumlah_pecahan[4])
print("Jumlah pecahan 1000:", jumlah_pecahan[5])
