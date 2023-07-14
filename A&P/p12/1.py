def calculator(operator, angka1, angka2):
    try:
        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
        elif operator == '/':
            hasil = angka1 / angka2
        else:
            raise ValueError("Operator yang dimasukkan salah: " + operator)
        
        return hasil
    
    except ValueError as err:
        return str(err)
    
    except Exception as err:
        return "Terjadi kesalahan: " + str(err)

try:
    operator = input("Masukkan operator (+, -, *, /): ")
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    
    hasil = calculator(operator, angka1, angka2)
    print("Hasil: ", hasil)

except ValueError:
    print("Input harus berupa bilangan bulat (int).")
    
except Exception as err:
    print("Terjadi kesalahan: ", err)
