import pygame
import random

PIXEL_WIDTH = 50
SQUARE_WIDTH = 750

class Snake:
    def __init__(self):
        self.direction = (0, 0)
        self.length = 1
        self.body = [pygame.rect.Rect(0, 0, PIXEL_WIDTH - 2, PIXEL_WIDTH - 2)]
        self.body[0].center = self.generate_starting_position()


    def generate_starting_position(self):
        position_range = (PIXEL_WIDTH // 2, SQUARE_WIDTH - PIXEL_WIDTH // 2, PIXEL_WIDTH)
        return [random.randrange(*position_range), random.randrange(*position_range)]
    
    def move(self):
        if self.direction != (0, 0):
            new_head = self.body[-1].move(self.direction)
            self.body.append(new_head)
            if len(self.body) > self.length:
                self.body.pop(0)
    
    def grow(self):
        self.length += 1
    
    def check_collision_with_self(self):
        head = self.body[-1]
        for segment in self.body[:-1]:
            if head.colliderect(segment):
                return True
        return False
    
    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    
    def check_out_of_bounds(self):
        head = self.body[-1]
        return head.bottom > SQUARE_WIDTH or head.top < 0 or head.left < 0 or head.right > SQUARE_WIDTH
