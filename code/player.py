# import lib.
import pygame

# import variables / functions
from settings import tile_size, p_speed
from files_import import ph_player_path, ph_player, ending
from support import load
from debug import debug

# import classes 
from animation import Animation

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # player setup (image + scale + rect)
        # self.image = Animation(ph_player, 4, pos)
        self.image = load(ph_player)
        
        
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(center = pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2() #self.rect.center -- in ()
        self.speed = p_speed
    
    def input(self):
        # control system for player movement
        keys = pygame.key.get_pressed()
        
        # vertical movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        # horizontal movement
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self,dt):
        
		# normalizing a vector 
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
		# horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        # self.rect.centerx = self.pos.x
        
		# vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        # self.rect.centery = self.pos.y
    
    def animation(self):
        frame_index = 1
        frames = 4
        animation_speed = 0.16
        
        while frame_index <= frames:
            path = f'{ph_player_path}{int(frame_index)}{ending}'
            self.image = load(path)
            frame_index += animation_speed
            
            if frame_index == frames:
                frame_index = 1
    
    def update(self, dt, surface):
        self.animation()
        self.input()
        self.move(dt)
        debug(self.direction, surface)