import pygame
import sys


def check_events(subzero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                subzero.image = pygame.image.load("imagenes/subzero_izquierda.png")
                subzero.mov_left = True
            elif event.key == pygame.K_d:
                subzero.image = pygame.image.load("imagenes/subzero_derecha.png")
                subzero.mov_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                subzero.mov_left = False
            if event.key == pygame.K_d:
                subzero.mov_right = False

def colision(subzero, pelota, ball):

    colissions = pygame.sprite.spritecollideany(subzero, pelota)

    if colissions:
        pelota.remove(ball)

def ball_falls(screen, pelota, stats):
    if stats.lifes == 0:
        stats.game_active = False
    screen_rect = screen.get_rect()
    for pelotas in pelota.copy():
        if pelotas.rect.bottom >= screen_rect.bottom:
            pelota.remove(pelotas)
            stats.lifes -= 1

