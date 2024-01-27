import pygame
from settings import tile_size, screen_height, screen_width

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # self.image = pygame.image.load(self.image_player)
        self.image = pygame.Surface(pos)
        self.image.fill('red')
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(center = pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed_setup = 20
        self.speed = self.speed_setup
    
    def input(self):
        # control system for player movement
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = self.speed
        
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = self.speed * -1
        
        else:
            self.direction.x = 0
    
    def move(self):
        
		# normalizing a vector 
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
		# horizontal movement
        self.pos.x += self.direction.x * self.speed
        self.rect.centerx = self.pos.x
        
		# vertical movement
        self.pos.y += self.direction.y * self.speed
        self.rect.centery = self.pos.y
    
    def update(self):
        self.input()
        self.move()
        
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y