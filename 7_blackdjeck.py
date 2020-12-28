player_1 = 18
import random
game_start = True
game_status = True
if game_status:
    while game_status:
            if game_start:
                take_card = input("Будешь брать карту? [ДА\НЕТ]")
            if take_card == "ДА":
                player_1 += 3
                print("Теперь у тебя очков", player_1)
            elif take_card == "НЕТ":
                inGame1 = False
            else:
                print("Я тебя не понял")
            if player_1 >= 21:
                inGame1 = False
    print("Игра окончена")
    if player_1 <= 21:
        print("Ты победил! Ура!")
    else:
        print("Ты проиграл, увы")
elif game_start == "Нет":
    print("Goodbye")

