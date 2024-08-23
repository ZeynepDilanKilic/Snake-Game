
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 03:36:30 2024

@author: ZeynepDilanKılıç
"""

import pygame
import random
import sys

pygame.init()
pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 32)

square_width = 750
pixel_width = 50
screen = pygame.display.set_mode([square_width] * 2)
clock = pygame.time.Clock()
running = True

snake_pixel = pygame.rect.Rect(0, 0, pixel_width - 2, pixel_width - 2)

snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

bait = pygame.rect.Rect(0, 0, pixel_width - 2, pixel_width - 2)

score = 0

direction_x = False
direction_y = False

def generate_starting_position():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]

def reset():
    bait.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    return snake_pixel.copy()


def is_out_of_bounds():
    return snake_pixel.bottom > square_width  or snake_pixel.top < 0 \
        or snake_pixel.left < 0 or snake_pixel.right > square_width 

def is_snake_bite_itself():
    head = snake[-1] # yılanın başı son eklenen diktörtgen
    for segment in snake[:-1]:
        if head.colliderect(segment):
            return True
    return False


def restart_game():
    global snake, score, snake_length, direction_x, direction_y, snake_direction  # Global değişkenleri tanımla
    show_game_over_screen()
    bait.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    snake = [snake_pixel.copy()]
    score = 0
    snake_length = 1
    direction_x = False
    direction_y = False
    snake_direction = (0, 0)  # Yönü sıfırla, böylece oyun başlangıcında hareket etmiyor


def check_game_over():
    if is_out_of_bounds():
        restart_game()
        return True
    elif is_snake_bite_itself():
        restart_game()
        return True
    return False

def show_game_over_screen():
    screen.fill("black")
    game_over_text = font.render("Game Over", True, "white")
    restart_text = font.render("Press R to Restart", True, "white")
    score_text = font.render(f"Score: {score}", True, "white")
    close_screen_text =  font.render("Press ESC to Quit", True, "white")
        
    screen.blit(game_over_text, (square_width // 2 - game_over_text.get_width() // 2, square_width // 4))
    screen.blit(score_text, (square_width // 2 - score_text.get_width() // 2, square_width // 2))
    screen.blit(restart_text, (square_width // 2 - restart_text.get_width() // 2, square_width // 2 + 100))
    screen.blit(close_screen_text, (square_width // 2 - close_screen_text.get_width() // 2, square_width // 2 + 250))
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Programı tamamen kapat
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()  # Programı tamamen kapat
                
            
        pygame.display.flip()
        clock.tick(10)

snake_pixel.center = generate_starting_position()
bait.center = generate_starting_position()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    

    if check_game_over():
        print("Check game over truee")
        
    
    if snake_pixel.center == bait.center:
        bait.center = generate_starting_position()
        snake_length += 1
        snake.append(snake_pixel.copy())
        score += 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if not direction_x:
            snake_direction = (0, -pixel_width)
            direction_x = True
            direction_y = False
    if keys[pygame.K_DOWN]:
        if not direction_x:
            snake_direction = (0, pixel_width)
            direction_x = True
            direction_y = False
    if keys[pygame.K_LEFT]:
        if not direction_y:
            snake_direction = (-pixel_width, 0)
            direction_x = False
            direction_y = True
    if keys[pygame.K_RIGHT]:
        if not direction_y:
            snake_direction = (pixel_width, 0)
            direction_x = False
            direction_y = True

    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)
    
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.draw.rect(screen, "red", bait)

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_length:]

    pygame.display.flip()
    clock.tick(10)

pygame.quit()