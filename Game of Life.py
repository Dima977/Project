import pygame
import time
import random
import numpy as np
import os
import grid

#Space - Пауза
#ЛКМ - закрасить клетку
#ПКМ - удалить клетку
#-/+ - уменьшить/увеличить скорость генерации
#Esc - выход

os.environ["SDL_VIDEO_CENTERED"]='1'

#Размеры окна
width, height = 480,510
size = (width, height)

#Создаем окно
pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

#Константы цветов RGB
black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 0, 100)
white = (255, 255, 255)

#Толщина и размер сетки
scaler = 30
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_KP_MINUS:
                fps=fps-1
            if event.key == pygame.K_KP_PLUS:
                fps=fps+1
    
    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)

    if pygame.mouse.get_pressed()[2]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandriMouse(mouseX, mouseY)



    pygame.display.update()

pygame.quit()
