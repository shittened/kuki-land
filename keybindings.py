import pygame as pg

def Keybindings(player, offset, dt):
    running = True

    pg.event.pump()
    keys=pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False

    if keys[pg.K_a]:
        player.Move(offset, 1, 0, dt)

    if keys[pg.K_d]:
        player.Move(offset, -1, 0, dt)

    if keys[pg.K_w]:
        player.Move(offset, 0, 1, dt)

    if keys[pg.K_s]:
        player.Move(offset, 0, -1, dt)

    return running
