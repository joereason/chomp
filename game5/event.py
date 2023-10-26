import pygame
import sys

from game_parameters import *
from background import draw_background

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Learning to get event types')

#Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('You pressed the up key')
            if event.key == pygame.K_DOWN:
                print('You pressed the down key')
            if event.key == pygame.K_LEFT:
                print('You pressed the left arrow')
            if event.key == pygame.K_RIGHT:
                print('You pressed the right arrow')



    #draw the background
    screen.blit(background, (0,0))

    #update the display
    pygame.display.flip()

    #limit the frame rate
    #clock.tick(60)



pygame.quit()
sys.exit()