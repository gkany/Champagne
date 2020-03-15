import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
title = pygame.display.set_caption("Drawing Line")


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,200)) # screen blue

    color = 255,255,0
    width = 8
    pygame.draw.line(screen, color, (100,100), (500,300), width)
    pygame.display.update()
    
