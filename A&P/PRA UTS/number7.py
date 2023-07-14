import datetime

tanggal = datetime.datetime.today().date()

if tanggal.day % 2 == 0:
    jenis_plat = "genap"
else:
    jenis_plat = "ganjil"

if tanggal.day == 31 and tanggal.month == 10:
    diperbolehkan = (jenis_plat == "ganjil")
elif tanggal.day == 1 and tanggal.month == 11:
    diperbolehkan = (jenis_plat == "ganjil")
elif tanggal.day == 2 and tanggal.month == 11:
    diperbolehkan = (jenis_plat == "genap")
else:
    diperbolehkan = False

if diperbolehkan:
    print(f"Kendaraan dengan plat nomor {jenis_plat} diperbolehkan lewat pada tanggal {tanggal.strftime('%d-%m-%Y')}.")
else:
    print(f"Kendaraan dengan plat nomor {jenis_plat} tidak diperbolehkan lewat pada tanggal {tanggal.strftime('%d-%m-%Y')}.")
