import hashlib
def signup():
    email = input("Enter email address: ") # Meminta pengguna memasukkan alamat email
    pwd = input("Enter password: ") # Meminta pengguna memasukkan kata sandi
    conf_pwd = input("Confirm password: ") # Meminta pengguna mengonfirmasi kata sandi
    if conf_pwd == pwd: # Memeriksa apakah kata sandi yang dikonfirmasi sama dengan kata sandi yang dimasukkan
        enc = conf_pwd.encode() # Mengonversi kata sandi yang dikonfirmasi ke bentuk byte
        hash1 = hashlib.md5(enc).hexdigest()  # Membuat hash MD5 dari kata sandi yang dikonfirmasi
        with open("Tugas Besar/credentials.txt", "a+") as f: # Membuka file "credentials.txt" dalam mode tulis
            f.seek(0) # memindahkan posisi baca/tulis dalam file ke awal atau offset 0
            lines = f.readlines() # membaca seluruh baris dalam file tersebut dan menyimpannya ke dalam variabel lines
            if lines:  # Jika file tidak kosong
                last_line = lines[-1].strip()  # Mengambil baris terakhir (ID terakhir)
                last_id = int(last_line.split()[0])  # Mengambil ID terakhir
                new_id = last_id + 1  # Menghasilkan ID baru
            else:
                new_id = 1  # Jika file kosong, ID dimulai dari 1

            f.write(f"{new_id} - {email} - {hash1} \n") # Menulis id, alamat email, dan password dalam bentuk hash md5 ke dalam file
        f.close() # Menutup file
        print("You have registered successfully! \n") # Menampilkan pesan bahwa pendaftaran berhasil
    else:
        print("Password is not same as above! \n") # Menampilkan pesan bahwa kata sandi tidak cocok dengan konfirmasi

# Fungsi untuk masuk ke akun
def login():
    email = input("Enter email: ")  # Meminta pengguna memasukkan email
    pwd = input("Enter password: ")  # Meminta pengguna memasukkan kata sandi
    auth = pwd.encode()  # Mengonversi kata sandi ke bentuk byte
    auth_hash = hashlib.md5(auth).hexdigest()  # Membuat hash MD5 dari kata sandi
    with open("Tugas Besar/credentials.txt", "r") as f:  # Membuka file "credentials.txt" dalam mode baca
        lines = f.readlines() # membaca seluruh baris dalam file tersebut dan menyimpannya ke dalam variabel lines
    f.close()  # Menutup file
    for line in lines: # Melakukan iterasi untuk setiap baris dalam list "lines"
        line_parts = line.strip().split(" - ") # Memecah baris menjadi bagian-bagian dengan menggunakan pemisah " - "
        stored_email = line_parts[1] # Mengambil alamat email yang tersimpan pada posisi indeks 1
        stored_pwd = line_parts[2] # Mengambil hash kata sandi yang tersimpan pada posisi indeks 2
        if email == stored_email and auth_hash == stored_pwd:  # Memeriksa apakah email dan hash kata sandi cocok dengan yang tersimpan
            print("Logged in Successfully! \n")  # Menampilkan pesan bahwa login berhasil
            return
    print("Login failed! \n")  # Menampilkan pesan bahwa login gagal

while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: ")) # Meminta pengguna memasukkan pilihan
    if ch == 1:
        signup() # Memanggil fungsi signup() jika pilihan adalah 1
    elif ch == 2:
        login() # Memanggil fungsi login() jika pilihan adalah 2
    elif ch == 3:
        break # Menghentikan program jika pilihan adalah 3
    else:
        print("Wrong Choice!") # Menampilkan pesan bahwa pilihan salah