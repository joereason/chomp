import pygame
import sys
import random
from fish import Fish, fishes #importing fish module and Fish class

#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

surf = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Using blit to draw tiles')
#Load game font
custom_font = pygame.font.Font("../assets/Fonts/Brainfish_Rush.ttf", 128)
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
    text = custom_font.render("Chomp",True, (255,29,0))
    surf.blit(text, (screen_width/2-text.get_width()/2, 0))
    # screen_height/2-text.get_height()/2

# draw fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(0, screen_width-tile_size*2),random.randint(100, screen_height-tile_size*2)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw background
    surf.blit(background, (0,0))

    fishes.draw(background)
    #update display
    pygame.display.flip()

    #pygame.surface.transform.flip()
pygame.quit()