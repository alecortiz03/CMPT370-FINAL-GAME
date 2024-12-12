# CMPT 370 - GROUP 2
# DoomEngine: A simple Doom-like game engine using Pygame

from WadData import WADData
from Settings import *
import pygame as pg
import sys
from MapRender import MapRenderer
from Player import Player
from BSP import BSP
from SegmentHandler import SegHandler
from ViewRender import ViewRender

class DoomEngine:
    def __init__(self, wad_path='Environment/DOOM.WAD'):
        self.wad_path = wad_path
        self.screen = pg.display.set_mode(WIN_RES)  # Initialize the game screen
        self.clock = pg.time.Clock()  # Initialize the game clock
        self.running = True  # Game running state
        self.dt = 1 / 60  # Delta time for frame rate control
        self.on_init()  # Initialize game components

    def on_init(self):
        self.wad_data = WADData(self, map_name='E1M1')  # Load WAD data
        self.map_renderer = MapRenderer(self)  # Initialize map renderer
        self.player = Player(self)  # Initialize player
        self.bsp = BSP(self)  # Initialize BSP (Binary Space Partitioning)
        self.seg_handler = SegHandler(self)  # Initialize segment handler
        self.view_render = ViewRender(self)  # Initialize view renderer

    def update(self):
        self.player.update()  # Update player state
        self.seg_handler.update()  # Update segment handler
        self.bsp.update()  # Update BSP
        self.dt = self.clock.tick()  # Update delta time
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')  # Update window caption with FPS

    def draw(self):
        pg.display.flip()  # Update the full display Surface to the screen
        self.screen.fill('black')  # Clear the screen with black color
        self.map_renderer.draw()  # Draw the map

    def check_events(self):
        for e in pg.event.get():  # Process all events
            if e.type == pg.QUIT:  # If the quit event is triggered
                self.running = False  # Stop the game

    def run(self):
        while self.running:  # Main game loop
            self.check_events()  # Check for events
            self.update()  # Update game state
            self.draw()  # Draw everything
        pg.quit()  # Quit Pygame
        sys.exit()  # Exit the program

if __name__ == '__main__':
    doom = DoomEngine()  # Create an instance of DoomEngine
    doom.run()  # Run the game
