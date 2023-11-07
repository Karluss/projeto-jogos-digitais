import pygame, sys
from settings_map import *
from level import Level
from menu import menu
from game_state import GameState

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
game_state = GameState()
img_background = pygame.image.load("assets\BG.png")
img = pygame.transform.scale(img_background,(screen_width, screen_height))
music_background = pygame.mixer.music.load("assets\SuperMarioBros.mp3")
pygame.mixer.music.play(-1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    screen.blit(img, (0,0))

    if game_state.state == "MENU":
        menu(screen, game_state)
    elif game_state.state == "LEVEL":
        level.run()

    pygame.display.update()
    clock.tick(60)