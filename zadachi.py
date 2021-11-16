t = int(input("Введите время записи в минутах: "))
print('Размер файла', ((t * 44100 * 2 * 24 * 60) // (8 * 1024 * 1024)) + 1, 'Мбайт')

import random
chisla = []
b = 5
while b != 0:
    chisla += list(random.randint(1, 90))
    b -= 1

