from collections import deque

# membuat dan menginisialisasi antrian
dt_antrian = deque()

# masukkan item-item ke dalam antrian
dt_antrian.append("JavaTpoint")
dt_antrian.append("VB.NET")
dt_antrian.append("Tutorial")
dt_antrian.append("Queue")
dt_antrian.append("Array")
dt_antrian.append(10)

# hitung item dalam antrian menggunakan "len"
print("Total Entri Elemen dalam antrian adalah:", len(dt_antrian))
print("Elemen antrian adalah:")
for item in dt_antrian:
    print(item)

print()

# fungsi untuk membaca isi elemen dalam antrian menggunakan "in"
print("Apakah Elemen 'Array' ada dalam antrian?:", 'Array' in dt_antrian)
print("Apakah Elemen '5' ada dalam antrian?:", 5 in dt_antrian)
print()

# menampilkan nilai berikutnya yang akan dikeluarkan dari antrian
if dt_antrian:
    print("Nilai berikutnya untuk dimunculkan dari antrian adalah:", dt_antrian[0])

# penghapusan beberapa elemen dari antrian
num_to_remove = 2  # specify the number of elements to remove

# membuat antrian baru untuk menyimpan elemen yang tersisa
remaining_elements = deque()

# memindahkan elemen yang tersisa ke antrian baru
for _ in range(num_to_remove):
    if dt_antrian:
        obj = dt_antrian.popleft()
        print("Nilai yang dihapus:", obj)
        remaining_elements.append(obj)

print("Setelah elemen dihapus dari antrian")
for item in remaining_elements:
    print(item)

print("Tekan sembarang tombol untuk keluar dari console...")
