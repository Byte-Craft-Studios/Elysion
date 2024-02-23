# import lib.
import pygame

# import variables / functions
from settings import tile_size, p_speed, p_size
from files_import import ph_player_path, ph_player, ending, ph_player_spritesheet
from support import load
from debug import debug

# import classes 
from animation import Animation
from support import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # player setup
        self.img_right = pygame.image.load(ph_player)
        self.img_left = pygame.transform.flip(self.img_right, True, False)
        
        self.draw_player(self.img_right)
        self.rect = self.image.get_rect(center = pos)
        
        # player image settings 
        self.imgs = []
        self.import_spritesheet()
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2() #self.rect.center -- in ()
        self.speed = p_speed
        
        # animation setup
        self.frame_index = 1
        self.frames = 48
        self.animation_speed = 0.0013
        
        # facing
        self.facing = 'right'
    
    def draw_player(self, path):
        # draw the player image and scale it
        self.image = path
        self.image = pygame.transform.scale(self.image, (p_size, p_size))
    
    def import_spritesheet(self):
        # import image
        img = pygame.image.load(ph_player_spritesheet)
        
        # set image height and width 
        img_height = img.get_height()
        img_width = img.get_width()
        
        # numbers of images and set row and col
        img_size = 192
        row = int(img_height / img_size)
        col = int(img_width / img_size)
        
        sprite_sheet = Spritesheet(img)
        BLACK = (0, 0, 0)
        
        for i in range(row):
            for m in range(col):
                image = sprite_sheet.get_img(m, i, img_size, img_size, 1, BLACK)
                self.imgs.append(image)        
    
    def input(self):
        # control system for player movement
        keys = pygame.key.get_pressed()
        
        # vertical movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.facing = 'up'
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.facing = 'down'
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
            # self.img_right = pygame.image.load(path)
            # self.img_left = pygame.transform.flip(self.img_right, True, False)
            
            self.img_right = self.imgs[(round(self.frame_index)-1)]
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
        self.move(dt)
        
        # draw the image and animate them
        self.animation()
        self.flip()
        
        # debugging tool
        debug(round(self.direction, 1), surface, 0)
        debug((round(self.rect.x, 1), round(self.rect.y, 1)), surface, 25)
        debug(self.frame_index, surface, 50)