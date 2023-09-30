a = [2, 3, 4, 5, 1, 10, -1, 7]
#
# """
# найти и вывести на экран сумму элементов равных 9
#
# """

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == 9:
            print(a[i], a[j])

try:
    a, b = int(input('введите число номер 1: ')), int(input('введите число номер 2: '))
except ValueError:
    print('Ввод должен быть числом')
count = 0
for i in range(a, b +1):
    print(i)
    count += i
print()
print(f'Кол-во чисел {count}')

