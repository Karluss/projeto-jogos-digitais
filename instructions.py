import pygame
from settings_map import *
from button import Button

TITLE_FONT = "assets/fonts/campus_font.ttf"
INSTRUCTIONS_FONT = "assets/fonts/BebasNeue-Regular.ttf"
INSTRUCTIONS_ARRAY = ["Corra para sobreviver à tsunami", "O cronômetro mostra em quanto tempo chega a tsunami", "Evite cair em buracos para sobreviver", "Se esbarrar com alguém, isso irá te atrasar", "Chegue ao local alto no fim para sobreviver!"]

def get_font(font_type, size):
    return pygame.font.Font(font_type, size)

def set_instruction_text(text, index, screen):
    font = get_font(INSTRUCTIONS_FONT, 50)
    instruction_text = font.render(text, True, "White")
    instruction_text_rect = instruction_text.get_rect(center=(screen_width/2, screen_height/3.5 + index * 80))  # Ajuste a posição vertical aqui
    pygame.draw.rect(screen, "#79A0FF", instruction_text_rect)
    screen.blit(instruction_text, instruction_text_rect)

def instructions(screen, game_state):
    how_to_play_text = get_font(TITLE_FONT, 100).render("COMO JOGAR", True, "#3A73FF")
    how_to_play_rect = how_to_play_text.get_rect(center=(screen_width/2,screen_height/7))
    screen.blit(how_to_play_text, how_to_play_rect)

    for i in range(len(INSTRUCTIONS_ARRAY)):
        set_instruction_text(f"{i+1} - {INSTRUCTIONS_ARRAY[i]}", i, screen)
    
    back_button = Button((100, 50), "<- MENU")
    back_button.update(screen)

    mouse_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if back_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM MENU")
            game_state.update("MENU")

