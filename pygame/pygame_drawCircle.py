import pygame
import sys 

pygame.init()
screen = pygame.display.set_mode((800, 600))

pos_x, pos_y = 300, 250
vel_x, vel_y = 2, 1

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,200)) #blue
    pos_x += vel_x
    pos_y += vel_y

    if pos_x > 800 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 600 or pos_y < 0:
        vel_y = -vel_y
    
    color = 255,255,0
    radius = 60
    width = 0
    pos = pos_x,pos_y
    pygame.draw.circle(screen, color, pos, radius, width)

    pygame.display.update()