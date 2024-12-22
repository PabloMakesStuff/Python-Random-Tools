import tkinter
import customtkinter
import pygame
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_window = pygame.display.set_mode((600,400))
        self.clock = pygame.time.Clock()

        self.paddle_width = 10
        self.paddle_height = 60
        self.ball_width = 15
        self.ball_speed_x = 4
        self.ball_speed_y = 4
        self.paddle_speed = 10

        self.left_paddle = pygame.Rect(30, 150, self.paddle_width, self.paddle_height)
        self.right_paddle = pygame.Rect(560, 150, self.paddle_width, self.paddle_height)
        self.ball = pygame.Rect(300, 200, self.ball_width, self.ball_width)

        self.left_score = 0
        self.right_score = 0
        self.font = pygame.font.SysFont('Arial', 32)

        self.running = True

        self.update_game()

    def update_game(self):
        """Update the game state and refresh the game window."""
        if not self.running:
            return

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.left_paddle.top > 0:
            self.left_paddle.y -= self.paddle_speed
        if keys[pygame.K_s] and self.left_paddle.bottom < self.game_window.get_height():
            self.left_paddle.y += self.paddle_speed
        if keys[pygame.K_UP] and self.right_paddle.top > 0:
            self.right_paddle.y -= self.paddle_speed
        if keys[pygame.K_DOWN] and self.right_paddle.bottom < self.game_window.get_height():
            self.right_paddle.y += self.paddle_speed

        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.top <= 0 or self.ball.bottom >= self.game_window.get_height():
            self.ball_speed_y = -self.ball_speed_y

        if self.ball.colliderect(self.left_paddle) or self.ball.colliderect(self.right_paddle):
            self.ball_speed_x = -self.ball_speed_x

        if self.ball.left <= 0:
            self.right_score += 1
            self.reset_ball()
        if self.ball.right >= self.game_window.get_width():
            self.left_score += 1
            self.reset_ball()

        self.game_window.fill(WHITE)

        pygame.draw.rect(self.game_window, BLACK, self.left_paddle)
        pygame.draw.rect(self.game_window, BLACK, self.right_paddle)
        pygame.draw.ellipse(self.game_window, RED, self.ball)

        score_text = f"{self.left_score} - {self.right_score}"
        score_surface = self.font.render(score_text, True, BLACK)
        self.game_window.blit(score_surface, (200,10))

        pygame.display.update()

        self.clock.tick(60)

        self.after(10, self.update_game)

    def reset_ball(self):
        """Reset ball to the center of the screen."""
        self.ball.x = self.game_window.get_width() // 2 - self.ball_width // 2
        self.ball.y = self.game_window.get_height() // 2 - self.ball_width // 2
        self.ball_speed_x = -self.ball_speed_x