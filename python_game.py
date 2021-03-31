'''
создать окно *
создать персонажа *
обеспечить ему передвижение и прыжок *
придать объекту рисовку и украсить программу
дописать стрельбу
'''

import pygame

pygame.init()  # запуск библеотеки
win = pygame.display.set_mode((500, 500))  # создание окна

pygame.display.set_caption("Рандомная игруха питон")  # название игры

walkRight = [pygame.image.load('pygame_right_1.png'), pygame.image.load('pygame_right_2.png'), pygame.image.load('pygame_right_3.png'), pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'), pygame.image.load('pygame_right_6.png')]

walkLeft = [pygame.image.load('pygame_left_1.png'), pygame.image.load('pygame_left_2.png'), pygame.image.load('pygame_left_3.png'), pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'), pygame.image.load('pygame_left_6.png')]


bg = pygame.image.load('pygame_bg.jpg')
playerStand = pygame.image.load('pygame_idle.png')

clock = pygame.time.Clock()


x = 50  # начальная координата персонажа по х
y = 430  # начальная координата персонажа по у
height = 60  # высота персонажа
width = 71  # ширина персонажа
speed = 5   # скорость персонажа

isJump = False  # Прыгает сейчас персонаж или нет
jumpCount = 10  # Переменная для прыжка

left = False  # идёт ли персонаж влево
right = False  # идет ли персонаж вправо
animCount = 0  # счётчик

def drawWindow():
    global animCount

    win.blit(bg, (0, 0))  # закрашивание пред. позиции объекта

    if animCount >= 30:  #
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif left:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    pygame.display.update()  # обновление сцены игры

play = True
while play:  # цикл для работы игры
    clock.tick(30)  # внутриигровая задержка

    for event in pygame.event.get():  # цикл для перебора введенных данных
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()  # список для внесение в него нажатых клавиш
    if keys[pygame.K_RIGHT] and x < 500 - width - speed:  # обработка условий нажатых клавиш + границы карты
        x += speed
        right = True
        left = False
    elif keys[pygame.K_LEFT] and x > speed:  # обработка условий нажатых клавиш + границы карты
        x -= speed
        right = False
        left = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):  # прыгает сейчас персонаж или нет
        if keys[pygame.K_SPACE]:
            isJump = True
    else:  # формула прыжка
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pygame.quit()

