import pygame 

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,level):
        super().__init__()
        self.image = self.get_tile_type(level)
        self.rect = self.image.get_rect(topleft = pos)
    
    def get_tile_type(self,level):
        if level == "PRAIA":
            return pygame.image.load("assets/graphics/sand/tile.png")
        elif level == "CIDADE":
            return pygame.image.load("assets/graphics/concrete/concreto_bloco.png")
        elif level == "PORTO":
            return pygame.image.load("assets/graphics/wood/pier_textura.jpg")

    def update(self, x_shift): 
        self.rect.x += x_shift