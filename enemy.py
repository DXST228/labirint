from pygame import *
from pygame.math import Vector2
from gamesprite import *
from const import *
class Enemy(Gamesprite):
    def __init__(self, img, x, y, size, speed =3):
        super().__init__(img, x, y, size)
        self.speed = speed
        self.run = False
        self.acc = 0.15
        self.dec = 0.3
        self.maxspeed = 5
        self.v = Vector2(0,0)
        self.pos = Vector2(x,y)
        self.lastpos=self.pos
        self.imageleft=self.image
        self.imageright=transform.flip(self.image, True, False)
    def getdirection(self, up=K_w, down=K_s, left=K_a, right=K_d):
        keys = key.get_pressed()
        direction = Vector2(0,0)
        if keys[up]:
            direction.y-=GAZAN
        if keys[down]:
            direction.y+=GAZAN
        if keys[left]:
            direction.x-=GAZAN
            self.image=self.imageleft
        if keys[right] :
            direction.x+=GAZAN
            self.image=self.imageright
        return direction
    
    def collide_walls_x(self, wall):
        if sprite.collide_mask(self, wall):
            step = 1.0 if self.v.x > 0 else -1.0
            # Откатываем назад по 1 пикселю, пока коллизия не исчезнет
            for _ in range(int(abs(self.v.x)) + 3):
                if not sprite.collide_mask(self, wall):
                    break
                self.pos.x -= step
                self.rect.centerx = int(self.pos.x)
    
    def collide_walls_y(self, wall):
        if sprite.collide_mask(self, wall):
            step = 1.0 if self.v.y > 0 else -1.0
            for _ in range(int(abs(self.v.y)) + 3):
                if not sprite.collide_mask(self, wall):
                    break
                self.pos.y -= step
                self.rect.centery = int(self.pos.y)

    def update(self, player_pos, walls, window_rect):
        if not self.run: return
        

        direction = Vector2(player_pos)- self.pos
        distance = direction.length()
        if distance < 15:
            return
        direction.normalize_ip()

        movex=direction.x*self.speed
        self.pos.x += movex
        self.rect.centerx = int(self.pos.x)
        self.collide_walls_x(walls)

        movey=direction.y*self.speed
        self.pos.y += movey
        self.rect.centery = int(self.pos.y)
        self.collide_walls_y(walls)

        self.rect.clamp_ip(window_rect)
        self.pos.x,self.pos.y=self.rect.center
    