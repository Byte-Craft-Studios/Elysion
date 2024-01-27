import pygame, sys
from settings import screen_width, screen_height
from text_import import game_name
from files_import import game_icon
from level import Level

class Game():
    
    def __init__(self):
        self.create_level()
    
    def create_level(self):
        self.level = Level(display_surface)
        self.status = 'level'
     
    def run(self):
        self.level.run()

# Pygame setup
pygame.init()
display_surface = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

# window setup
pygame.display.set_caption(game_name)
# pygame_icon = pygame.image.load(game_icon)
# pygame.display.set_icon(pygame_icon)

while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
            pygame.quit()
            sys.exit()
    
    display_surface.fill('black')
    
    game.run()
    
    pygame.display.update()
    clock.tick(60)