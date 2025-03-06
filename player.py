import pygame as pg
import os
from settings import fps, resolution
import math

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.animation = 'idle'
        self.direction = 'down'
        self.image = pg.image.load('assets/player/idle_down/0.png').convert_alpha()
        self.image = pg.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect()
        self.rect.topleft = (
                resolution[0] / 2 - self.rect.width / 2,
                resolution[1] / 2 - self.rect.height / 2
        )
        self.animation_speed = 6

    def Draw(self, screen):
        screen.screen.blit(self.image, self.rect)

    def Animate(self, i):
        path = 'assets/player/' + self.animation + '_' + self.direction
        path_len = len([img for img in os.listdir(path)])

        self.image = pg.image.load(path + '/' + str(math.floor(i)) + '.png').convert_alpha()
        self.image = pg.transform.scale_by(self.image, 2)

        i += 1 / fps * self.animation_speed
        if i > path_len - 1:
            i = 0

        return i
