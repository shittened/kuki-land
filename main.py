import pygame as pg
from screen import Screen
from keybindings import Keybindings
import sys
from map import Map
from player import Player

running = True
player_animation_timer = 0

pg.init()

screen = Screen()
map = Map()
player = Player(100, 100)

while running:
    map.Draw(screen)
    player_animation_timer = player.Animate(player_animation_timer)
    player.Draw(screen)
    screen.Update()
    running = Keybindings()

pg.quit()
sys.exit()
