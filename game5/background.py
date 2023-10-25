import pygame
from game_parameters import *
import random
def draw_background(surf):
    #Load our tiles from the assets folder
    water = pygame.image.load("../assets/Sprites/water.png").convert()
    sand = pygame.image.load("../assets/Sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/Sprites/seagrass.png").convert()
    #make PNGS transparent
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))
    #draw sandy bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height-tile_size))
    #draw sea_grass
    for _ in range(26):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x,screen_height-tile_size*2))

    #draw the text
    custom_font = pygame.font.Font("../assets/Fonts/Brainfish_Rush.ttf", 128)
    text = custom_font.render("Chomp",True, (255,29,0))
    surf.blit(text, (screen_width/2-text.get_width()/2, 0))
