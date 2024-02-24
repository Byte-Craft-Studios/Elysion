# import lib.
import pygame 

# import from pygame and set the font 
pygame.init()
font = pygame.font.Font(None ,30)

# debugging surface
def debug(info, surface=None, y = 1, x = 1):
    if not surface:
        display_surf = pygame.display.get_surface()
    else:
        display_surf = surface
    debug_surf = font.render(str(info), True, 'white')
    debug_rect = debug_surf.get_rect(topleft = ((x*25-15), (y*25+10)))
    pygame.draw.rect(surface, 'black', debug_rect)
    display_surf.blit(debug_surf, debug_rect)