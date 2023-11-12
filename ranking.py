import pygame
from settings_map import *
from button import Button
import operator

TITLE_FONT = "assets/fonts/campus_font.ttf"
RANKING_FONT = "assets/fonts/BebasNeue-Regular.ttf"
RANKING_DICT_POINTS = {}
RANKING_DICT_NAME = {}

def get_font(font_type, size):
    return pygame.font.Font(font_type, size)

def set_ranking_text(text, index, screen):
    font = get_font(RANKING_FONT, 50)
    ranking_text = font.render(text, True, "White")
    ranking_rect = ranking_text.get_rect(center=(screen_width/2, screen_height/3.5 + index * 80))  # Ajuste a posição vertical aqui
    pygame.draw.rect(screen, "#79A0FF", ranking_rect)
    screen.blit(ranking_text, ranking_rect)

def ranking(screen, game_state):
    ranking_text = get_font(TITLE_FONT, 100).render("Ranking", True, "#3A73FF")
    ranking_rect = ranking_text.get_rect(center=(screen_width/2,screen_height/7))
    screen.blit(ranking_text, ranking_rect)

    top_five_dict = dict(sorted(RANKING_DICT_POINTS.items(), key=lambda item: item[1], reverse=True)[:6])

    pos = 1
    for key in top_five_dict.keys():
        set_ranking_text(f"{pos} - {RANKING_DICT_NAME[key]} - {RANKING_DICT_POINTS[key]}", pos, screen)
        pos += 1
    
    back_button = Button((100, 50), "<- MENU")
    back_button.update(screen)

    mouse_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if back_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM MENU")
            game_state.update("MENU")

    
