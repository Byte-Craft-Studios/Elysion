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
        
        # player setup
        self.img_right = pygame.image.load(ph_player)
        self.img_left = pygame.transform.flip(self.img_right, True, False)
        
        self.draw_player(self.img_right)
        self.rect = self.image.get_rect(center = pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2() #self.rect.center -- in ()
        self.speed = p_speed
        
        # animation setup
        self.frame_index = 1
        self.frames = 4
        self.animation_speed = 0.002
        
        # facing
        self.facing = 'right'
    
    def draw_player(self, path):
        # draw the player image and scale it
        self.image = path
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
    
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
            self.facing = 'right'
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.facing = 'left'
        else:
            self.direction.x = 0
    
    def move(self,dt):
        
		# normalizing a vector 
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
		# horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x += self.direction.x * self.speed * dt
        
		# vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
    
    def animation(self):
        for _ in range(self.frames):    # infinite loop
            
            # path, which is changed
            path = f'{ph_player_path}{round(self.frame_index)}{ending}'
            
            # set the images
            self.img_right = pygame.image.load(path)
            self.img_left = pygame.transform.flip(self.img_right, True, False)
            
            # change the frame index and reset the frame index
            self.frame_index += self.animation_speed
            if self.frame_index >= self.frames:
                self.frame_index = 1
    
    def flip(self):
        # choose the right image
        if self.facing == 'right':
            self.draw_player(self.img_right)
        elif self.facing == 'left':
            self.draw_player(self.img_left)
    
    def update(self, dt, surface):
        # movement 
        self.input()
        self.move(1)
        
        # draw the image and animate them
        self.animation()
        self.flip()
        
        # debugging tool
        debug(round(self.direction, 1), surface, 0)
        debug((round(self.rect.x, 1), round(self.rect.y, 1)), surface, 25)
        debug(self.frame_index, surface, 50)