import pygame, sys
from settings import *
from tiles import Tile
from level import Level
# Pygame setup
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.ext()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
