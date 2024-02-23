import pygame, sys
import spritesheet

pygame.init()

screen_width = 192 * 3
screen_heigth = 192 * 3

screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption('Spritesheets')

path = 'tests\import spritecheets\warrior.png'
sprite_sheet_img = pygame.image.load(path).convert_alpha()

sprite_sheet = spritesheet.Spritesheet(sprite_sheet_img)

BG = (50, 50, 50)
BLACK = (0, 0, 0)


frame_0 = sprite_sheet.get_img(0, 0, 192, 192, 1, BLACK)
frame_1 = sprite_sheet.get_img(4, 3, 192, 192, 1, BLACK)


while True:
    
    screen.fill(BG)
    
    screen.blit(frame_0, (0, 0))
    screen.blit(frame_1, (192, 0))
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        
        # to quite the game
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
            pygame.quit()
            sys.exit()
    
    pygame.display.update()