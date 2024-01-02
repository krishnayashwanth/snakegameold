import pygame
import time
import random

pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Initialize snake
snake_list = []
snake_length = 1
snake_head = [width // 2, height // 2]

# Initial direction
direction = 'RIGHT'

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Function to display the score
def your_score(score):
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, [0, 0])
# Function to add food
def add_food(food_position, snake_list):
    while food_position in snake_list:
        food_position = [random.randrange(1, width // snake_block) * snake_block, random.randrange(1, height // snake_block) * snake_block]
    return food_position

# Function to draw the food
def draw_food(food_position):
    pygame.draw.rect(window, red, [food_position[0], food_position[1], snake_block, snake_block])

# Variables to track the food
food_position = [random.randrange(1, width // snake_block) * snake_block, random.randrange(1, height // snake_block) * snake_block]
food_spawn = True

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'

    # Move the snake
    if direction == 'LEFT':
        snake_head[0] -= snake_block
    elif direction == 'RIGHT':
        snake_head[0] += snake_block
    elif direction == 'UP':
        snake_head[1] -= snake_block
    elif direction == 'DOWN':
        snake_head[1] += snake_block

    # Check for collisions with the food
    if snake_head == food_position:
        food_spawn = False
        snake_length += 1

    # Check for collisions with the walls
    if (
        snake_head[0] < 0
        or snake_head[0] >= width
        or snake_head[1] < 0
        or snake_head[1] >= height
    ):
        game_over = True

    # Update the display
    window.fill(black)
    draw_snake(snake_block, snake_list)
    draw_food(food_position)
    your_score(snake_length - 1)

    # Update the snake's body
    snake_head_copy = snake_head[:]
    snake_list.append(snake_head_copy)
    if len(snake_list) > snake_length:
        del snake_list[0]

    #Spawn food
    if not food_spawn:
        food_position = add_food(food_position, snake_list)
    food_spawn = True

    # Check for collisions with itself
    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    pygame.display.update()

    # Control the snake's speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
