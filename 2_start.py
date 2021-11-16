a = input("Введите текст: ").lower()
d = []
c = []

for i in a:
    if i in ['у', 'е', 'ё', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю'] or i in ['e', 'y', 'u', 'i', 'o', 'a']:
        d.append(i)
    else:
        c.append(i)

print("Всего символов: ", len(a))
print("Гласных букв: ", len(d))
print("Согласных букв :", len(c))
b = (len(d) / len(c)) * 100
if b - int(b) == 0:
    print("Процентное соотношение гласных к согласным: ", int(b))
else:
    print("Процентное соотношение гласных к согласным: ", round(b, 2))





