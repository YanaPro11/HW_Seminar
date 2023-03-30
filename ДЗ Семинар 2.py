# Задача 10
# import random
#
# n = int(input("Введите количество монеток:"))
# coins = []
# for m in range(n):
#     coins.append(random.randint(0, 1))
# zero = coins.count(0)
# unit = coins.count(1)
# if zero < unit:
#     print("Нужно перевернуть", zero)
# elif unit<zero:
#     print("Нужно перевернуть", unit)
# else:
#     print("Количество монет с решкой и орлом одиннаковое.Нужно перевернуть",zero)
# print(coins)

# Задача 12
# s=int(input("Введите сумму чисел:"))
# p=int(input("Введите произведение чисел:"))
# for x in range(s):
#     for y in range(s):
#         if x+y==s and x*y==p:
#             print("Петя загадал числа:",x,y)

# Задача 14
# n=int(input("Введите число N:"))
# k=0
# result=1
# while result<=n:
#     print(result)
#     k+=1
#     result=2**k

