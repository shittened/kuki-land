import pygame as pg
from settings import resolution, fps, vsync, fullscreen

class Screen:
    def __init__(self):
        if fullscreen:
            tags = pg.FULLSCREEN
        else:
            tags = None

        self.screen = pg.display.set_mode(resolution, tags, vsync)
        self.clock = pg.time.Clock()

    def Update(self):
        self.clock.tick(fps)
        pg.display.flip()

