import functions

while True:
    print(("1. вывод, 2. добавление, 3. поиск,4.изменение, 5.удаление"))
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.change_data()
    elif mode == 5:
        functions.delete_data()
    else:
        break