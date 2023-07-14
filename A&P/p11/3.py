import random

list1 = []
for i in range(10):
    list1.append(random.randint(0, 100))

x = int(input('Masukan nilai x: '))

list2 = []
for i in range(len(list1)):
    list2.append(list1[i] * x)

print(f'T : {list1}')
print(f'X : {x}')
print(f'Setelah Element T Dikalikan : {list2}')