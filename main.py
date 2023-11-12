import pygame, sys
from settings_map import *
from level import Level
from menu import menu
from game_state import GameState
from instructions import instructions
from game_over import game_over
from select_level import select_level
from input_name import InputBox

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
game_state = GameState()
input = InputBox(screen_width/3, screen_height/1.5,int(screen_width/3), int(screen_height/6), 'Player1')
img_background = pygame.image.load("assets/graphics/background/sky.png")
img = pygame.transform.scale(img_background,(screen_width, screen_height*1.2))
music_background = pygame.mixer.music.load("assets/music/beach sound effect.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


def set_input_text():
    input.draw(screen)
    input_help_text = pygame.font.Font("assets/fonts/BebasNeue-Regular.ttf", int(screen_height/8)).render("Insira um nome", True, "Black")
    input_help_rect = input_help_text.get_rect(center=(screen_width/2, screen_height/1.1))

    game_state.user_name = input.text

    screen.blit(input_help_text, input_help_rect)

while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        input.handle_event(event)

    screen.fill('black')
    screen.blit(img, (0,0))

    if game_state.state == "MENU":
        menu(screen, game_state)
        set_input_text()
    elif game_state.state == "LEVEL":
        level.run(game_state,screen)
    elif game_state.state == "INSTRUCTION":
        instructions(screen, game_state)
    elif game_state.state == "GAME OVER":
        game_over(screen, game_state)
    elif game_state.state == "SELECT_LEVEL":
        select_level(screen, game_state)

    pygame.display.update()
    clock.tick(60)