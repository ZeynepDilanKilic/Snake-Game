import pygame
import random

PIXEL_WIDTH = 50
SQUARE_WIDTH = 750

class Bait:
    def __init__(self):
        self.position = pygame.rect.Rect(0, 0, PIXEL_WIDTH - 2, PIXEL_WIDTH - 2)
        self.position.center = self.generate_starting_position()
    
    def generate_starting_position(self):
        position_range = (PIXEL_WIDTH // 2, SQUARE_WIDTH - PIXEL_WIDTH // 2, PIXEL_WIDTH)
        return [random.randrange(*position_range), random.randrange(*position_range)]
    
    def relocate(self):
        self.position.center = self.generate_starting_position()
