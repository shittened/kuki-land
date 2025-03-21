import pygame as pg
import os
from settings import fps, resolution
import math

class Player(pg.sprite.Sprite):
    def __init__(self):
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
        self.walking_speed = 100
        self.animations = {}
        self.asset_path = 'assets/player'

    def Draw(self, screen):
        screen.screen.blit(self.image, self.rect)

    def LoadAnimations(self):
        for anim_dir in os.listdir(self.asset_path):
            animations = []
            anim_path = self.asset_path + '/' + anim_dir

            if not os.path.isdir(anim_path):
                continue

            for png in os.listdir(anim_path):
                img = pg.image.load(anim_path + '/' + png).convert_alpha()
                img = pg.transform.scale_by(img, 2)
                animations.append(img)

            self.animations[anim_dir] = animations

    def Animate(self, i, dt):
        current_animation = self.animation + '_' + self.direction

        self.image = self.animations[current_animation][math.floor(i)]

        i += dt * self.animation_speed
        if i > len(self.animations[current_animation]) - 1:
            i = 0

        return i

    def Move(self, offset, x, y, dt):
        offset[0] += (x * self.walking_speed) * dt
        offset[1] += (y * self.walking_speed) * dt

