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
        z = [1]*b
        for i in c:
            z[c.index(i)] = i
        z.append(a)
        print(z)

    else:
        z = []
        if b == 0:
            z.append(a)
            for i in c:
                z.append(i)
        elif b == 1:
            z.append(c[0])
            z.append(a)
            for i in c[1:len(c)]:
                z.append(i)
        else:
            for i in c[0:b]:
                z.append(i)
            z.append(a)
            for i in c[b:len(c)]:
                z.append(i)
        print(z)
