a = input("Введите элемент который вы хотите добавить: ")
b = int(input("Введите номер места, на которое вы хотите его поставить: "))

c = [i for i in range(0, 15)]

def spis(a, b, c):
    if len(c) < b:
        z = [0]*(b-1)
        for i in c:
            z[c.index(i)] = i
        z.append(a)
        print(z)

    elif len(c) == b:
        z = []
        for i in c[0:len(c)-1]:
            z.append(i)
        z.append(a)
        z.append(c[len(c) - 1])
        print(z)

    else:
        z = []
        if b == 0:
            z.append(a)
            for i in c:
                z.append(i)

        else:
            for i in c[0:b-1]:
                z.append(i)
            z.append(a)
            for i in c[b-1:len(c)]:
                z.append(i)
        print(z)
