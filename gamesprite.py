from const import *
from pygame import *
class Gamesprite(sprite.Sprite):
    def __init__(self, img, x, y, size):
        super().__init__()
        self.set_image(img, x, y, size)
    def draw(self, window):
        window.blit(self.image,(self.rect.x, self.rect.y))
    def drawrect(self, window):
        draw.rect(window, PINK, self.rect, 5 )
    def set_image(self, img, x, y, size):
        self.image = transform.scale(
            image.load(img),
            # здесь - размеры картинки
            size
        )
        self.mask = mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y