golonganA = 6000
golonganB = 8000
golonganC = 3000
golonganD = 14000

def hitung_gaji(golongan, jam_kerja):
    if golongan == 'A':
        gaji_pokok = golonganA
    elif golongan == 'B':
        gaji_pokok = golonganB
    elif golongan == 'C':
        gaji_pokok = golonganC
    elif golongan == 'D':
        gaji_pokok = golonganD
    else:
        return "Golongan tidak valid."
    
    if jam_kerja > 48:
        jam_lembur = jam_kerja - 48
        gaji_lembur = jam_lembur * 4000
        gaji_total = gaji_pokok + gaji_lembur
    else:
        gaji_total = gaji_pokok
        
    return gaji_total

def format_rupiah(amount):
    formatted_amount = f"Rp {amount:,.2f}"
    return formatted_amount

nama_karyawan = input("Masukkan nama karyawan: ")
golongan = input("Masukkan golongan (A/B/C/D): ")
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

gaji = hitung_gaji(golongan, jam_kerja)
print(f"Gaji {nama_karyawan}: {format_rupiah(gaji)}")
