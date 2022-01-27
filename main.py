import json
import os

from shelves import Shelves

BACK_TEXT = "\033[95m" + "Натисніть Enter щоб повернутись в меню" + "\033[0m"
UNAVAILABLE_TEXT = "Такого препарату немає!"


def createBaseData():
    for i in range(len(templates["shelves"])):
        shelf = Shelves()
        shelf.setId(i)
        shelf.setData(templates["shelves"]["shelf"+str(i)])
        shelves[i] = shelf


def insertNewDrug():
    shelfNumber = int(
        input('\033[32m' + "Вкажіть полицю, на якій будуть медикаменти: " + '\033[0m'))
    if shelfNumber > 6 or int(shelfNumber) < 1:
        print()
        print("Такої полиці немає!")
        return

    title = input('\033[32m' + "Введіть назву: " + '\033[0m')
    price = int(input('\033[32m' + "Введіть ціну: " + '\033[0m'))
    againstDiseases = input(
        '\033[32m' + "Введіть симптоми, які усуває/призначенння: " + '\033[0m')
    count = int(input('\033[32m' + "Введіть наявну кількість: " + '\033[0m'))
    expiriationDate = int(
        input('\033[32m' + "Вкажіть строк придатності: " + '\033[0m'))
    instruction = input('\033[32m' + "Введіть інструкцію: " + '\033[0m')
    pol = "shelf" + str(shelfNumber-1)

    for i in range(len(shelves)):
        isAval = shelves[i].isAvailable(title)
        if (isAval[0] == True):
            del templates["shelves"]["shelf"+str(i)][isAval[1]]

    templates["shelves"][pol].append({
        "title": title,
        "price": price,
        "againstDiseases": againstDiseases,
        "count": count,
        "expiriationDate": expiriationDate,
        "instruction": instruction
    })

    rewrite = json.dumps(templates, ensure_ascii=False, indent=4)
    a = open('shelves.json', 'w', encoding='utf-8')
    a.write(rewrite)
    a.close()

    print()
    print("Препарат успішно додано.")


def deleteDrug():
    title = input('\033[32m' + "Введіть назву: " + '\033[0m')
    for i in range(len(shelves)):
        isAval = shelves[i].isAvailable(title)
        if (isAval[0] == True):
            del templates["shelves"]["shelf"+str(i)][isAval[1]]
            rewrite = json.dumps(templates, ensure_ascii=False, indent=4)
            a = open('shelves.json', 'w', encoding='utf-8')
            a.write(rewrite)
            a.close()
            print()
            print("Препарат успішно видалено.")
            return
    print()
    print("Такого препарату немає.")


def printMenu():
    print("/--------------------------------\\")
    print('\033[31m' + '| Програма "Помічник фармацевта" |' + '\033[0m')
    print("\\--------------------------------/")
    print()
    print('\033[36m' + "============= Меню ==============" + '\033[0m')
    print()
    print("1. Знайти медикаменти на полиці")
    print("2. Сортувати медикаменти в алфавітному порядку")
    print("3. Пошук медикаментів за призначенням")
    print("4. Дізнатися ціну медикаментів")
    print("5. Список медикаментів, які необхідно замовити")
    print("6. Список медикаментів, які необхідно утилізувати")
    print("7. Вивести інструкцію заданих медикаментів")
    print("8. Додати медикаменти в базу даних")
    print("9. Видалити медикаменти з бази даних")
    print("10. Про програму")
    print("0. Вихід")
    print()
    print('\033[36m' + "=================================" + '\033[0m')
    print()


def returnToMenu():
    print()
    print(BACK_TEXT)
    input()
    os.system("cls")
    printMenu()
    selectMenu()


