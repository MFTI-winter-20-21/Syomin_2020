slova = []
a = int(input("Сколько слов вы хотите проверить?", ))
while a != 0:
    new = input("Ваше слово? Все слова писать маленькими буквами", )
    if new == new[::-1]:
        slova.append(new)
    a -= 1
print("все эти слова палиндропы", slova)
