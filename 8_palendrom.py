word = input("Ваше слово?")
test = word[::-1]
if word == test:
    print("Это определённо палиндроп")
else:
    print("Обычное слово")
