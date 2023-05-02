import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the dimensions of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Set the size of each block of the snake and food
BLOCK_SIZE = 10

# Initialize pygame
pygame.init()

# Set the title of the window
pygame.display.set_caption("Snake Game")

# Set the dimensions of the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the font for the score and level display
font = pygame.font.SysFont('Calibri', 25, True, False)

# Define a function to draw the snake
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Define a function to generate the position of the food
def generate_food(snake_list):
    while True:
        food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
        food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
        if [food_x, food_y] not in snake_list:
            return [food_x, food_y]

# Define the main function for the game
def game():
    # Set the initial position and direction of the snake
    snake_x = SCREEN_WIDTH / 2
    snake_y = SCREEN_HEIGHT / 2
    snake_x_change = 0
    snake_y_change = 0

    # Initialize the snake list and its length
    snake_list = []
    snake_length = 1

    # Set the initial position of the food
    food_pos = generate_food(snake_list)

    # Set the initial score and level
    score = 0
    level = 1

    # Set the initial speed of the game
    clock = pygame.time.Clock()
    fps = 10

    # Game loop
    game_over = False
    while not game_over:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = BLOCK_SIZE
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -BLOCK_SIZE
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = BLOCK_SIZE
                    snake_x_change = 0

        # Check for border collision
        if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
            game_over = True

        # Update the position of the snake
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Check for food collision
        if snake_x == food_pos[0] and snake_y == food_pos[1]:
            # Increase the score and snake length
            score += 10
            snake_length += 1

    