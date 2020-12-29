import random
simvols = list('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
kolichestvo_simbols = int(input('длина пароля?\n', ))
lenght = 8
parol = ''
while lenght != 0:
    parol += simvols[random.randint(0, 76)]
    lenght -= 1
print(parol)
