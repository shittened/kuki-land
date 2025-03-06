import pygame as pg

class Ground(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/ground/grass.png').convert()
        self.image = pg.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * self.rect.width, y * self.rect.height)