def selectMenu():
    i = 0
    j = 0
    s = input('\033[32m' + "Оберіть пункт меню -> " + '\033[0m')
    if s == "0":
        print("Програму завершено.")
        exit()

    if s == "10":
        os.system("cls")
        print('\033[36m' + "============ Про програму ============" + '\033[0m')
        print()
        print("Розробив: Цегольник Владислав Вадимович")
        print("          група КН-Б21_д/122_2_в")
        print("          2021 рік")
        print()
        print("Версія: 1.0.0")
        returnToMenu()

    if s == "1":
        os.system("cls")
        print(
            '\033[36m' + "============ Знайти медикаменти на полиці ============" + '\033[0m')
        print()
        name = input('\033[32m' + "Введіть назву препарату: " + '\033[0m')
        isAval = False

        for i in range(len(shelves)):
            isAval = shelves[i].isAvailable(name)
            if (isAval[0] == True):
                print()
                print(name + " лежить на полиці",
                      i + 1, "у відділі", isAval[1] + 1)
                break

        if (isAval[0] == False):
            print()
            print(UNAVAILABLE_TEXT)

        returnToMenu()

    if s == "2":   
        array = []
        os.system("cls")
        print(
            '\033[36m' + "============ Список медикаментів в алфавітному порядку ============" + '\033[0m')
        print()
        for i in range(len(shelves)):
            array = shelves[i].sortArray(array)
        array = sorted(array)
        for i in range(len(array)):
            print(array[i])
        returnToMenu()

    if s == "3": 
        os.system("cls")
        print(
            '\033[36m' + "============ Пошук медикаментів за призначенням ============" + '\033[0m')
        print()
        name = input(
            '\033[32m' + "Введіть симптом, який усуває медикамент, щоб почати пошук: " + '\033[0m')

        for i in range(len(shelves)):
            isAval = shelves[i].findByDescription(name)
            if(isAval != None): 
                print()
                print(" Назва:", isAval['title'], "\n", "Ціна:",
                      isAval['price'], "грн\n", "Кількість:", isAval['count'], "\n" + '\033[0m')
                j += 1
        if (j == 0): 
            print()
            print("Нічого не знайдено!")

        returnToMenu()

    if s == "4": 
        os.system("cls")
        print(
            '\033[36m' + "============ Дізнатися ціну медикаментів ============" + '\033[0m')
        print()
        name = input('\033[32m' + "Введіть назву препарату: " + '\033[0m')
        isAval = False

        for i in range(len(shelves)):
            isAval = shelves[i].isAvailable(name)
            if (isAval[0] == True):
                print()
                print("Ціна:", isAval[2], "грн")
                break

        if (isAval[0] == False):
            print()
            print(UNAVAILABLE_TEXT)
        returnToMenu()

    if s == "5": 
        os.system("cls")
        print(
            '\033[36m' + "============ Список медикаментів, які необхідно замовити ============" + '\033[0m')
        print()
        for i in range(len(shelves)):
            isMore = shelves[i].needMore()
            if(isMore[0] == True):
                for j in range(len(isMore[1])):
                    if(j % 2 == 0):
                        print(isMore[1][j], end=" - ",)
                    else:
                        print(isMore[1][j], "одиниць")
        if (isMore[0] == False):
            print(
                "Усіх медикаментів в достатній кількості. Замовляти нічого не потрібно.")
        returnToMenu()

    if s == "6":
        os.system("cls")
        print(
            '\033[36m' + "============ Список медикаментів, які необхідно утилізувати ============" + '\033[0m')
        print()
        for i in range(len(shelves)):
            isUtilize = shelves[i].needUtilize()
            if(isUtilize[0] == True):
                for j in range(len(isUtilize[1])):
                    print(isUtilize[1][j])
        if (isUtilize[0] == False):
            print(
                "Усі медикаменти ще можна використовувати. Нічого утилізувати не потрібно.")
        returnToMenu()

    if s == "7": 
        os.system("cls")
        print(
            '\033[36m' + "============ Дізнатися інструкцію медикаментів ============" + '\033[0m')
        print()
        name = input('\033[32m' + "Введіть назву препарату: " + '\033[0m')
        isAval = False

        for i in range(len(shelves)):
            isAval = shelves[i].isAvailable(name)
            if (isAval[0] == True):
                print()
                print("Інструкція:", isAval[3])
                break

        if (isAval[0] == False):
            print()
            print(UNAVAILABLE_TEXT)
        returnToMenu()

    if s == "8":  
        os.system("cls")
        print(
            '\033[36m' + "============ Додати медикаменти до бази даних ============" + '\033[0m')
        print()
        insertNewDrug()
        returnToMenu()

    if s == "9":  
        os.system("cls")
        print(
            '\033[36m' + "============ Видалити медикаменти з бази даних ============" + '\033[0m')
        print()
        deleteDrug()
        returnToMenu()

    else:  
        os.system("cls")  
        printMenu()
        selectMenu()  


with open('shelves.json', 'r', encoding='utf-8') as f:
    templates = json.load(f)
    shelves = list(range(len(templates["shelves"])))

createBaseData()
os.system("cls")
printMenu()
selectMenu()
