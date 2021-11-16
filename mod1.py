print(' '.join([str(x) for x in [i for i in range(1, 6)] if x % 2 != 0]))
print()
print([x * str(x) for x in range(1, 5)])
print()
print(' '.join([x * str(x) for x in range(12)]))

t1 = 20.37
t2 = 20.15
t3 = 20.25
t4 = 20.41
t5 = 20.46
n = 5
tsr = (t1+t2+t3+t4+t5) / n
dtsr = (abs(t1 - tsr) + abs(t2 - tsr) + abs(t3 - tsr) + abs(t4 - tsr) + abs(t5 - tsr)) / n
print("Среднее время экспермента:", tsr)
print("Абсолютная погрешность:", dtsr)
print("Относительная погрешность времени:", dtsr/tsr)
print("Относительная погрешность длины маятника:", 0.001/1.01)
print("Относительная погрешность ускорения:", 2*(dtsr/tsr) + 1*(0.001/1.01))
print("Ускорение", (4*(3.14**2)*1.01*(10**2))/(tsr**2))
print("Дельта g", ((4*(3.14**2)*1.01*(10**2))/(tsr**2))*(2*(dtsr/tsr) + 1*(0.001/1.01)))


