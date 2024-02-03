# import lib.
import pygame

# import variables
from settings import screen_width, screen_height

# import classes
from player import Player
from presets import Wall

class Level():
    def __init__(self, surface):
        # get the display surface
        self.display_surface = surface
        
        # call important methods
        self.setup()
    
    def setup(self):
        # create all sprites
        self.all_sprites = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        # player setup
        player = Player((screen_width/2, screen_height/2))
        self.player.add(player)
        
        # blue wall 64x64 setup
        blue_wall_1x1 = Wall((screen_width/3, screen_height/2))
        self.all_sprites.add(blue_wall_1x1)
    
    def horizontal_movement_collision(self):
        # setup for horizontal movement
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        # check if a block left or right besides the player
        for sprite in self.all_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                
                # left
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    self.current_x = player.rect.left
                
                # right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    self.current_x = player.rect.right
    
    def vertical_movement_collision(self):
        # setup for horizontal movement
        player = self.player.sprite
        
        # process player on ground
        for sprite in self.all_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                
                # player is on a block 
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                
                # player is not on a block
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    
    def update_and_draw(self, surface, dt):
        # player 
        self.player.update(dt)
        self.player.draw(surface)
        
        # layer
        self.all_sprites.draw(surface)
    
    def run(self, dt):
        # call methods to draw sth. on the surface
        self.update_and_draw(self.display_surface, dt)
        
        # player / wall collision
        self.horizontal_movement_collision()
        self.vertical_movement_collision()