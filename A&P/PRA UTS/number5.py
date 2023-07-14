import locale
locale.setlocale(locale.LC_ALL, '')

print("=========================================")
print("          Ujian Tengah Semester          ")
print("Nama: Dystian En Yusgiantoro")
print("=========================================")

major_code = ["TI", "TE", "TS", "TM", "MJ", "AKT", "BING", "ILKOM"]
major = [
    "Teknik Informatika",
    "Teknik Elektro",
    "Teknik Sipil",
    "Teknik Mesin",
    "Manajemen",
    "Akuntansi",
    "Bahasa Inggris",
    "Ilmu Komunikasi",
]

cost = [4900000, 4600000, 4800000, 4700000, 4200000, 4150000, 4100000, 4250000]
additional_cost = 0

nisn = input("Masukan NISN: ")
name = input("Masukan Nama Lengkap: ")
no_hp = input("Masukan Nomor Telepon: ")
domicile = input("Masukan Alamat Domisili: ")
faculty = input("Masukan Fakultas [FTI/FBIS]: ")
jurusan = input("Masukan Jurusan [TI/TE/TS/TM/MJ/AKT/BING/ILKOM]: ")
classes = input("Masukan Kelas Reguler [Reguler 1/Reguler 2]: ")

print("=========================================")
print(" Data Pendaftaran Siswa")
print("=========================================")
print("NISN:", nisn)
print("Nama Lengkap:", name)
print("Nomor Telepon:", no_hp)
print("Alamat Domisili:", domicile)
print("Fakultas:", faculty)

if jurusan in major_code:
    index = major_code.index(jurusan)
    biaya_kuliah = cost[index]
    print("Jurusan:", major[index])
    print("Biaya Kuliah:", locale.currency(biaya_kuliah, grouping=True))
else:
    print("Jurusan tidak tersedia")

print("Kelas:", classes)

if classes == "Reguler 2":
    additional_cost = 700000
    print("Biaya Tambahan:", locale.currency(additional_cost, grouping=True))

print('Jumlah Biaya: ', locale.currency(biaya_kuliah + additional_cost, grouping=True))
print("=========================================")
print("UTS by Dystian En Yusgiantoro")
print("=========================================")
