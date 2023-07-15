def format_rupiah(amount):
    formatted_amount = f"Rp {amount:,.2f}"
    return formatted_amount

def hitung_diskon(total_belanja):
    diskon = 0

    if total_belanja < 120000:
        diskon = 0
    elif total_belanja >= 120000 and total_belanja < 500000:
        diskon = 0.1
    elif total_belanja >= 550000 and total_belanja < 1000000:
        diskon = 0.2
    elif total_belanja > 1200000:
        diskon = 0.3

    return diskon

total_belanja = float(input("Masukkan total belanja: "))

diskon = hitung_diskon(total_belanja)
jumlah_diskon = diskon * total_belanja
total_belanja_setelah_diskon = total_belanja - jumlah_diskon

print(f"Diskon: {int(diskon * 100)}%")
print(f"Jumlah diskon: {format_rupiah(jumlah_diskon)}")
print(f"Total belanja setelah diskon: {format_rupiah(total_belanja_setelah_diskon)}")