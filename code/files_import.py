# import lib.
import pygame

# def img(path):
#     pygame.image.load(path).convert_alpha()

# window
game_icon = '...'

# placeholder images
normal_path = 'D:\Programmieren\Projekte\Games\Elysion\image'
player_path = '\Place holder\Pixel Dungeon Asset Pack\Character_animation\priests_idle'
p_img_path = 'priest1_v1_'
ending = '.png'
img_1 = f'{normal_path}{player_path}/priest1/v1/{p_img_path}1{ending}'
ph_player = pygame.image.load(img_1)