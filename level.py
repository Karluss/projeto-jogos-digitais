import pygame 
from tiles import Tile
from settings_map import *
from player import Player

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        self.time_remaining = 60
        self.start_time = pygame.time.get_ticks()

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = tile_size * col_index
                y = tile_size * row_index
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def scroll_x(self):  
        player = self.player.sprite
        player_x = player.rect.centerx  
        direction_x = player.direction.x
        speed = 5

        if player_x < screen_width/4 and direction_x < 0:
            self.world_shift = speed
            player.speed = 0
        elif player_x > screen_width - (screen_width/4) and direction_x > 0:
            self.world_shift = -speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = speed

    def horizontal_movement_collision(self):
        player = self.player.sprite 

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites(): 
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:  # moving left 
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0: # moving right
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right < self.current_x or player.direction.x <= 0):
            player.on_right = False
    def vertical_movement_collision(self, game_state):
        player = self.player.sprite 
        player.apply_gravity()

        for sprite in self.tiles.sprites(): 
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
        
        if player.rect.y > screen_height:
            game_state.update("GAME OVER")
    
    def get_font(self, font_type, size):
        return pygame.font.Font(font_type, size)
    
    def countdown(self,screen): 
        elapsed_time = pygame.time.get_ticks() - self.start_time
        remaining_seconds = max(0, self.time_remaining - elapsed_time / 1000)  # Convertendo milissegundos para segundos
        countdown_text = self.get_font("assets/fonts/BebasNeue-Regular.ttf", 50).render(f"{remaining_seconds}", True, "Red")
        countdown_rect = countdown_text.get_rect(center=(screen_width/2,screen_height/7))
        screen.blit(countdown_text, countdown_rect)
    def run(self, game_state, screen):

        if game_state.restart_level:
            self.setup_level(level_map)  
            game_state.restart_level = False
            if game_state.sound == "ON":
                pygame.mixer.music.load("assets/music/Soundtrack da fase.mp3")
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)

        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # player
        self.player.update()
        self.player.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision(game_state)

        # countdown
        self.countdown(screen)
        