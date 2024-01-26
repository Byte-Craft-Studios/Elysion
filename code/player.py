import pygame
from settings import tile_size

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        # general setup
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)