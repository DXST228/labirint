from const import *
from pygame import *
class Gamesprite(sprite.Sprite):
    def __init__(self, img, x, y, size):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            # здесь - размеры картинки
            size
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, window):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def drawrect(self, window):
        draw.rect(window, PINK, self.rect, 5 )