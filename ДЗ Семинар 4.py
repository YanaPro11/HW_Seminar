# Задача 22
# n=int(input("Введите количество элементов первого множества:"))
# m=int(input("Введите количество элементов второго множества:"))
# n_list=[]
# m_list=[]
# for i in range(n):
#     n_list.append(int(input(f"Введите элемент № {i+1} первого множества:")))
# for i in range(m):
#     m_list.append(int(input(f"Введите элемент № {i+1} второго множества:")))
# mn_list=[]
# for i in set(n_list):
#     if i in set(m_list):
#         mn_list.append(i)
# print(sorted(mn_list))

# Задача 24
# n = int(input("Введите количество кустов:"))
# count_berries = []
# for i in range(n):
#     count = int(input(f"Введите количество ягод на кусте №{i + 1}:"))
#     count_berries.append(count)
# print(count_berries)
# summa = 0
# medium_summa = 0
# for i in range(1, n):
#     try:
#         medium_summa = count_berries[i - 1] + count_berries[i] + count_berries[i + 1]
#     except IndexError:
#         medium_summa = count_berries[i - 1] + count_berries[i] + count_berries[0]
#     if medium_summa > summa:
#         summa = medium_summa
# print(f"Максимальная сумма ягод:{summa}")
