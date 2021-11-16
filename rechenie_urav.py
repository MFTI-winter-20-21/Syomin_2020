p = int(input())
nomera = list(map(int, input().split()))
znachenie, nomer = map(int, input().split())
nomera.insert(znachenie, nomer)
i = 0
print(nomera)


while i <= (len(nomera) - 2):
    # Сортировка одинаковых значений
    if nomera[i] == nomera[i + 1]:
        nomera[i] += 1
        nomera.pop(i + 1)
        print("1", nomera)
    elif nomera[i - 1] == nomera[i]:
        nomera[i] += 1
        nomera.pop(i - 1)
        print("2",nomera)
    elif nomera[i-1] == nomera[i] == nomera[i+1]:
        nomera[i] += 2
        nomera.pop(i - 1)
        nomera.pop(i + 1)
        print("3",nomera)
    # Сортировка крайних значений
    elif nomera[0] == nomera[len(nomera) - 1]:
        nomera[0] += 1
        nomera.pop(len(nomera) - 1)
        print("4",nomera)
    else:
        i += 1
print(nomera)

if len(nomera) > 1:
    if nomera[0] == nomera[1] == nomera[-1] == nomera[-2]:
        nomera.pop(1)
        nomera.pop(-1)
        nomera.pop(-1)
        nomera[0] += 3
        print("5",nomera)

    elif nomera[0] == nomera[-1] == nomera[-2]:
        nomera.pop(-1)
        nomera.pop(-1)
        nomera[0] += 2
        print("5",nomera)

    elif nomera[0] == nomera[1] == nomera[-1]:
        nomera.pop(1)
        nomera.pop(-1)
        nomera[0] += 2
        print("6",nomera)

    elif nomera[0] == nomera[len(nomera) - 1]:
        nomera[0] += 1
        nomera.pop(len(nomera) - 1)
        print("7",nomera)

    elif nomera[len(nomera) - 2] == nomera[len(nomera) - 1]:
        nomera[len(nomera) - 2] += 1
        nomera.pop(len(nomera) - 1)
        print("8",nomera)

    print(nomera)
    print(len(nomera))

else:
    print(nomera)
    print(len(nomera))
