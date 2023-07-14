number1 = int(input('Masukan Angka Pertama      : '))
number2 = int(input('Masukan Angka Kedua        : '))
operator = input('Masukan Operator [+/-/x/:] : ')

if operator == '+':
    result = number1 + number2
    print('Hasil: ', result)
elif operator == '-':
    result = number1 - number2
    print('Hasil: ', result)
elif operator == 'x':
    result = number1 * number2
    print('Hasil: ', result)
elif operator == ':':
    result = number1 / number2
    print('Hasil: ', result)
else:
    print('Operator tidak valid!')