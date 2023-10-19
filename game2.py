import pygame
import sys
import random

#initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Using blit to draw tiles')

#Load Game Font
custom_font = pygame.font.Font('assets/fonts/Brainfish_Rush.ttf', 128)

def draw_background(screen):
    #Load our tiles from the assets folder
    water = pygame.image.load('assets/sprites/water.png').convert()
    sand = pygame.image.load('assets/sprites/sand_top.png').convert()
    seagrass = pygame.image.load('assets/sprites/seagrass.png').convert()
    #make PNGs transparent
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x, y))

    #draw a sandy bottom
    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x, screen_height-tile_size))

    #place the seagrass randomly along the bottom
    for _ in range(7):
        screen.blit(seagrass, (random.randint(0, screen_width), random.randint(screen_height-2*tile_size, screen_height-tile_size)))

    #draw the text
    text = custom_font.render('Chomp', True, (255, 29, 0))
    screen.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-text.get_height()/2))

def draw_fishes(surf):
    #Load our fish files onto our surface
    green_fish = pygame.image.load('assets/sprites/green_fish.png').convert()
    orange_fish = pygame.image.load('assets/sprites/orange_fish.png').convert()
    puffer_fish = pygame.image.load('assets/sprites/puffer_fish.png').convert()
    #set colorkey
    green_fish.set_colorkey((0,0,0))
    orange_fish.set_colorkey((0, 0, 0))
    puffer_fish.set_colorkey((0, 0, 0))
    fishes = [green_fish, orange_fish, puffer_fish]

    #distribute our fish on the screen randomly
    for _ in range (5):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height-2*tile_size)
        f = random.randint(0, 2)
        if x > screen_width/2:
            if f == 0:
                pygame.transform.flip(green_fish, True, False)
                surf.blit(green_fish, (x,y))
            elif f == 1:
                pygame.transform.flip(orange_fish, True, False)
                surf.blit(orange_fish, (x, y))
            else:
                pygame.transform.flip(puffer_fish, True, False)
                surf.blit(puffer_fish, (x, y))
        else:
            surf.blit(fishes[f], (x,y))

#Main loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the background
    screen.blit(background, (0,0))

    #update the display
    pygame.display.flip()

#quit pygame
pygame.quit()
