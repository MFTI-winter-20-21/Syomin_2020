slovar = {}
while True:
    answer = input("Вы хотите добавить новые слова[N] или поиграть?[O] ").upper()
    if answer == "N":
        data = input("Введите русский и английский вариант слова").split()
        if len(data) == 2:
            russian_word = data[0]
            english_word = data[1]
                    #Если таких слов ещё нет
            if slovar.get(russian_word) == None:
                slovar[russian_word] = english_word  #Добавляем слова в словарь
            else: #если такая пара слов уже есть в словаре
                print("Такое слово уже было")
        else: #Если было введено больше 2х значений
            print("попробуй ещё раз")
    elif answer == "0":
