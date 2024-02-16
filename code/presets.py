# import lib.
import pygame

# import variables
from settings import tile_size
from support import scale

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # wall setup (image + scale + rect)
        # self.image = pygame.image.load(self.image_player)
        self.image = pygame.Surface(pos)
        scale((self.image.fill('blue')), (tile_size, tile_size))
        # self.image = scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(center = pos)
    
    # def update(self):
    #     self.input()
    #     # self.move()