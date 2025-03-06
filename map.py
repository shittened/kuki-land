import pygame as pg
from ground import Ground
import random

class Map:
    def __init__(self):
        self.start_x = random.randint(-5, 5)
        self.start_y = random.randint(-3, 3)
        self.width = random.randint(15, 25)
        self.height = random.randint(10, 15)

    def Draw(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                ground = Ground(i, j)
                ground.rect.move(self.start_x, self.start_y)
                screen.screen.blit(ground.image, ground.rect)
