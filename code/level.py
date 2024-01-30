import pygame
from settings import screen_width, screen_height, tile_size
from player import Player
from presets import Wall

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
        
        # blue wall 64x64
        blue_wall_1x1 = Wall((screen_width/3, screen_height/2))
        self.all_sprites.add(blue_wall_1x1)
    
    def update_and_draw(self):
        # player 
        self.player.update()
        self.player.draw(self.display_surface)
        # collisions   -- not working
        # collisions = pygame.sprite.spritecollide(self.player, self.all_sprites, dokill=False)
        # for self.all_sprites in collisions:
        #     print('collision dect')

        # layer
        self.all_sprites.draw(self.display_surface)

        
    def run(self):
        self.update_and_draw()