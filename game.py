'''
a, b, c, d, f = map(int, input().split())

#a
if a + b > c and a + c > b and c + b > a and a + d > f and a + f > d and f + d > a:
    print(a)
    print(b, c)
    print(d, f)
elif a + b > d and a + d > b and d + b > a and a + c > f and a + f > c and f + c > a:
    print(a)
    print(b, d)
    print(c, f)
elif a + b > f and a + f > b and f + b > a and a + d > c and a + c > d and c + d > a:
    print(a)
    print(b, f)
    print(c, d)

#b
elif a + b > c and a + c > b and c + b > a and d + b > f and d + f > b and f + b > d:
    print(b)
    print(a, c)
    print(d, f)
elif a + b > d and a + d > b and d + b > a and c + b > f and c + f > b and f + b > c:
    print(b)
    print(a, d)
    print(c, f)
elif a + b > f and a + f > b and f + b > a and d + b > c and d + c > b and c + b > d:
    print(b)
    print(a, f)
    print(d, c)

#c
elif c + b > a and c + a > b and a + b > c and c + d > f and d + f > c and f + c > d:
    print(c)
    print(a, b)
    print(d, f)
elif c + d > a and c + a > d and a + d > c and c + b > f and b + f > c and f + c > b:
    print(c)
    print(a, d)
    print(b, f)
elif c + f > a and c + a > f and a + f > c and c + d > b and d + b > c and b + c > d:
    print(c)
    print(a, f)
    print(d, b)


#d
elif a + b > d and a + d > b and d + b > a and c + f > d and c + d > f and d + f > c:
    print(d)
    print(a, b)
    print(c, f)
elif a + c > d and a + d > c and d + c > a and b + f > d and b + d > f and d + f > b:
    print(d)
    print(a, c)
    print(b, f)
elif a + f > d and a + d > f and d + f > a and c + b > d and c + d > b and d + b > c:
    print(d)
    print(a, f)
    print(c, b)

#f
elif a + b > f and a + f > b and f + b > a and c + f > d and c + d > f and d + f > c:
    print(f)
    print(d, c)
    print(b, a)
elif a + c > f and a + f > c and f + c > a and b + f > d and b + d > f and d + f > b:
    print(f)
    print(a, c)
    print(b, d)
elif a + d > f and a + f > d and f + d > a and c + f > b and c + b > f and b + f > c:
    print(f)
    print(d, a)
    print(b, c)

else:
    print(0)

if nomera[0] == nomera[1] == nomera[-1] == nomera[-2]:
        nomera.pop(1)
        nomera.pop(-1)
        nomera.pop(-1)
        nomera[0] += 3

elif nomera[0] == nomera[1] == nomera[-1]:
        nomera.pop(1)
        nomera.pop(-1)
        nomera[0] += 2

if len(nomera) > 1:
    if nomera[0] == nomera[-1] == nomera[-2]:
        nomera.pop(-1)
        nomera.pop(-1)
        nomera[0] += 2
    elif nomera[0] == nomera[len(nomera) - 1]:
        nomera[0] += 1
        nomera.pop(len(nomera) - 1)
    elif nomera[len(nomera) - 2] == nomera[len(nomera) - 1]:
        nomera[len(nomera) - 2] += 1
        nomera.pop(len(nomera) - 1)
    print(len(nomera))
else:

'''

