import random
import pygame
import sys
from fish import Fish, fishes #importing a class and a Sprite group

#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Using blit to draw tiles')
#add pygame clock
clock = pygame.time.Clock() # allows us to set the frames per second

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

    #draw the textx
    custom_font = pygame.font.Font("../assets/Fonts/Brainfish_Rush.ttf", 128)
    text = custom_font.render("Chomp",True, (255,29,0))
    surf.blit(text, (screen_width/2-text.get_width()/2, 0))
    # screen_height/2-text.get_height()/2

#Main loop
running = True
background = screen.copy()
draw_background(background)

for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(tile_size, screen_height-tile_size)))

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    #draw background
    screen.blit(background, (0,0))

    #update fish position
    fishes.update()

    #check if fish have left the screen
    for fish in fishes: # loop through our fish in the sprite group
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width+50),
                                random.randint(tile_size, screen_height-tile_size)))

    fishes.draw(screen)

    # update the display
    pygame.display.flip()

    # set the frame rate
    clock.tick(60)

#quit pygame
pygame.quit()