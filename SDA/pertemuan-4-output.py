# Number 1
print("a. Harga: ", 'Rp', 7.700, sep="")
print("b. Akurasi: ", 90, "%", sep="")
print("c. Data", "Sci", "ence", sep="")
print("d. Akurasi", 90, "%", sep="")
print("e. Cerdas\tAmanah\n\tKreatif")
print("f. COUNTRY\t", "LAND AREA") 
print("India\t", 2.5, "million sq km")
print("China\t", 9.6, "million sq km")

x = 10
y = 8
print("g. The matix of {0:d} and {1:d} has {2:d} elements".format(x, y, x * y))

str1 = "h. If {0:s} dream it, {0:s} do it - Walt Disney"
print(str1.format("you can"))
print("\n")

# Number 2
print("NUMBER\tSQUARE\tCUBE")
print(str(2) + "\t", str(2**2), "\t", str(2**3))
print(str(3) + "\t", str(3**2), "\t", str(3**3))
print("\n")

# NUMBER 3
print("{0:22s} {1:s}".format("Departemen", "Persentase Mahasiswa"))
print("{0:18s} {1:10.1%}".format("Statistika Bisnis", .20))
print("{0:14s} {1:10.1%}".format("Teknik Informatika", .50))
print("{0:18s} {1:10.1%}".format("Sistem Infomasi", .30))
print("\n")

# NUMBER 4
price = 150000
diskon = '10%'
print("Harga Asli = ", "Rp.", price, sep="")
print("Diskon = ", diskon)
total = price - price * 10 / 100
print("Harga Setelah Diskon = ", "Rp.", int(total), sep="")
print('\n')

# NUMBER 5
pendapatan = input("Pendapatan = ")
pengeluaran = input("pengeluaran = ")

laba_bersih = int(pendapatan) - int(pengeluaran)
print("Laba bersih = ", laba_bersih)
