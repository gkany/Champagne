import pygame
from pygame.locals import *
import math
import sys
import time

pygame.init()
screen = pygame.display.set_mode((600,600))
title = pygame.display.set_caption("The Pie Game")

myfont = pygame.font.Font(None,60)

color = 200,80,60
width = 4
x = 300
y = 250
radius = 200
position = x-radius,y-radius,radius*2,radius*2


#设置按键1，2，3，4变量
piece1 = False
piece2 = False
piece3 = False
piece4 = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True
    #清屏
    screen.fill((0,0,200))

    #绘制4个数字
    textImage1 = myfont.render("1",True,color)
    text1=screen.blit(textImage1,(x+radius/2-20,y-radius/2))
    #print("text1==",text1)
    textImage2 = myfont.render("2",True,color)
    text2=screen.blit(textImage2,(x-radius/2,y-radius/2))
    #print("text2==", text2)
    textImage3 = myfont.render("3",True,color)
    text3=screen.blit(textImage3,(x-radius/2,y+radius/2-20))
    #print("text3==", text3)
    textImage4 = myfont.render("4",True,color)
    text4=screen.blit(textImage4,(x+radius/2-20,y+radius/2-20))
    #print("text4==", text4)

    #判断是否绘制饼
    if piece1:
        start_angle = math.radians(0)
        end_angle = math.radians(90)
        arc1=pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        # print("arc1==",arc1)
        line1=pygame.draw.line(screen,color,(x,y),(x,y-radius),width)
        # print("line1==",line1)
        line2=pygame.draw.line(screen,color,(x,y),(x+radius,y),width)
        # print("line2==",line2)
    if piece2:
        start_angle = math.radians(90)
        end_angle = math.radians(180)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y-radius),width)
        pygame.draw.line(screen,color,(x,y),(x-radius,y),width)
    if piece3:
        start_angle = math.radians(180)
        end_angle = math.radians(270)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x-radius,y),width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
    if piece4:
        start_angle = math.radians(270)
        end_angle = math.radians(360)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)

    #是否4个饼都绘制完成
    if piece1 and piece2 and piece3 and piece4:
        color = 0,255,0
        # time.sleep(2)
        piece1, piece2, piece3, piece4 = False, False, False, False

    pygame.display.update()