word = input("Ваше слово?")
test = word[::-1]
if word == test:
    print("Это определённо палендроп")
else:
    print("Обычное слово")
