import random

print("************************")
print("~~~ Добро пожаловать ~~~")
print("************************")

name = input('Введи свой ник: ')
print("И так правила игры: в зависимоти от уровня сложности тебе нужно будет угадать трёхзначное число, на этом всё.")
uroveni = input('Ну ка, {0}, на каком уровне хочешь сыграть? лёгкий / нормальный / хардкор'.format(name))

def legk():
    print('Это реально просто, ты попросту угадываешь количество каждого разряда, то есть у числа ')
    game_status = True
    code_list = list(str(random.randint(N, K)))
    kolichestvo_popitok = 0

    while game_status:
        code_otvet = list(str(int(input("И так, ваш ответ? "))))
        if len(str(N)) <= len(code_otvet) <= len(str(K)):
            if code_otvet == code_list:
                print("Ты угадал(а) с первого раза, молодец!")

        else:
            print("Число не соответствует введённому диапозону.")
            if kolichestvo_popitok == 0:
                kolichestvo_popitok = 0
            else:
                kolichestvo_popitok -= 1


