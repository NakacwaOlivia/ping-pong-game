import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
BALL_RADIUS = 15
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_SPEED = 10

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Ping Pong Game')

# Define the paddles and ball
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_RADIUS // 2, WINDOW_HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
left_paddle = pygame.Rect(10, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WINDOW_WIDTH - 20, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Game loop
clock = pygame.time.Clock()

ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y
left_paddle_speed = 0
right_paddle_speed = 0

left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = WINDOW_WIDTH // 2 - BALL_RADIUS // 2
    ball.y = WINDOW_HEIGHT // 2 - BALL_RADIUS // 2
    ball_speed_x = BALL_SPEED_X if ball_speed_x > 0 else -BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y if ball_speed_y > 0 else -BALL_SPEED_Y

def draw_score():
    left_score_text = font.render(f"{left_score}", True, WHITE)
    right_score_text = font.render(f"{right_score}", True, WHITE)
    screen.blit(left_score_text, (WINDOW_WIDTH // 4, 20))
    screen.blit(right_score_text, (3 * WINDOW_WIDTH // 4, 20))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                left_paddle_speed = -PADDLE_SPEED
            if event.key == K_s:
                left_paddle_speed = PADDLE_SPEED
            if event.key == K_UP:
                right_paddle_speed = -PADDLE_SPEED
            if event.key == K_DOWN:
                right_paddle_speed = PADDLE_SPEED
        if event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                left_paddle_speed = 0
            if event.key == K_UP or event.key == K_DOWN:
                right_paddle_speed = 0

    # Move the paddles
    left_paddle.y += left_paddle_speed
    right_paddle.y += right_paddle_speed

    # Prevent paddles from going out of bounds
    left_paddle.y = max(min(left_paddle.y, WINDOW_HEIGHT - PADDLE_HEIGHT), 0)
    right_paddle.y = max(min(right_paddle.y, WINDOW_HEIGHT - PADDLE_HEIGHT), 0)

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Ball goes out of bounds
    if ball.left <= 0:
        right_score += 1
        reset_ball()

    if ball.right >= WINDOW_WIDTH:
        left_score += 1
        reset_ball()

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)

    # Draw score
    draw_score()

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)
