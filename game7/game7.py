import pygame
import sys
import random

#Import all our necessary files
from fish import Fish, fishes
from background import draw_background, add_fish, add_enemies
from game_parameters import *
from player import Player
from enemy import enemies, Enemy

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
add_fish(5)

#Add enemies to the screen
add_enemies(5)

#Draw player fish
player = Player(screen_width/2, screen_height/2)

#load new font to keep source
score = 0
score_font = pygame.font.Font("../assets/Fonts/Black_Crayon.ttf", 60)

#load a sound to our game
chomp = pygame.mixer.Sound('../assets/sounds/villager.wav')

#Placeholder for a orange player fish
while running:
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            running = False
        #control our player fish with arrow keys
        #player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move_up()
            if event.key == pygame.K_s:
                player.move_down()
            if event.key == pygame.K_a:
                player.move_left()
                player.reverse()
            if event.key == pygame.K_d:
                player.move_right()
                player.forward()

        if event.type == pygame.KEYUP:
            player.stop()

    # draw background
    screen.blit(background, (0, 0))

    # update our fish location
    fishes.update()

    #draw enemy fish
    enemies.update()

    # update player fish
    player.update()

    #check for collisions between our player and fish - use group collision method
    result = pygame.sprite.spritecollide(player, fishes, True)
    #print(result)
    if result:
        #play chomp sound
        pygame.mixer.Sound.play(chomp)

        score += len(result)

        #draw more green fish on the screen
        for _ in range(len(result)):
            add_fish(1)
            #fishes.add(Fish(random.randint(screen_width, screen_width * 1.5),
            #            random.randint(tile_size, screen_height - 2 * tile_size)))

    #check if player collides with enemy fish
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        for _ in range(len(result)):
            add_enemies(1)

    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #use the tile size
            fishes.remove(fish) #remove the fish from the sprite group
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(tile_size, screen_height - 2 * tile_size)))

    for enemy in enemies:
        if fish.rect.x < -fish.rect.width:  # use the tile size
            enemies.remove(enemy)  # remove the fish from the sprite group
            enemies.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(tile_size, screen_height - 2 * tile_size)))

    #draw the fish
    fishes.draw(screen)

    #draw the player fish
    player.draw(screen)

    enemies.draw(screen)

    #blit score text
    text = score_font.render(f'{score}', True, (255, 0, 0))
    screen.blit(text, (screen_width - text.get_width()/2-15, 0))

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()