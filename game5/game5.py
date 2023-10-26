import pygame
import sys
import random

#Import all our necessary files
from fish import Fish, fishes
from background import draw_background
from game_parameters import *
from player import Player

#Initialize pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Adding a player fish')

#Create the clock object
clock = pygame.time.Clock()

#Main loop
running = True
background = screen.copy()
draw_background(background)

#Draw fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*1.5),random.randint(tile_size, screen_height-2*tile_size)))

#Draw player fish
player = Player(screen_width/2, screen_height/2)

#Placeholder for a orange player fish
while running:
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            running = False
        #control our player fish with arrow keys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
                player.reverse()
            if event.key == pygame.K_RIGHT:
                player.move_right()
                player.forward()

    # draw background
    screen.blit(background, (0, 0))

    # update our fish location
    fishes.update()

    # update player fish
    player.update()

    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #use the tile size
            fishes.remove(fish) #remove the fish from the sprite group
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(tile_size, screen_height - 2 * tile_size)))

    #draw the fish
    fishes.draw(screen)

    #draw the player fish
    player.draw(screen)

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()