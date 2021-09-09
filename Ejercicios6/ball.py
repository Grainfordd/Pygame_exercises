import pygame
from pygame.sprite import Sprite
from random import randint


class Ball(Sprite):

    def __init__(self, screen):

        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect() 
        
        self.image = pygame.image.load("imagenes/pelota2.png")
        self.rect = self.image.get_rect()
        
        self.rect.x = randint(0, 1440 - self.rect.width)

    def update(self):
        self.rect.y += 1
        if self.rect.y  >= self.screen_rect.bottom:
            self.rect.y = 0
            self.rect.x = randint(0, 1440 - self.rect.width)
    def blitme(self):
        self.screen.blit(self.image, self.rect)