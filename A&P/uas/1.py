def print_segitiga_siku_terbalik(n):
    for i in range(n, 0, -1):
        print("* " * i)

n = int(input("Masukkan tinggi segitiga: "))
print_segitiga_siku_terbalik(n)