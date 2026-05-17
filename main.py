from pygame import *
from const import *
from gamesprite import *
from player import *
#from classes import*


def give_birth():
    rarity = Player(PONY2,30,30, P2_SIZE)
    fluttershy = Gamesprite(PONY1,(WIN_W-P1_SIZE[0])/2,WIN_H-70, P1_SIZE)
    diskord = Gamesprite(NEMONSTER,WIN_W-M_SIZE[0],WIN_H-200, M_SIZE)

    return(rarity, fluttershy, diskord)


font.init()
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
walls = Gamesprite(WALLS, 0, 0, (WIN_W,WIN_H))

rarity, fluttershy, diskord = give_birth()

#record =  Card(0, 0, WIN_W, WIN_H )
#record.set_text('Красавчик, но мог быстрее ')d
game= True
finish = False
while game:
    if not finish:
        # отобразить картинку фона
        background.draw(window)
        walls.draw(window)
        rarity.draw(window)
        rarity.updatepony(window.get_rect(), walls)
        rarity.drawrect(window)
        fluttershy.draw(window)
        diskord.draw(window)
        # if sprite.collide_mask(rarity, walls):
        #     rarity.pos+=rarity.lastpos * rarity.speed          
        #     rarity.rect.center=(rarity.pos.x, rarity.pos.y)
        #     rarity.pos.update(rarity.rect.center)

        if sprite.collide_rect(rarity, fluttershy):
            rarity.draw(window)
            rarity.drawrect(window)

    #         ball.speed_y *= -1
    #     if sprite.spritecollide( ball,monsters, True):
    #         ball.speed_y *= -1
    # else: 
    #     pass
        #record.draw(window)
        

    # слушать события и обрабатывать
    for e in event.get():
        if e.type == KEYDOWN: 
            if e.key == K_p: 
                if finish: 
                    rarity, fluttershy = give_birth()
                    finish = False
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)
