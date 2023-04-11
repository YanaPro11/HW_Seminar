Задача 34
# poem=input("Введите стихотворение:")
# poem_list=poem.split()
# count_vowel_letters=[]
# for phrase in poem_list:
#     summa=0
#     for letter in phrase:
#         if letter in "аеёиоуыэюя":
#             summa+=1
#     count_vowel_letters.append(summa)
# if len(set(count_vowel_letters))==1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# Задача 36
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows+1):
#         for j in range(1, num_columns + 1):
#             print(operation(i,j), end="\t")
#         print()
# print_operation_table(lambda x, y: x * y)