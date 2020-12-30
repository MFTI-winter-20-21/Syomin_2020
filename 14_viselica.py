from random import choice
def hangman():
    print ('Время играть в виселицу')
    wordlist =['антарктида', 'видеокарта', 'процессор', 'суперархиэкстраультрамегаграндиозно', 'контрреволюция', 'продразвёрстка']
    word = choice(wordlist)
    words = 'q'
    lives = 5
    while lives > 0:
         missed = 0
         for letter in word:
             if letter in words:
                 print (letter, end=' ')
             else:
               print ('_', end=' ')
               missed= missed + 1
         if missed == 0:
             print ('\nТы выйграл!')
             break
         bukva = input('\nДавай букву: ')
         words += bukva
         if bukva not in word:
             lives -= 1
             print ('\nНеа.')
             print ('\n''ещё попыток', lives)
             if lives < 5: print ('\n  |  ')
             if lives < 4: print ('  O  ')
             if lives < 3: print (' /|\ ')
             if lives < 2: print ('  |  ')
             if lives < 1: print (' / \ ')
             if lives == 0:
                 print ('\n\nА вот и загаданное слово', word)
game_status = 'да'
while game_status == 'да':
    hangman()
    game_status = input('Хочешь сыграть ещё? (да/нет)')
