import pygame
from settings import screen_width, screen_height, tile_size
from player import Player

class Level():
    def __init__(self, surface):
        # get the display surface
        self.display_surface = surface
        
        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        
        self.setup()
    
    def setup(self):
        # player
        self.player = pygame.sprite.GroupSingle()
        player = Player((screen_width/2, screen_height/2))
        self.player.add(player)
    
    def update_and_draw(self):
        # player 
        self.player.update()
        self.player.draw(self.display_surface)
    
    def run(self):
        self.update_and_draw()