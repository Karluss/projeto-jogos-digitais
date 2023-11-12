import pygame
from settings_map import *
from button import Button

TITLE_FONT = "assets/campus_font.ttf"
RANKING_FONT = "assets/BebasNeue-Regular.ttf"
RANKING_ARRAY = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

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

    for i in range(len(RANKING_ARRAY)):
        set_ranking_text(f"{i+1} - {RANKING_ARRAY[i]}", i, screen)
    
    back_button = Button((100, 50), "<- MENU")
    back_button.update(screen)

    mouse_pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        if back_button.checkForInput(mouse_pos):
            print("DEBUG: CLIQUE EM MENU")
            game_state.update("MENU")

    
