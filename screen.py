import pygame as pg
from settings import resolution, fps, vsync, fullscreen

class Screen:
    def __init__(self):
        if fullscreen:
            tags = pg.FULLSCREEN
        else:
            tags = 0

        self.screen = pg.display.set_mode(resolution, tags, vsync)
        self.clock = pg.time.Clock()
        self.fps = fps
        self.dt = 0

    def Update(self):
        self.clock.tick(fps)
        pg.display.flip()
        self.fps = self.clock.get_fps()
        if self.fps != 0:
            self.dt = 1 / float(self.fps)

