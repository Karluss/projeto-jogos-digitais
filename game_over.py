import pygame
from settings_map import *
from button import Button

FONT_TEXT = "assets/fonts/BebasNeue-Regular.ttf"

def get_font(font_type, size):
    return pygame.font.Font(font_type, size)

def game_over(screen, game_state):
    pygame.mixer.music.stop()
    game_over_text = get_font(FONT_TEXT, 100).render("VOCÊ PERDEU", True, "Red")
    game_over_rect = game_over_text.get_rect(center=(screen_width/2,screen_height/7))
    screen.blit(game_over_text, game_over_rect)
    
    try_again_button = Button((screen_width/2, screen_height/2.5), " TENTAR NOVAMENTE ")
    try_again_button.update(screen)

    back_to_menu_button = Button((screen_width/2, screen_height/1.4), " VOLTAR AO MENU ")
    back_to_menu_button.update(screen)

    mouse_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if try_again_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM TRY AGAIN")
            game_state.update("LEVEL")
        if back_to_menu_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM BACK TO MENU")
            game_state.update("MENU")
            if game_state.sound == "ON":
                pygame.mixer.music.load("assets/music/beach sound effect.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)

