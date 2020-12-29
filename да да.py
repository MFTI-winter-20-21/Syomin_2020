import random
game_card_1 = "o"
game_card_2 = "g"
name_1 = input("Игрок 1 как вас зовут?",)
name_2 = input("Игрок 2 как вас зовут?",)
player_1 = random.randint(2, 11)
player_2 = random.randint(2, 11)
game_status_1 = True
game_status_2 = True
while game_status_1:
    game_card_1 = input("{0}, будете брать карту? Да/Нет".format(name_1),)
    if game_card_1 == 'Да':
        player_1 += random.randint(2, 11)
        print("{0}, ваш счёт:".format(name_1), player_1)
        game_card_2 = input("{0}, будете брать карту? Да/Нет".format(name_2), )
        if game_card_2 == 'Да':
            player_2 += random.randint(2, 11)
            print("{0}, ваш счёт:".format(name_2), player_2)
        elif game_card_2 == 'Нет':
            game_status_2 = False
        else:
            print("Я вас не понял.")
        if player_2 >= 21:
            game_status_2 = False
    elif game_card_1 == 'Нет' and game_card_2 == 'Нет':
        game_status_1 = False
    else:
        print("Я вас не понял.")
    if player_1 >= 21:
        game_status_1 = False
if player_1 <= 21 and player_1 > player_2:
    print("{0}, вы выйграли!".format(name_1))
if player_1 <= 21 and player_1 < player_2:
    print("{0}, вы выйграли!".format(name_2))
if player_1 > 21:
    print("{0}, вы проиграли!".format(name_1))
if player_2 > 21:
    print("{0}, вы проиграли!".format(name_2))
