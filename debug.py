import pygame as pg
from settings import show_fps
from fonts import font_20

def Debug(screen):
    if show_fps:
        FPS(screen)

def FPS(screen):
    fps_text = font_20.render('FPS: ' + str(int(screen.fps)), False, (255, 255, 255))
    screen.screen.blit(fps_text, (10, 10))

