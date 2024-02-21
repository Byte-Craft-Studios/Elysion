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
        image = pygame.image.load(ph_player)
        self.draw_player(pos, image)
        self.face_right = True
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2() #self.rect.center -- in ()
        self.speed = p_speed
    
    def draw_player(self, pos, path):
        self.image = path
        
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(center = pos)
    
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
            self.face_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.face_right = False
        else:
            self.direction.x = 0
    
    def move(self,dt):
        
		# normalizing a vector 
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
		# horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x += self.direction.x * self.speed * dt
        # self.rect.centerx = self.pos.x
        
		# vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y += self.direction.y * self.speed * dt
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
    
    def flip(self, pos):
        img_right = pygame.image.load(ph_player)
        img_left = pygame.transform.flip(img_right, True, False)
        
        if self.face_right == True:
            self.draw_player(pos, img_right)
        elif self.face_right == False:
            self.draw_player(pos, img_left)
    
    def update(self, dt, surface, pos):
        # self.animation()
        self.flip(pos)
        self.input()
        self.move(1)
        debug(round(self.direction, 1), surface, 0)
        debug((round(self.rect.x, 1), round(self.rect.y, 1)), surface, 25)