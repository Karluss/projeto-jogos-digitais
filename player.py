import pygame
from support import import_folder
from settings_map import screen_width, screen_height

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()  
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.2
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -12

        self.status = 'idle'
        self.facing_right = True

    def import_character_assets(self): 
        character_path = 'assets/graphics/character/'  
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}

        for animation in self.animations.keys(): 
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def animate(self): 
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed 
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True, False)
            self.image = flipped_image


    def get_input(self):
        keys = pygame.key.get_pressed()  

        if keys[pygame.K_RIGHT]: 
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else: 
            self.direction.x = 0
        
        if keys[pygame.K_SPACE] and not self.space_pressed: 
            self.jump()
            self.space_pressed = True
        elif not keys[pygame.K_SPACE]:
            self.space_pressed = False
    
    def apply_gravity(self): 
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def get_status(self): 
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'idle'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def resize_image(self):
        original_image = self.animations[self.status][int(self.frame_index)]
        resized_image = pygame.transform.scale(original_image, (screen_width/10, screen_height/10))
        self.image = resized_image

    def jump(self): 
        self.direction.y = self.jump_speed
    
    def update(self):
        self.get_input()
        self.get_status()
        self.resize_image()
        self.animate()