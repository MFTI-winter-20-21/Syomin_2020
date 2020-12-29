slova = input('Какте слова вы хотите проверить?').lower().split()
palindrops = []
for word in slova:
    if word == word[::-1]:
        palindrops.append(word)
if len(palindrops) <= 0:
    print('Падиндропов не обнаруженно')
else:
    print("А вот и падиндропы", ', '.join(palindrops))


