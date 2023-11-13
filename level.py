import pygame 
from tiles import Tile
from settings_map import *
from player import Player
from ranking import RANKING_DICT_POINTS, RANKING_DICT_NAME
from button import Button

class Level:
    def __init__(self,surface):
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = 0
        self.game_timer = pygame.time.get_ticks()
        self.temporizer = True
        self.points = 0
        self.win = False

    def setup_level(self,layout, game_state):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = tile_size * col_index
                y = tile_size * row_index
                if cell == 'X':
                    tile = Tile((x,y),game_state.level)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == 'S' or cell == 'W':
                    tile = Tile((x,y),"SAFE")
                    if cell == 'W':
                        tile.isWin = True
                    self.tiles.add(tile)
                if cell == 'O':
                    tile = Tile((x,y),"OBSTACLE")
                    self.tiles.add(tile)
                if cell == 'I':
                    tile = Tile((x,y),"INV")
                    self.tiles.add(tile)

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
    def vertical_movement_collision(self, game_state, screen):
        player = self.player.sprite 
        player.apply_gravity()

        for sprite in self.tiles.sprites(): 
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    if sprite.isWin:
                        player.status = 'idle'
                        player.stop = True
                        self.win = True
                        if not game_state.end:
                            RANKING_DICT_POINTS[game_state.run_id] = self.points
                            RANKING_DICT_NAME[game_state.run_id] = game_state.user_name
                            game_state.run_id += 1
                        game_state.end = True
                        self.set_win(screen, game_state)
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
    
    def set_win(self,screen, game_state):
        win_text = self.get_font("assets/fonts/BebasNeue-Regular.ttf", 100).render("VOCÊ SOBREVIVEU", True, "Green")
        win_rect = win_text.get_rect(center=(screen_width/2,screen_height/7))
        screen.blit(win_text, win_rect)

        self.set_buttons(game_state, screen) 
    
    def set_buttons(self,game_state, screen):
        level_button = Button((100, 50), "<- NÍVEIS ")
        level_button.update(screen)

        ranking_button = Button((screen_width/1.1, 50), " RANKING ->")
        ranking_button.update(screen)

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if level_button.checkForInput(mouse_pos):
                print("DEBUG: CLIQUE EM LEVEL")
                game_state.update("SELECT_LEVEL")
            if ranking_button.checkForInput(mouse_pos):
                print("DEBUG: CLIQUE EM RANKING")
                game_state.update("RANKING")
    def get_font(self, font_type, size):
        return pygame.font.Font(font_type, size)
    
    def countdown(self, screen, game_state):
        initial_time = 25000  # Tempo inicial em milissegundos (18000ms = 18 segundos)
        current_time = pygame.time.get_ticks()  # Tempo atual do jogo
        remaining_time = max(0, initial_time - (current_time - self.game_timer))  # Tempo restante

        if self.temporizer:
            countdown_text = self.get_font("assets/fonts/BebasNeue-Regular.ttf", 50).render(f"{int(remaining_time/1000)}", True, "Red")  # Exibição do tempo (convertido para segundos)
            countdown_rect = countdown_text.get_rect(center=(screen_width/2, screen_height/7))
            self.points = remaining_time/1000
            screen.blit(countdown_text, countdown_rect)

            if remaining_time <= 0:
                self.temporizer = False
                game_state.update("GAME OVER")
            

    def get_level_map(self, game_state):
        if game_state.level == "PRAIA":
            return beach_map
        elif game_state.level == "CIDADE":
            return city_map
        elif game_state.level == "PORTO":
            return port_map

    def run(self, game_state, screen):

        level_map = self.get_level_map(game_state)

        if game_state.restart_level:
            self.setup_level(level_map, game_state)  
            self.game_timer = pygame.time.get_ticks()  # Reiniciando o timer
            game_state.restart_level = False
            game_state.end = False
            self.win = False
            self.temporizer = True  # Habilitando o temporizador novamente
            self.points = 0
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
        self.vertical_movement_collision(game_state, screen)

        # countdown
        if not self.win:
            self.countdown(screen,game_state)
        
