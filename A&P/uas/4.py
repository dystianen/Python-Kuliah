number_of_elements = int(input("Input Jumlah Elemen: "))

list_of_numbers = []
for i in range(1, number_of_elements + 1):
    number = int(input(f"Elemen ke {i}: "))
    list_of_numbers.append(number)

biggest_number = max(list_of_numbers)
indeks_of_biggest_number = list_of_numbers.index(biggest_number) + 1

print(f"Angka Terbesar adalah {biggest_number} ada di Elemen ke - {indeks_of_biggest_number}")