import pygame as pg
from screen import Screen
from keybindings import Keybindings
import sys
from map import Map
from player import Player
from debug import Debug

class Game:
    def __init__(self):
        self.running = True
        self.player_animation_timer = 0
        self.offset = [0, 0]

        pg.init()

        self.screen = Screen()
        self.map = Map()
        self.player = Player()
        self.player.LoadAnimations()

    def Run(self):
        while self.running:
            self.screen.screen.fill('blue')
            self.map.Draw(self.screen, self.offset)
            self.player_animation_timer = self.player.Animate(self.player_animation_timer, self.screen.dt)
            self.player.Draw(self.screen)
            Debug(self.screen)
            self.screen.Update()
            self.running = Keybindings(self.player, self.offset, self.screen.dt)

        pg.quit()
        sys.exit()

game = Game()

game.Run()
