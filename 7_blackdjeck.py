import random
player_name_1 = input('Ваш ник?\n')
start_number_1 = 0 # Начальное количество очков 1 игрока
game_status_1 = True # Игровой статус первого игрока
while game_status_1:
    game_card_1 = input('Будешь брать карту? [да\нет]\n', )
    if game_card_1 == 'да':
        start_number_1 += random.randint(2, 11)
        
