import pygame
from snake import Snake
from bait import Bait
from display import Display

FPS = 10

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.snake = Snake()
        self.bait = Bait()
        self.display = Display()
        self.score = 0
    
    def reset(self):
        self.snake = Snake()
        self.bait = Bait()
        self.score = 0

    def check_game_over(self):
        if self.snake.check_out_of_bounds() or self.snake.check_collision_with_self():
            self.display.show_game_over_screen(self.score)
            self.reset()
    
    def handle_input(self):
        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_UP]: #and not self.snake.direction_x:
            
            self.snake.change_direction((0, -50))
 
        if keys[pygame.K_DOWN]:
            self.snake.change_direction((0, 50))

        if keys[pygame.K_LEFT]:
            self.snake.change_direction((-50, 0))

        if keys[pygame.K_RIGHT]:# and not self.snake.direction_y:
            self.snake.change_direction((50, 0))


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.handle_input()
            self.snake.move()

            if self.snake.body[-1].colliderect(self.bait.position):
                self.snake.grow()
                self.bait.relocate()
                self.score += 10

            self.check_game_over()
            self.display.update(self.snake, self.bait, self.score)
            self.clock.tick(FPS)
        
        pygame.quit()
