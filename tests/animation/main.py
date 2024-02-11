import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        
        
        for i in range(1, 5):
            path = f'D:\Programmieren\Projekte\Games\Elysion\image\Place holder\Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest3/v2\priest3_v2_{i}.png'
            img = pygame.image.load(path)
            img = pygame.transform.scale(img, (64,64))
            self.sprites.append(img)
        
        print(self.sprites)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
    
    def attack(self):
        self.attack_animation = True
    
    def update(self, speed):
        if self.attack_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False
            self.image = self.sprites[int(self.current_sprite)]
        # print(self.image)

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
            pygame.quit()
            sys.exit()
    
    player.attack()
    
	# Drawing
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.125)
    pygame.display.flip()
    clock.tick(60)