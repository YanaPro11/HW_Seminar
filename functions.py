def show_data() -> None:

    with open("book.txt", "r", encoding="utf-8") as f:
        print(f.read())


def add_data() -> None:

    fio = input("Введите ФИО:")
    tel_number = input("Введите номер телефона:")
    with open("book.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{fio}| {tel_number}")
    print("Успешно!")


def find_data() -> None:

    data = input("Введите данные для поиска:")
    with open("book.txt", "r", encoding="utf-8") as f:
        tel_book = f.readlines()
    print("Результаты поиска:")
    print(search(tel_book, data))


def search(book: list, info: str) -> str:
    return "".join([post for post in book if info in post])


def change_data():
    data = input("Введите данные для поиска:")
    with open("book.txt", "r", encoding="utf-8") as f:
        tel_book = f.readlines()
    print("Результаты поиска:")
    change_info = search(tel_book, data).split("\n")
    if change_info[0] == '':
        print("Данные не найдены")
    else:
        if '' in change_info:
            for i in change_info:
                if i == '':
                    change_info.remove(i)
        for a, value in enumerate(change_info, start=1):
            print(f"{a}. {value}")

        select_contact = int(input("Введите номер контакта:"))
        new_surname = input("Введите фамилию: ")
        new_phone = input("Введите телефон: ")
        change_info[select_contact-1] = f"{new_surname}| {new_phone}"

        with open("book.txt", "w", encoding="utf-8") as f:
            for data in change_info:
                f.write(f"{data}\n")
        print("Данные успешно записаны")


def delete_data():
    data = input("Введите данные для поиска:")
    with open("book.txt", "r", encoding="utf-8") as f:
        tel_book = f.readlines()
    print("Результаты поиска:")
    change_info = search(tel_book, data).split("\n")
    if change_info[0] == '':
        print("Данные не найдены")
    else:
        if '' in change_info:
            for i in change_info:
                if i == '':
                    change_info.remove(i)
        for a, value in enumerate(change_info, start=1):
            print(f"{a}. {value}")

        select_contact = int(input("Введите номер удаляемого контакта:"))
        del change_info[select_contact-1]

        with open("book.txt", "w", encoding="utf-8") as f:
            for data in change_info:
                f.write(f"{data}\n")
        print("Данные успешно удалены")