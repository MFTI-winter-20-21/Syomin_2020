'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

print([i for i in a if i in b])

for i in a:
    if i in b:
        c.append(i)
print(c)
'''

nominals = [100, 5000, 2000, 1000, 200, 500]
def calc_banknotes( amount ):

    ret = {}
    amount_float = int(amount)
    if amount_float < 0:
        raise Exception('Некорректная сумма')
    if amount_float % min(nominals) > 0:
        raise Exception('В банкомате отсутствуют купюры нужного номинала')
    noms = nominals.copy()
    noms.sort(reverse=True)
    remains = amount_float
    for nominal in noms:
        num_banknotes = remains // nominal
        remains -= num_banknotes * nominal
        if num_banknotes > 0:
            ret[nominal] = num_banknotes
    return ret

# сумма
summ = input("Введите сумму: ")
try:
    banknotes = calc_banknotes( summ )
    print("К выдаче:")
    for nominal in banknotes:
        print(f"Купюр номинала {nominal}: {banknotes[nominal]}")
except ValueError:
    print("Некорректные данные")
except Exception as e:
    print(e.args[0])
