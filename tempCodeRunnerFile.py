import pygame, sys
from settings_map import *
from level import Level
from menu import menu
from game_state import GameState
from instructions import instructions
from game_over import game_over

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
pygame.mixer.music.set_volume(0.05)


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
        level.run(game_state,screen)
        game_state.should_restart_level = True
    elif game_state.state == "INSTRUCTION":
        instructions(screen, game_state)
    elif game_state.state == "GAME OVER":
        game_over(screen, game_state)

    pygame.display.update()
    clock.tick(60)