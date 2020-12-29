import random
simvols = list('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
kolichestvo_simbols = int(input('длина пароля?\n', ))
lenght = 8
parol = ''
while lenght != 0:
    a = random.randint(0, 50)
    parol += simvols[random.randint(0, 70)]
    lenght -= 1
print(parol)
