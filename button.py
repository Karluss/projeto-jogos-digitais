import pygame

COLOR_WHITE = (255, 0, 0)

class Button:
    def __init__(self, position, text_button):
        self.position = position
        self.text = self.get_font(50).render(text_button, True, "White")
        self.text_color = "White"
        self.rect_color = "RED"
        self.rect = self.text.get_rect(center=self.position)
    
    def get_font(self, size):
        return pygame.font.Font("assets/BebasNeue-Regular.ttf", size)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def update_text_button(self, text, screen):
        self.text = self.get_font(50).render(text, True, "White")
        self.rect = self.text.get_rect(center=self.position)
        self.update(screen)

    def update(self, screen):
        pygame.draw.rect(screen, self.rect_color, self.rect)

        screen.blit(self.text, self.rect)

