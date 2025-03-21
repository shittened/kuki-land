import pygame as pg
from ground import Ground
import random

class Map:
    def __init__(self):
        self.start_x = random.randint(-5, 5)
        self.start_y = random.randint(-3, 3)
        self.width = random.randint(15, 25)
        self.height = random.randint(10, 15)
        self.ground_group = pg.sprite.Group()
        self.prob_1 = 20
        self.prob_2 = 70

        for i in range(self.height):
            #left edge
            probability = random.randint(1, 100)
            if probability > self.prob_1:
                ground = Ground(self.start_x - 1, i + self.start_y)
                self.ground_group.add(ground)
            if probability > self.prob_2:
                ground = Ground(self.start_x - 2, i + self.start_y)
                self.ground_group.add(ground)

            #right edge
            probability = random.randint(1, 100)
            if probability > self.prob_1:
                ground = Ground(self.start_x + self.width, i + self.start_y)
                self.ground_group.add(ground)
            if probability > self.prob_2:
                ground = Ground(self.start_x + self.width + 1, i + self.start_y)
                self.ground_group.add(ground)

        for i in range(self.width):
            #top edge
            probability = random.randint(1, 100)
            if probability > self.prob_1:
                ground = Ground(i + self.start_x, self.start_y - 1)
                self.ground_group.add(ground)
            if probability > self.prob_2:
                ground = Ground(i + self.start_x, self.start_y - 2)
                self.ground_group.add(ground)

            #bottom edge
            probability = random.randint(1, 100)
            if probability > self.prob_1:
                ground = Ground(i + self.start_x, self.start_y + self.height)
                self.ground_group.add(ground)
            if probability > self.prob_2:
                ground = Ground(i + self.start_x, self.start_y + self.height + 1)
                self.ground_group.add(ground)

        #middle
        for i in range(self.width):
            for j in range(self.height):
                ground = Ground(i + self.start_x, j + self.start_y)
                self.ground_group.add(ground)

    def Draw(self, screen, offset):
        self.ground_group.update(offset)
        self.ground_group.draw(screen.screen)
