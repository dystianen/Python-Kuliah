def doSearch(kata, teks):
    kata_ditemukan = []
    kata_split = teks.split()

    for kata_teks in kata_split:
        if kata.lower() in kata_teks.lower():
            kata_ditemukan.append(kata_teks)

    return kata_ditemukan


teks = input("Masukkan sebuah teks: ")
kata = input("Masukkan kata atau huruf yang ingin dicari: ")
print(50 * '-')

result = doSearch(kata, teks)

if result:
    for kata_ditemukan in result:
        print('Kata yang ditemukan dalam teks: ', kata_ditemukan)
else:
    print("Tidak ada kata yang di cari.")

print(50 * '-')