# import lib.
import pygame 
from settings import screen_height, screen_width

# import from pygame and set the font 
pygame.init()
surface = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.Font(None ,30)

# debugging surface
def debug(info, surface=None, y = 10, x = 10):
    if not surface:
        display_surf = pygame.display.get_surface()
    else:
        display_surf = surface
    debug_surf = font.render(str(info), True, 'white')
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    pygame.draw.rect(surface, 'black', debug_rect)
    display_surf.blit(debug_surf, debug_rect)

def load(path):
    pygame.image.load(path).convert_alpha()

# a class to subtract the spritesheet in different small images
class Spritesheet():
    def __init__(self, image):
        self.image = image
    
    def get_img(self, col, row, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        # image.fill('grey')
        image.blit(self.image, (0, 0), ((col * width), (row * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        
        image.set_colorkey(color)
        
        return image