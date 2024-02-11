import pygame 

from settings import tile_size

class Animation():
    def __init__(self, path, frames, pos):
        super().__init__()
        
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        
        
        for i in range(1, (frames + 1)):
            new_path = f'{path}{i}.png'
            print(new_path)
            
            img = pygame.image.load(new_path)
            img = pygame.transform.scale(img, (tile_size, tile_size))
            self.sprites.append(img)
        
        print(self.sprites)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(center = pos)
    
    def attack(self):
        self.attack_animation = True
    
    def update(self, speed):
        if self.attack_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False
            self.image = self.sprites[int(self.current_sprite)]