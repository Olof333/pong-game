import pygame
from paddle import Paddle

WIDTH = 600
HEIGHT = 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Board:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    pass


class Game:
    all_sprites = pygame.sprite.Group()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)