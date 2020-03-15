import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
title = pygame.display.set_caption("Drawing Arcs")


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,200)) # screen blue

   #绘制弧形
    color = 255,0,255
    position = 200,150,200,200
    start_angle = math.radians(0)
    stop_angle = math.radians(180)
    # print(start_angle,stop_angle)
    width =8
    pygame.draw.arc(screen,color,position,start_angle,stop_angle,width)

    pygame.display.update()
    
