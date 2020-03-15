import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((800,600))
title = pygame.display.set_caption("Block")

# print 
font = pygame.font.Font(None, 60)
# white = 255,255,255
blue = 0,0,200
# textImage = font.render("Hi, pygame 2020-3-14 ", True, white)

def block():
    white = 255,255,255
    local_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    textImage = font.render("Hi, pygame {} ".format(local_time), True, white)
    screen.blit(textImage, (100, 200))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(blue)
    block()
    pygame.display.update()