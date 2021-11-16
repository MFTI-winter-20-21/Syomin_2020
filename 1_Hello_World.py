a = input("Введите 1-е число: ")
b = input("Введите 2-е число: ")
c = input("Введите 3-е число: ")

while True:
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        break
    except:
        print("Неверный ввод")
        a = input("Введите 1-е число: ")
        b = input("Введите 2-е число: ")
        c = input("Введите 3-е число: ")

nod = [a, b, c]
nod.sort()

if nod[1] - int(nod[1]) != 0:
    print("Среднее между введёнными числами:", nod[1])
else:
    print("Среднее между введёнными числами:", int(nod[1]))
