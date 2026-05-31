from pygame import *
from const import *
from gamesprite import *
from player import *
from enemy import *
#from classes import*


def give_birth():
    rarity = Player(PONY2,30,30, P2_SIZE)
    fluttershy = Gamesprite(PONY1,(WIN_W-P1_SIZE[0])/2,WIN_H-70, P1_SIZE)
    diskord = Enemy(NEMONSTER,WIN_W-M_SIZE[0],WIN_H-200, M_SIZE)
    kluch = Gamesprite(KIUCH,WIN_W-K_SIZE[0], 10, K_SIZE)

    return(rarity, fluttershy, diskord, kluch)


font.init()
title=font.SysFont('verdana', 36)
# вынесем размер окна в константы для удобства
# W - width, ширина
# H - height, высота
# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()

# название окна
display.set_caption("Я грр, ты мне?")

# задать картинку фона такого же размера, как размер окна
background = Gamesprite(FON, 0, 0, (WIN_W,WIN_H))
walls = Gamesprite(WALLS2, 0, 0, (WIN_W,WIN_H))

rarity, fluttershy, diskord, kluch = give_birth()


record=title.render('Красавчик, но мог быстрее ',True, PINK)
i =0
game= True
finish = False
while game:
    if not finish:
        # отобразить картинку фона
        background.draw(window)
        if not diskord.run:
            kluch.draw(window)
        else:
            walls.set_image(WALLS, 0, 0, (WIN_W,WIN_H))
        walls.draw(window)
        rarity.draw(window)
        rarity.updatepony(window.get_rect(), walls)
        #rarity.drawrect(window)
        fluttershy.draw(window)
        diskord.draw(window)
        diskord.update(rarity.pos,walls,window.get_rect())

            
        if sprite.collide_rect(rarity, fluttershy):
            rarity.draw(window)
            finish = True
            
            
        
        if sprite.collide_rect(rarity, kluch):
            diskord.run=True

        if sprite.collide_rect(rarity, diskord):
            finish=True

    #         ball.speed_y *= -1
    #     if sprite.spritecollide( ball,monsters, True):
    #         ball.speed_y *= -1
    else: 
        if sprite.collide_rect(rarity, fluttershy):
            record=title.render('Красавчик ',True, PINK)
        else:
            record=title.render('Красавчик, но мог быстрее ',True, PINK)

        window.blit(record, (300,400))
        

    # слушать события и обрабатывать
    for e in event.get():
        if e.type == KEYDOWN: 
            if e.key == K_p: 
                if finish: 
                    rarity, fluttershy, diskord, kluch = give_birth()
                    finish = False
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)
