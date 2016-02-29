# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from random import randint
from math import *
import time
from gameobjects.vector2 import *
import os
import copy


screen_size = (640, 480)
body_size = (10, 10)
speed = 100
WHITE = (255 ,255 ,255)
init_pos = Vector2(100, 300)
class Objects:
    def __init__(self, pos, size):
        self.x = pos[0]
        self.y = pos[1]
        self.width = size[0]
        self.height = size[1]



class snakeBody():
    def __init__(self, pos, body_size):
        self.pos = pos
        self.surf = pygame.Surface(body_size)
        self.surf.fill(WHITE)



def check(pos, screen_size):
    if pos.x <=0 or pos.x + body_size[0] >= screen_size[0] or pos.y <= 0 or pos.y + body_size[1] >= screen_size[1]:
        return True
    else:
        return False


def update(snake):
    idx = len(snake) - 1
    while idx > 0:
        #snake[idx].pos = snake[idx - 1].pos
        snake[idx].pos = copy.deepcopy(snake[idx - 1].pos)
        idx -= 1

def init_snake():
    snake = []
    for i in range(5):
        body_pos = (init_pos.x - i * 10, init_pos.y)
        body = snakeBody(Vector2(body_pos), body_size)
        snake.append(body)
    return snake

def run():
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)

    clock = pygame.time.Clock()
    ball_direction = Vector2(1, 0)
    my_font = pygame.font.SysFont('arial', 64)
    snake = init_snake()
    print 'init success'
    while True:
        if check(snake[0].pos,screen_size):
            text = 'you lose'
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                font_surface = my_font.render(text, True, (255, 255, 255))
                font_size = font_surface.get_size()
                screen.blit(font_surface, ((screen_size[0] - font_size[0])/ 2, (screen_size[1] - font_size[1]) / 2))
                pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    ball_direction.x = 0
                    ball_direction.y = 1
                elif event.key == K_UP:
                    ball_direction.x = 0
                    ball_direction.y = -1
                elif event.key == K_LEFT:
                    ball_direction.y = 0
                    ball_direction.x = -1
                elif event.key == K_RIGHT:
                    ball_direction.y = 0
                    ball_direction.x = 1
        time_passed = clock.tick() / 1000.0
        distance = ball_direction * time_passed * speed
        #time.sleep(100. / 1000.)
        snake[0].pos += distance
        screen.fill((0,0,0))
        for body in snake:
            print body.pos,
            screen.blit(body.surf, (body.pos.x, body.pos.y))
        print '\n'
        pygame.display.update()

def test():
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    snake = init_snake()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.fill((0,0,0))
        #print len(snake)
        for body in snake:
            #print body.pos,
            screen.blit(body.surf, (body.pos.x, body.pos.y))
        pygame.display.update()

if __name__ == '__main__':
    run()
    #test()