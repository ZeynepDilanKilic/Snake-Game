import pygame
import sys

SQUARE_WIDTH = 750
PIXEL_WIDTH = 50
FPS = 10

class Display:
    def __init__(self):
        self.screen = pygame.display.set_mode([SQUARE_WIDTH] * 2)
        pygame.display.set_caption("Snake Game")
        self.font = pygame.font.Font("freesansbold.ttf", 32)

    def update(self, snake, bait, score):
        self.screen.fill("black")
        for segment in snake.body:
            pygame.draw.rect(self.screen, "green", segment)
        pygame.draw.rect(self.screen, "red", bait.position)
        score_text = self.font.render(f'Score: {score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()
    
    def show_game_over_screen(self, score):
        self.screen.fill("black")
        game_over_text = self.font.render("Game Over", True, "white")
        restart_text = self.font.render("Press R to Restart", True, "white")
        score_text = self.font.render(f"Score: {score}", True, "white")
        close_screen_text = self.font.render("Press ESC to Quit", True, "white")

        self.screen.blit(game_over_text, (SQUARE_WIDTH // 2 - game_over_text.get_width() // 2, SQUARE_WIDTH // 4))
        self.screen.blit(score_text, (SQUARE_WIDTH // 2 - score_text.get_width() // 2, SQUARE_WIDTH // 2))
        self.screen.blit(restart_text, (SQUARE_WIDTH // 2 - restart_text.get_width() // 2, SQUARE_WIDTH // 2 + 100))
        self.screen.blit(close_screen_text, (SQUARE_WIDTH // 2 - close_screen_text.get_width() // 2, SQUARE_WIDTH // 2 + 250))
        
        pygame.display.flip()
        self.wait_for_restart_or_exit()

    def wait_for_restart_or_exit(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            pygame.time.Clock().tick(FPS)
