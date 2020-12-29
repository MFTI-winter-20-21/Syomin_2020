korzina = []
magazine = True
while magazine:
    status = int(input('Вы хотите добавить продукт в список [1], удалить [2], посмотреть весь список [3], купить [4]',))
    if status == 1:
        deistvie_1 = input('Что нужно добавить? (1 продукт за 1 запрос)',)
        korzina.append(deistvie_1)
    elif status == 2:
        print(korzina)
        deistvie_2 = int(input('Что нужно убрать? (1 продукт за 1 запрос). Отсчёт начинать с 0',))
        korzina.pop(deistvie_2)
    elif status == 3:
        print(korzina)
    elif status == 4:
        print("С вас 100 рублей")
        magazine = False
    else:
        print("Я вас не понял")