p = int(input())
nomera = list(map(int, input().split()))
znachenie, nomer = map(int, input().split())
nomera.insert(znachenie, nomer)
i = 0
nomera_1 = list(reversed(nomera))
while i <= (len(nomera) - 2):
    if nomera[i] == nomera[i + 1]:
        nomera[i] += 1
        nomera.pop(i + 1)
        if len(nomera) > 1 and nomera[0] == nomera[1] == nomera[-1]:
            nomera[0] += 2
            nomera.pop(1)
            nomera.pop(-1)
        elif len(nomera) > 1 and nomera[0] == nomera[-1] == nomera[-2]:
            nomera.pop(-1)
            nomera.pop(-1)
            nomera[0] += 2
    elif nomera[i-1] == nomera[i] == nomera[i+1]:
        nomera[i] += 2
        nomera.pop(i - 1)
        nomera.pop(i + 1)
        if len(nomera) > 1 and [0] == nomera[1] == nomera[-1]:
            nomera[0] += 2
            nomera.pop(1)
            nomera.pop(-1)
        elif len(nomera) > 1 and nomera[0] == nomera[-1] == nomera[-2]:
            nomera.pop(-1)
            nomera.pop(-1)
            nomera[0] += 2
    elif nomera[i - 1] == nomera[i]:
        nomera[i] += 1
        nomera.pop(i - 1)
        if len(nomera) > 1 and nomera[0] == nomera[1] == nomera[-1]:
            nomera[0] += 2
            nomera.pop(1)
            nomera.pop(-1)
        elif len(nomera) > 1 and nomera[0] == nomera[-1] == nomera[-2]:
            nomera.pop(-1)
            nomera.pop(-1)
            nomera[0] += 2
    elif nomera[0] == nomera[len(nomera) - 1]:
        nomera[0] += 1
        nomera.pop(len(nomera) - 1)
        if len(nomera) > 1 and nomera[0] == nomera[1] == nomera[-1]:
            nomera[0] += 2
            nomera.pop(1)
            nomera.pop(-1)
        elif len(nomera) > 1 and nomera[0] == nomera[-1] == nomera[-2]:
            nomera.pop(-1)
            nomera.pop(-1)
            nomera[0] += 2
    else:
        i += 1

    if i == len(nomera) - 1 and i > 1 and nomera[0] == nomera[-1]:
        i = 0
        if nomera[0] == nomera[-1] == nomera[-2]:
            nomera.pop(-1)
            nomera.pop(-1)
            nomera[0] += 2
        elif nomera[0] == nomera[len(nomera) - 1]:
            nomera[0] += 1
            nomera.pop(len(nomera) - 1)
        elif nomera[len(nomera) - 2] == nomera[len(nomera) - 1]:
            nomera[len(nomera) - 2] += 1
            nomera.pop(len(nomera) - 1)
i = 0
while i <= (len(nomera_1) - 2):
    if nomera_1[i] == nomera_1[i + 1]:
        nomera_1[i] += 1
        nomera_1.pop(i + 1)
        if len(nomera_1) > 2 and nomera_1[0] == nomera_1[1] == nomera_1[-1]:
            nomera_1[0] += 2
            nomera_1.pop(1)
            nomera_1.pop(-1)
        elif len(nomera_1) > 2 and nomera_1[0] == nomera_1[-1] == nomera_1[-2]:
            nomera_1.pop(-1)
            nomera_1.pop(-1)
            nomera_1[0] += 2
    elif nomera_1[i-1] == nomera_1[i] == nomera_1[i+1]:
        nomera_1[i] += 2
        nomera_1.pop(i - 1)
        nomera_1.pop(i + 1)
        if len(nomera_1) > 2 and [0] == nomera_1[1] == nomera_1[-1]:
            nomera_1[0] += 2
            nomera_1.pop(1)
            nomera_1.pop(-1)
        elif len(nomera_1) > 2 and nomera_1[0] == nomera_1[-1] == nomera_1[-2]:
            nomera_1.pop(-1)
            nomera_1.pop(-1)
            nomera_1[0] += 2
    elif nomera_1[i - 1] == nomera_1[i]:
        nomera_1[i] += 1
        nomera_1.pop(i - 1)
        if len(nomera_1) > 2 and nomera_1[0] == nomera_1[1] == nomera_1[-1]:
            nomera_1[0] += 2
            nomera_1.pop(1)
            nomera_1.pop(-1)
        elif len(nomera_1) > 2 and nomera_1[0] == nomera_1[-1] == nomera_1[-2]:
            nomera_1.pop(-1)
            nomera_1.pop(-1)
            nomera_1[0] += 2
    elif nomera_1[0] == nomera_1[len(nomera_1) - 1]:
        nomera_1[0] += 1
        nomera_1.pop(len(nomera) - 1)
        if len(nomera_1) > 2 and nomera_1[0] == nomera_1[1] == nomera_1[-1]:
            nomera_1[0] += 2
            nomera_1.pop(1)
            nomera_1.pop(-1)
        elif len(nomera_1) > 2 and nomera_1[0] == nomera_1[-1] == nomera_1[-2]:
            nomera_1.pop(-1)
            nomera_1.pop(-1)
            nomera_1[0] += 2
    else:
        i += 1
    if i == len(nomera_1) - 1 and i > 1 and nomera_1[0] == nomera_1[-1]:
        i = 0
        if nomera_1[0] == nomera_1[-1] == nomera_1[-2]:
            nomera_1.pop(-1)
            nomera_1.pop(-1)
            nomera_1[0] += 2
        elif nomera_1[0] == nomera_1[len(nomera_1) - 1]:
            nomera_1[0] += 1
            nomera_1.pop(len(nomera_1) - 1)
        elif nomera_1[len(nomera_1) - 2] == nomera_1[len(nomera_1) - 1]:
            nomera_1[len(nomera_1) - 2] += 1
            nomera_1.pop(len(nomera_1) - 1)

if len(nomera) < len(nomera_1):
    print(len(nomera))
elif len(nomera) == len(nomera_1):
    print(len(nomera))
else:
    print(len(nomera_1))
