#A pygame sprite class for a player fish

import pygame
import random
from game_parameters import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # TODO: Turn the fish in the opposite direction if moving the other way
        self.image = pygame.image.load('../assets/sprites/orange_fish.png').convert()
        self.forward_image = self.image
        self.reverse_image = pygame.transform.flip(self.image, True, False)
        self.image.set_colorkey((0, 0, 0))
        self.reverse_image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed  = -1*PLAYER_SPEED

    def move_down(self):
        self.y_speed  = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1*PLAYER_SPEED

    def move_right(self):
        self.x_speed = PLAYER_SPEED

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def reverse(self):
        self.image = self.reverse_image

    def forward(self):
        self.image = self.forward_image

    def update(self):
        # TODO: need to check if player fish went off the screen
        self.x += self.x_speed
        if self.x > screen_width-tile_size:
            self.x = screen_width-tile_size
        elif self.x < 0:
            self.x = 0
        self.y += self.y_speed
        if self.y > screen_height-tile_size:
            self.y = screen_height-tile_size
        elif self.y < 0:
            self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)
