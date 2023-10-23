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

#add pygame clock
clock = pygame.time.Clock() # allows us to set the frames per second

#Main loop
running = True
background = screen.copy()
draw_background(background)

for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*2), random.randint(tile_size, screen_height-tile_size)))

while running:
    for event in pygame.event.get()
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
        pygame.display.flip

        # set the frame rate
        clock.tick(60)

#quit pygame
pygame.quit()