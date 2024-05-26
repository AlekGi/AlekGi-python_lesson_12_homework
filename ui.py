from logger import input_data, showContacts, findContact, changeContact, deleteContact

def interface():  # Функция рисования интерфейса главного меню
    print("Добро пожаловать в интерактивный справочник GeekBrains!")
    print("=" * 26)
    print(" [1] -- Показать справочник")
    print(" [2] -- Добавить запись")
    print(" [3] -- Найти запись")
    print(" [4] -- Изменить контакт")
    print(" [5] -- Удалить контакт")
    print("\n [0] -- Выход")
    print("=" * 26)
    
    
def main():  # Функция реализации главного меню    
    while True:
        interface()
        userChoice = int(input("Введите номер команды или нажмите 0 для выхода: "))

        if userChoice == 1:
            showContacts()
        elif userChoice == 2:
            input_data()
        elif userChoice == 3:
            findContact()
        elif userChoice == 4:
            changeContact()
        elif userChoice == 5:
            deleteContact()
        elif userChoice == 0:
            print("Спасибо!")
            return