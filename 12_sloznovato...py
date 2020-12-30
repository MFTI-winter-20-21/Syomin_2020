import random
game_status = True
right_number = 0
right_placed = 0
name = input('Введи свой ник\n')
uroveni = input('Ну ка, {0}, на каком уровне хочешь сыграть? лёгкий/нормальный/хадкор\n'.format(name))
code_list = list(str(random.randint(100, 999))) # разделенное на список рандомное число
kolichestvo_popitok = 0
if uroveni == 'лёгкий':
    print('Это реально просто, сначала ты угадывааешь сотни, потом десятки и затем единицы')
    while game_status:
        code_otvet = list(str(int(input("И так, ваш ответ?\n"))))
        if len(code_otvet) == 3:
            kolichestvo_popitok += 1
            if int(code_list[0]) != int(code_otvet[0]):
                print("Не угадал, попробуй ещё раз")
            if int(code_list[0]) == int(code_otvet[0]):
                print('О! Ты угадал одну цифру!')
                while game_status:
                    code_otvet = list(str(int(input("И так, ваш ответ?\n"))))
                    kolichestvo_popitok += 1
                    if int(code_list[1]) != int(code_otvet[1]):
                        print("Не угадал, попробуй ещё раз")
                    if int(code_list[1]) == int(code_otvet[1]):
                        print('О! Ты угадал ещё одну цифру!')
                        while game_status:
                            code_otvet = list(str(int(input("И так, ваш ответ?\n"))))
                            kolichestvo_popitok += 1
                            if int(code_list[2]) != int(code_otvet[2]):
                                print("Не угадал, попробуй ещё раз")
                            if int(code_list[2]) == int(code_otvet[2]):
                                print('О! Ты угадал всё число!')
                                print('{0}, на угадывание загаданного числа у тебя ушло:'.format(name), kolichestvo_popitok, 'попыток')
                                game_status = False
        elif len(code_otvet) > 3:
            print("Это не трёхзначное число")
elif uroveni == 'нормальный':
    print('Ну тут уже без подсказок, тут пишется сколько цифр ты угадал из 3 и сколько из них правильно расположены. Посложнее так сказать')
    random_number = random.randint(100, 999)
    code = str(random_number)
    game = True
    kolichestvo_popitok_1 = 0
    while game:
        kolichestvo_popitok_1 += 1
        user_number = input("Введи трёхзначное число:\t")
        right_number = 0 #Сколько цифр угадано вообще
        right_placed = 0 #сколько цифр стоит на нужном месте
        if len(user_number) != 3:
            print('Это не трёхзначное число')
        elif not user_number.isdigit():
            print("только цифры")

        elif user_number == code:
            print("Ты угадал")
            print('{0}, на угадывание загаданного числа у тебя ушло:'.format(name), kolichestvo_popitok_1, 'попыток.')
            exit("")
        else:
            for d in code:
                if d in user_number:
                    right_number += 1

            for i in range(3):
                if user_number[i] == code[i]:
                    right_placed += 1
        print("Ты угадал вот столько цифр: {0}".format(right_number), 'из них правильно расположены {0}'.format(right_placed))
elif uroveni == 'хардкор':
    print('Значит ты выбрал смерть. У тебя всего лишь 5 попыток угадать число, затем оно меняется. Удачи!)')
    live = 5
    game_status_1 = True
    code_list_1 = list(str(random.randint(100, 999)))
    while game_status_1 and live != 0:
        user_number_1 = list(str(int(input("Введи трёхзначное число:\n"))))
        if len(user_number_1) != 3:
            print('Это не трёхзначное число')
            continue
        if user_number_1 == code_list_1:
            print("Ты угадал! {0}, у тебя осталось".format(name), live, "жизней")
            exit("")
        if user_number_1 != code_list_1:
            live -= 1
            print("Ты не угадал. У тебя осталось осталось", live, 'попыток (тки).')
    if live == 0:
        print('Ты проиграл, увы. Но к этому и надо было готовиться. Попробуй ещё раз что ли.')




