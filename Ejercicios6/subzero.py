import pygame
from pygame.sprite import Sprite


class SubZero(Sprite):

    def __init__(self, screen, settings):
        
        super().__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings

        self.image = pygame.image.load("imagenes/subzero_derecha.png")
        self.rect = self.image.get_rect()

        self.rect.y = self.screen_rect.height - self.rect.height
        self.rect.x = self.screen_rect.width / 2 - self.rect.width / 2

        self.mov_right = False
        self.mov_left = False


    def update(self):

        if self.mov_right:
            self.rect.x += 1

        elif self.mov_left:
            self.rect.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)