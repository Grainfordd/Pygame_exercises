import pygame
from pygame.sprite import Group
from game_stats import GameStats
import sys
from settings import Settings
import gf
from ball import Ball
from subzero import SubZero

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Pelota")
settings = Settings()

ball = Ball(screen)
subzero = SubZero(screen, settings)

pelota = Group()
pelota.add(ball)

stats = GameStats(settings)

while True:
    screen.fill(settings.bg_color)    
    gf.check_events(subzero)
    pelota.draw(screen)
    subzero.blitme()
    
    if stats.game_active:

        if len(pelota) == 0:
            ball = Ball(screen)
            pelota.add(ball)
            pelota.draw(screen)

        pelota.update()

        gf.colision(subzero, pelota, ball)
        subzero.update()


        gf.ball_falls(screen, pelota, stats) 
        print (stats.lifes)

    pygame.display.flip()

    