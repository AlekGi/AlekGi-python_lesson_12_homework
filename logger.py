
from data_create import name_data, surname_data, phone_data

def input_data():   # Функция ввода данных
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    with open('spravochnik.txt', 'a', encoding='utf-8') as f:
            f.write(f"{name},{surname},{phone}\n")
    input("\nКонтакт успешно добавлен!\n ===Нажмите любую кнопку===")        

def print_data(data):  # Функция вывода справочника в терминал
    spravochnik = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  surname        Name          Phone Numbers")
    print(splitLine)
    personID = 1

    for contact in data:
        surname, name, phone = contact.rstrip().split(",")
        spravochnik.append(
            {
                "ID": personID,
                "surname": surname,
                "name": name,
                "phone": phone,
            }
        )
        personID += 1

    for contact in spravochnik:
        personID, surname, name, phone = contact.values()
        print(f"{personID:>2}. {surname:<15} {name:<10}  {phone:<15}")

    print(splitLine)

def showContacts():  # Функция открытия справочника
    spravochnik = []
    with open('spravochnik.txt', "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        print_data(data)
    input("\n=== Нажмите любую кнопку ===")

def findContact():  # Функция поиска
    target = input("Введите имя контакта для поиска: ")
    result = []
    with open('spravochnik.txt', "r", encoding="UTF-8") as f:
        data = f.readlines()
        for name in data:
            if target in name:
                result.append(name)

    if len(result) != 0:
        print_data(result)
    else:
        print(f"Не могу найти контакт, с именем {target}")
    input("=== Нажмите любую кнопку ===")


def changeContact():  # Функция изменения контакта
    spravochnik = []
    with open('spravochnik.txt', "r", encoding="UTF-8") as f:
        data = sorted(f.readlines())
        print_data(data)

        numberContact = int(
            input("Введите номер контакта для удаления или нажмите цифру 0 для возврата в главное меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newSurname = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый номер телефона: ")
            data[numberContact - 1] = (
                newSurname + "," + newName + "," + newPhone + "\n"
            )
            with open('spravochnik.txt', "w", encoding="UTF-8") as f:
                f.write("".join(data))
                print("\nКонтакт успешно изменен!")
                input("\n=== Нажмите любую кнопку ===")
        else:
            return
        
def deleteContact():  # Функция удаления контакта из телефонной книги
    with open('spravochnik.txt', "r+", encoding="UTF-8") as f:
        data = sorted(f.readlines())
        print_data(data)

        numberContact = int(
            input("Введите номер контакта для удаления или нажмите цифру 0 для возврата в главное меню: ")
        )
        if numberContact != 0:
            print(f"Запись удалена: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open('spravochnik.txt', "w", encoding="UTF-8") as f:
                f.write("".join(data))

        else:
            return

    input("=== Нажмите любую кнопку ===")