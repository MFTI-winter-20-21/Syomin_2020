import random
a = 0
number = 0
step = "g"
name = input('Привет! Как тебя зовут?')
game = random.randint(1, 100)
print ("Круто, {0}, сможешь угадать число между 1 и 100?".format(name))
while game != number:
    a += 1
    if a < 3:
        step = "крут!!"
    elif 3 < a < 6:
        step = "хорош!"
    elif 6 < a:
        step = "неплох."
    number = int(input('Введи число от 1 до 100: '))
    if 1 < number > 100:
        print(" ОТ 1 ДО 100)")
    if number < game:
        print ('Твое число меньше загаднного, смотри выше!')
    if number > game:
        print ('Твое число больше загаданного, смотри ниже!')
    if number == game:
        print ("А ты {0} Ты угадал моё число, изпользовав".format(step), a , "попыток. Тренируйся и играй больше и развей экстрасенсорные способности до максимума!")
        exit("")

