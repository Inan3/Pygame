from re import T
import pygame

pygame.init()
pygame.display.set_mode((800, 540))

running = True
while running:
    for event in pygame.event.get():
        # Close window
        if event.type == pygame.QUIT:
            running = False