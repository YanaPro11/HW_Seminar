# Задача 16
# n = int(input("Введите количество элементов в массиве:"))
# a = []
# for m in range(1, n + 1):
#     a.append(m)
# print(a)
# x= int(input("Введите число:"))
# print(a.count(x))

# Задача 18
# n = int(input("Введите количество элементов в массиве:"))
# a = []
# for m in range(1, n + 1):
#     a.append(m)
# print(a)
# x = int(input("Введите число:"))
# if x > max(a):
#     print(max(a))
# elif x < min(a):
#     print(min(a))
# else:
#     for i in range(len(a)):
#         if a[i] == x:
#             if a[i] == min(a):
#                 print(a[i + 1])
#             elif a[i] == max(a):
#                 print(a[i - 1])
#             else:
#                 print(a[i - 1], a[i + 1])

# Задача 20
# scrabble = {
#     1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
#     2: ["D", "G", "Д", "К", "Л", "М", "П", "У"],
#     3: ["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"],
#     4: ["F", "H", "V", "W", "Y", "Й", "Ы"],
#     5: ["K", "Ж", "З", "Х", "Ц", "Ч"],
#     8: ["J", "X", "Ш", "Э", "Ю"],
#     10: ["Q", "Z", "Ф", "Щ", "Ъ"]
# }
# word=input("Введите слово:").upper()
# summa=0
# for letter in word:
#     for key,value in scrabble.items():
#         # if letter in value:
#             summa+=key
#             break
# print(summa)


