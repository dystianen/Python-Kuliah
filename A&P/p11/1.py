total_mhs = int(input("Input Total Mahasiswa: "))
data_mhs = []

for x in range(1, total_mhs + 1):
    print(30 * '-')
    nim = input(f'Masukan NIM ke-{x}: ')
    mahasiswa = input(f'Masukan Nama Mahasiswa ke-{x}: ')
    finalScore = float(input(f'Masukan Nilai Akhir ke-{x}: '))

    data_mhs.append({'nim': nim, 'mahasiswa': mahasiswa, 'finalScore': finalScore})

def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if array[j]['finalScore'] < array[j + 1]['finalScore']:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

sorted_data = bubble_sort(data_mhs)

print()
print(40 * "=")
print("Sorted Data (Highest to Lowest):")
print(40 * "=")
for data in sorted_data:
    print("NIM:", data['nim'])
    print("Mahasiswa:", data['mahasiswa'])
    print("Final Score:", data['finalScore'])
    print(30 * '-')
