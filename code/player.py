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
        
        # status
        self.status = 'right'
        self.attack = False
        
        # player image settings 
        self.imgs_idle = []
        self.imgs_run = []
        self.imgs_down = []
        self.imgs_up = []
        
        self.imgs_idle_attack = []
        self.imgs_idle_attack_down = []
        self.imgs_idle_attack_up = []
        
        self.imgs_run_attack = []
        self.imgs_run_attack_down = []
        self.imgs_run_attack_up = []
        
        
        # player setup
        self.import_spritesheet()
        self.draw_player(self.imgs_idle[round(self.frame_index)-1])
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
                
                if i == 0:
                    self.imgs_idle.append(image)
                
                elif i == 1:
                    self.imgs_run.append(image)
                
                elif i == 2:
                    self.imgs_run_attack.append(image)
                
                elif i == 3:
                    self.imgs_idle_attack.append(image)
                
                elif i == 4:
                    self.imgs_run_attack_down.append(image)
                
                elif i == 5:
                    self.imgs_idle_attack_down.append(image)
                
                elif i == 6:
                    self.imgs_run_attack_up.append(image)
                
                elif i == 7:
                    self.imgs_idle_attack_up.append(image)
    
    def input(self):
        # control system for player movement
        keys = pygame.key.get_pressed()
        
        # vertical movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
        
        # horizontal movement
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
        
        # check for attacking
        if keys[pygame.K_SPACE]:
            self.attack = True
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
        
        self.animation()
        animation = (round(self.frame_index)-1)
        
        if self.status == 'right':
            if self.attack:
                image = self.imgs_idle_attack[animation]
            else:
                image = self.imgs_run[animation]
        
        elif self.status == 'left':
            if self.attack:
                img = self.imgs_idle_attack[animation]
            else:
                img = self.imgs_run[animation]
            
            image = pygame.transform.flip(img, True, False)
        
        elif self.status == 'up':
            if self.attack:
                image = self.imgs_idle_attack_up[animation]
            else:
                image = self.imgs_idle[animation]
        
        elif self.status == 'down':
            if self.attack:
                image = self.imgs_idle_attack_down[animation]
            else:
                image = self.imgs_idle[animation]
        
        else:
            if self.attack:
                image = self.imgs_idle_attack[animation]
            else:
                image = self.imgs_idle[animation]
        
        self.draw_player(image)
    
    def update(self, dt, surface):
        # movement 
        self.input()
        self.move(dt)
        
        # draw the image and animate them
        self.alignment()
        
        # debugging tool
        debug(round(self.direction, 1), surface, 0)
        debug((round(self.rect.x, 1), round(self.rect.y, 1)), surface, 1)
        debug(self.frame_index, surface, 2)
        debug(self.status, surface, 3)