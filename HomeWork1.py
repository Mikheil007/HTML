# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции

userList = list(map(int, input('Введите числа списка через пробел: ').split()))
print(f'Ваш список: {userList}')

sumListNum = 0

for i in range(1, len(userList), 2):
     sumListNum = sumListNum + userList[i]

print(f'Сумма элементов на нечетных позициях: {sumListNum}')
