import pygame, sys
from settings import screen_width, screen_height
from text_import import game_name
from files_import import game_icon 
from level import Level

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        
        self.level = Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            
            pygame.display.update()

# window setup
pygame.display.set_caption(game_name)
# pygame_icon = pygame.image.load(game_icon).convert_alpha()
# pygame.display.set_icon(pygame_icon)

if __name__ == '__main__':
    game = Game()
    game.run()