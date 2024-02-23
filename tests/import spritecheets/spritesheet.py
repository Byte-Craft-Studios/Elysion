import pygame 

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