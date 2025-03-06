import pygame as pg

def Keybindings():
    running = True

    pg.event.pump()
    keys=pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False

    return running
