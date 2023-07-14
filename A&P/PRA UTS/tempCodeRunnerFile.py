print("=========================================")
print("          Ujian Tengah Semester          ")
print("Nama: Dystian En Yusgiantoro")
print("=========================================")

menu = [
    "Pandan Latte",
    "Matcha",
    "Espresso",
    "Cuppocino",
    "Kopi Kenangan Mantan",
    "Kopi Kangen",
    "Kopi Enak",
]
price = [28000, 29000, 25000, 28000, 31000, 26000, 18000]

lst = []

next_order = "y"

while next_order == "y":
    print("Daftar Menu pada Warung Kopi Kita")
    for i in range(len(menu)):
        print(i + 1, menu[i], "", price[i])
        
    print("Daftar Pesanan")
    menu_code = int(input("Masukan Kode Menu: "))
    if menu_code < 1 or menu_code > len(menu):
        print("Kode menu salah")
        continue

    item = {"menu": menu[menu_code - 1], "price": price[menu_code - 1]}
    lst.append(item)

    print(f"{item['menu']} ditambahkan ke pesanan")
    next_order = input("Lanjutkan Pemesanan (y/t): ").lower()

print("=========================================")
total_price = 0
for i, item in enumerate(lst):
    print(i + 1, item["menu"], "", item["price"])
    total_price += item["price"]

print("Harga Yang Dibayarkan: ", total_price)
print("=========================================")