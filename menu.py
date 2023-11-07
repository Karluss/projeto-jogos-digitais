import pygame
from settings_map import *
from button import Button

DESATIVAR_SOM_TEXT = " DESATIVAR SOM "
ATIVAR_SOM_TEXT = " ATIVAR SOM "
SOUND_BUTTON_PRESSED = False

def get_font(size):
    return pygame.font.Font("assets/campus_font.ttf", size)

def set_button_position(button, screen):
    button.update(screen)

def set_button_sound(game_state):
    if game_state.get_sound_state() == "ON":
        sound_button = Button((screen_width/2, screen_height/2), DESATIVAR_SOM_TEXT)
    else:
        sound_button = Button((screen_width/2, screen_height/2), ATIVAR_SOM_TEXT)
    return sound_button

def menu(screen, game_state):
    global SOUND_BUTTON_PRESSED

    game_name = get_font(100).render("SURVIVE THE WAVE", True, "#3A73FF")
    game_rect = game_name.get_rect(center=(screen_width/2,screen_height/4.5))
    screen.blit(game_name, game_rect)

    play_button = Button((screen_width/3, screen_height/2), " JOGAR ")
    instruction_button = Button((screen_width/1.4, screen_height/2), " INSTRUÇÕES ")
    sound_button = set_button_sound(game_state)

    for button in [instruction_button, play_button, sound_button]:
        set_button_position(button, screen)

    mouse_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if play_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM PLAY")
            game_state.update("LEVEL")
        if sound_button.checkForInput(mouse_pos) and not SOUND_BUTTON_PRESSED:
            if game_state.get_sound_state() == "ON":
                print("DEBUG: CLIQUE EM SOUND OFF")
                game_state.set_sound_state("OFF")
                button.update_text_button(ATIVAR_SOM_TEXT, screen)
                pygame.mixer.music.stop()
            else:
                print("DEBUG: CLIQUE EM SOUND ON")
                game_state.set_sound_state("ON")
                button.update_text_button(DESATIVAR_SOM_TEXT, screen)
                pygame.mixer.music.play(-1)
            SOUND_BUTTON_PRESSED = True
    else:
        SOUND_BUTTON_PRESSED = False # Para corrigir o comportamento do botão de som




