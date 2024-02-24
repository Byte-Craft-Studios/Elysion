# import lib.
import pygame, time

# import variables / functions
from settings import p_speed, p_size
from files_import import ph_player_spritesheet
from debug import debug

# import classes 
from support import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2() #self.rect.center -- in ()
        self.speed = p_speed
        
        # animation setup
        self.frame_index = 1
        self.frames = 6
        self.animation_speed = 0.0017
        
        # facing
        self.facing = 'right'
        self.attack = False
        
        # player image settings 
        self.imgs_idle_1 = []
        self.imgs_idle_2 = []
        self.imgs_attack_side_up = []
        self.imgs_attack_side_down = []
        self.imgs_attack_down_right = []
        self.imgs_attack_down_left = []
        self.imgs_attack_up_left = []
        self.imgs_attack_up_right = []
        
        # player setup
        self.import_spritesheet()
        self.draw_player(self.imgs_idle_1[round(self.frame_index)-1])
        self.rect = self.image.get_rect(center = pos)
    
    def draw_player(self, path):
        # draw the player image and scale it
        self.image = path
        self.image = pygame.transform.scale(self.image, (p_size, p_size))
    
    def import_spritesheet(self):
        # import image
        img = pygame.image.load(ph_player_spritesheet)
        
        # set image height and width 
        spritesheet_height = img.get_height()
        spritesheet_width = img.get_width()
        
        # numbers of images and set row and col
        img_size = 192
        row = int(spritesheet_height / img_size)
        col = int(spritesheet_width / img_size)
        
        sprite_sheet = Spritesheet(img)
        bg = (0, 0, 0)
        
        for i in range(row):
            for m in range(col):
                image = sprite_sheet.get_img(m, i, img_size, img_size, 1, bg)
                
                if i == 1:
                    self.imgs_idle_1.append(image)
                elif i == 2:
                    self.imgs_idle_2.append(image)
                elif i == 3:
                    self.imgs_attack_side_up.append(image)
                elif i == 4:
                    self.imgs_attack_side_down.append(image)
                elif i == 5:
                    self.imgs_attack_down_right.append(image)
                elif i == 6:
                    self.imgs_attack_down_left.append(image)
                elif i == 7:
                    self.imgs_attack_up_left.append(image)
                elif i == 8:
                    self.imgs_attack_up_right.append(image)
    
    def input(self, dt):
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
        
        # check for attacking
        if keys[pygame.K_SPACE]:
            self.attack = True
            # self.frame_index = 1
            
            t = (self.frames / self.animation_speed * dt)
        else:
            self.attack = False
    
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
        for _ in range(self.frames):
            # change the frame index and reset the frame index
            self.frame_index += self.animation_speed
            if self.frame_index >= self.frames:
                self.frame_index = 1
    
    def alignment(self):
        
        animation = (round(self.frame_index)-1)
        
        if self.facing == 'right':
            if self.attack:
                self.animation()
                image = self.imgs_attack_side_up[animation]
            else:
                self.animation()
                image = self.imgs_idle_1[animation]
        
        elif self.facing == 'left':
            if self.attack:
                self.animation()
                img = self.imgs_attack_side_up[animation]
            else:
                self.animation()
                img = self.imgs_idle_1[animation]
            
            image = pygame.transform.flip(img, True, False)
        
        elif self.facing == 'up':
            if self.attack:
                image = self.imgs_attack_up_left[animation]
        
        elif self.facing == 'down':
            if self.attack:
                image = self.imgs_attack_down_right[animation]
        
        self.draw_player(image)
    
    def update(self, dt, surface):
        # movement 
        self.input(dt)
        self.move(dt)
        
        # draw the image and animate them
        self.alignment()
        
        # debugging tool
        debug(round(self.direction, 1), surface, 0)
        debug((round(self.rect.x, 1), round(self.rect.y, 1)), surface, 1)
        debug(self.frame_index, surface, 2)