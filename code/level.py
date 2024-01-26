import pygame
from settings import solid_color, screen_width, screen_height
from player import Player

class Level():
    def __init__(self):
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite groups
        self.all_sprites = pygame.sprite.Group()
    
    def setup(self):
        self.player = Player((screen_width/2, screen_height / 2), self.all_sprites)
    
    def run(self, dt):
        self.setup()
        
        self.display_surface.fill(solid_color)
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)