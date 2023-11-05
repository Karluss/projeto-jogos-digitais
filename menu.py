import pygame
from settings_map import *
from button import Button


def get_font(size):
    return pygame.font.Font("assets/campus_font.ttf", size)

def set_button_position(button, screen):
    button.update(screen)

def menu(screen, game_state):

    game_name = get_font(100).render("SURVIVE THE WAVE", True, "White")
    game_rect = game_name.get_rect(center=(screen_width/2,screen_height/4.5))
    screen.blit(game_name, game_rect)

    play_button = Button((screen_width/3, screen_height/2), "JOGAR")
    instruction_button = Button((screen_width/1.5, screen_height/2), "INSTRUÇÕES")

    for button in [instruction_button, play_button]:
        set_button_position(button, screen)

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if pygame.mouse.get_pressed()[0]:
            if play_button.checkForInput(mouse_pos):
                game_state.update("LEVEL")
                




