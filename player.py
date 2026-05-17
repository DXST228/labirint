from pygame import *
from pygame.math import Vector2
from gamesprite import *
from const import *
class Player(Gamesprite):
    def __init__(self, img, x, y, size, speed =5):
        super().__init__(img, x, y, size)
        self.speed = speed
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
            self.lastpos.y=direction.y
            direction.y-=GAZAN
        if keys[down]:
            self.lastpos.y=direction.y
            direction.y+=GAZAN
        if keys[left]:
            self.lastpos.x=direction.x
            direction.x-=GAZAN
            self.image=self.imageleft
        if keys[right] :
            self.lastpos.x=direction.x
            direction.x+=GAZAN
            self.image=self.imageright
        return direction
    
    def update(self, window_rect , up=K_w, down=K_s, left=K_a, right=K_d):
        direction = self.getdirection(up, down, left, right)
        if direction.length()>0:
            direction.normalize_ip()
            self.pos+=direction * self.speed
        self.rect.center=(self.pos.x, self.pos.y)
        
        self.rect.clamp_ip(window_rect)
        self.pos.update(self.rect.center)
    
    def collide_walls_x(self, wall):
        if sprite.collide_mask(self, wall):
            step = 1.0 if self.v.x > 0 else -1.0
            for _ in range(self.maxspeed): 
                self.pos.x -= step
                self.rect.centerx = self.pos.x
                if not sprite.collide_mask(self, wall):
                    break
                
            self.v.x = 0

    def collide_walls_y(self, wall):
        if sprite.collide_mask(self, wall):
            step = 1.0 if self.v.y > 0 else -1.0
            for _ in range(self.maxspeed): 
                self.pos.y -= step
                self.rect.centery = self.pos.y
                if not sprite.collide_mask(self, wall):
                    break
                
            self.v.y = 0

    def updatepony(self, window_rect ,wall, up=K_w, down=K_s, left=K_a, right=K_d):
        direction = self.getdirection(up, down, left, right)
        if direction.length()>0:
            direction.normalize_ip()
            self.v+=direction * self.acc
        else:
            if self.v.length_squared()>0:
                if self.v.length()<self.dec:
                    self.v = Vector2(0,0)
                else:
                    self.v -=self.v.normalize()*self.dec
        if self.v.length_squared()>self.maxspeed**2:
            self.v.scale_to_length(self.maxspeed)
        print(1,self.v)
        self.pos.x+=self.v.x
        self.rect.centerx=self.pos.x
        self.collide_walls_x(wall)
        #self.otskok_x(window_rect)
        self.pos.x+=self.v.y
        self.rect.centerx=self.pos.y
        self.collide_walls_y(wall)
        #self.otskok_y(window_rect)
        print(2,self.v)
        
        self.rect.center = (self.pos.x,self.pos.y)
        self.pos.update(self.rect.center)
    
    def otskok_x(self,window_rect):
        half_w = self.rect.width / 2

        # Отскок по X
        if self.pos.x - half_w < window_rect.left:
            self.pos.x = window_rect.left + half_w
            self.rect.centerx=self.pos.x
            self.v.x =0
        elif self.pos.x + half_w > window_rect.right:
            self.pos.x = window_rect.right - half_w
            self.rect.centerx=self.pos.x
            self.v.x = 0

    def otskok_y(self,window_rect):
        half_h = self.rect.height / 2

        # Отскок по Y
        if self.pos.y - half_h < window_rect.top:
            self.pos.y = window_rect.top + half_h
            self.rect.centery=self.pos.y
            self.v.y = 0
        elif self.pos.y + half_h > window_rect.bottom:
            self.pos.y = window_rect.bottom - half_h
            self.rect.centery=self.pos.y
            self.v.y = 0