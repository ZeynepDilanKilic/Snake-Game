# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 03:36:30 2024

@author: ZeynepDilanKılıç
"""

import pygame
import random

pygame.init()
square_width = 750
pixel_width = 50
screen = pygame.display.set_mode([square_width] * 2)
clock = pygame.time.Clock()
running = True


def generate_starting_position():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]


def reset():
    bait.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    return snake_pixel.copy()


def is_out_of_bounds():
    return snake_pixel.bottom > square_width or snake_pixel.top < 0 \
        or snake_pixel.left < 0 or snake_pixel.right > square_width


snake_pixel = pygame.rect.Rect(0, 0, pixel_width - 2, pixel_width - 2)
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

bait = pygame.rect.Rect(0, 0, pixel_width - 2, pixel_width - 2)
bait.center = generate_starting_position()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    if is_out_of_bounds():
        snake_length = 1
        bait.center = generate_starting_position()
        snake_pixel.center = generate_starting_position()
        snake = [snake_pixel.copy()]

    if snake_pixel.center == bait.center:
        bait.center = generate_starting_position()
        snake_length += 1
        snake.append(snake_pixel.copy())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_direction = (0, - pixel_width)
    if keys[pygame.K_DOWN]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_LEFT]:
        snake_direction = (-pixel_width, 0)
    if keys[pygame.K_RIGHT]:
        snake_direction = (pixel_width, 0)


    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)
        

    pygame.draw.rect(screen, "red", bait)

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_length:]

    pygame.display.flip()

    clock.tick(8)

pygame.quit()

