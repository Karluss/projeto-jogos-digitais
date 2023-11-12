import pygame
from settings_map import *
from button import Button

DESATIVAR_SOM_TEXT = " DESATIVAR SOM "
ATIVAR_SOM_TEXT = " ATIVAR SOM "

def get_font(size):
    return pygame.font.Font("assets/fonts/campus_font.ttf", size)

def set_button_position(button, screen):
    button.update(screen)

def select_level(screen, game_state):

    select_level_name = get_font(100).render("SELECIONE A FASE", True, "#3A73FF")
    select_level_rect = select_level_name.get_rect(center=(screen_width/2,screen_height/4.5))
    screen.blit(select_level_name, select_level_rect)

    beach_button = Button((screen_width/3, screen_height/2.4), " PRAIA ")
    city_button = Button((screen_width/1.6, screen_height/2.4), " CIDADE ")
    port_button = Button((screen_width/2.1, screen_height/1.5), " PORTO ")

    for button in [beach_button, city_button, port_button]:
        set_button_position(button, screen)
    
    back_button = Button((100, screen_height/1.1), "<- MENU")
    back_button.update(screen)
    
    mouse_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if beach_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM BEACH")
            game_state.update("LEVEL")
        if city_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM CITY")
            game_state.update("LEVEL")
        if port_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM PORT")
            game_state.update("LEVEL")
        if back_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM MENU")
            game_state.update("MENU")