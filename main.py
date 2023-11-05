import pygame, sys
from settings_map import *
from level import Level
from menu import menu
from game_state import GameState

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
game_state = GameState()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    if game_state.state == "MENU":
        menu(screen, game_state)
    elif game_state.state == "LEVEL":
        level.run()

    pygame.display.update()
    clock.tick(60)