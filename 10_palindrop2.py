'''
slova = input('Какие слова вы хотите проверить?\n').lower().split()
palindrops = []
for word in slova:
    if word == word[::-1]:
        palindrops.append(word)
if len(palindrops) <= 0:
    print('Палиндропов не обнаруженно')
else:
    print("А вот и падиндропы:", ', '.join(palindrops))
'''




def vkl(A,b,c):
    A[c-1]=b
    return A

print(vkl([1, 2, 3, 4, 5], 'qwe', 5))










