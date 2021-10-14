import pygame
import sys
import random
import time
from pygame import mouse

from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP, K_a, K_d, K_s, K_w
pygame.init()

display = pygame.display.set_mode((700,720))

pygame.display.set_caption("snek")


def display_word(word,x,y,size,color):
    main_font = pygame.font.SysFont("Roboto", size)
    tmp = main_font.render(f"{word}", True, f"{color}") 
    x += len(word) * size/(len(word)/2)  
    display.blit(tmp, tmp.get_rect(center=(x, y)))

def draw_map():
    for y in range(20,720):
        for x in range(0,700):
            if y % 20 == 0:
                if x % 20 == 0:
                    pygame.draw.rect(display, "black", pygame.Rect(x, y, 19, 19))

def draw_snake(snake,color):
    if (len(snake) % 2 == 1):
        snake.remove(snake[len(snake)-1]) #Safety First
    n = len(snake) / 2
    x = -2
    while n:
        x += 2
        y = x + 1
        snake[x] = snake[x] % 35
        snake[y] = snake[y] % 35
        snake_x = snake[x] * 20
        snake_y = snake[y] * 20
        snake_y += 20
        pygame.draw.rect(display, color, pygame.Rect(snake_x, snake_y, 19, 19))
        n -= 1

def draw_food(food):
    if (len(food) % 2 == 1):
        food.remove(food[len(food)-1]) #Safety First
    n = len(food) / 2
    x = -2
    while n:
        x += 2
        y = x + 1
        food[x] = food[x] % 35
        food[y] = food[y] % 35
        food_x = food[x] * 20
        food_y = food[y] * 20
        food_y += 20
        pygame.draw.rect(display, "green", pygame.Rect(food_x, food_y, 19, 19))
        n -= 1

def move_snake(snake, Move):
    snake[0] += Move[0]
    snake[1] += Move[1]
    if (len(snake) % 2 == 1):
        snake.remove(snake[len(snake)-1]) #Safety First
    n = (len(snake) / 2) - 1
    x = len(snake)
    while n:
        x -= 2
        y = x + 1
        snake[x] = snake[x-2] 
        snake[y] = snake[y-2]
        n -= 1

def check_if_snake_eat_food(snake,food):
    n = (len(food) / 2 )
    x = -2
    while n:
        x += 2
        y = x + 1
        if (snake[0] == food[x] and snake[1] == food[y]):
            x -= 1
            y -= 1
            del food[x]
            del food[y]
            food.append(random.randrange(0,35))
            food.append(random.randrange(0,35))
            snake.append(snake[len(snake) - 3] - (snake[len(snake) - 5] - snake[len(snake) - 4]))
            snake.append(snake[len(snake) - 2] - (snake[len(snake) - 4] - snake[len(snake) - 2]))
            return True
        n -= 1
    return False
def check_if_hit(snake,obj):
    n = (len(obj) / 2 )
    x = -2
    while n:
        x += 2
        y = x + 1
        if (snake[0] == obj[x] and snake[1] == obj[y]):
            return True
        n -= 1
    return False
def endGame(player):
    while True:
        display.fill("black")
        if player != "Draw":
            display_word(f"{player} WON !!", 250, 300, 50,"white")
        else:
            display_word("Draw", 250, 300, 50,"red")
        display_word("Left click or Space to Restart", 250, 450, 50,"white")
        display_word("Right click or Esc to Exit", 250, 500, 50,"white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            start()
        elif mouse_pressed[2]:
            pygame.quit()
            sys.exit()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            start()
        elif pressed_keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()
        
        pygame.display.update()


def start():
    snake1 = [17,17,16,17,15,17,16,17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    snake2 = [17,17,18,17,19,17,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    Move1 = [0,1]
    Move2 = [0,-1]
    score1 = 0
    score2 = 0
    difficulty = 1 #From 1 - 10 if more it will crash
    difficulty = difficulty * 10        
    slow = 100 - difficulty
    food = []
    food.append(random.randrange(0,35))
    food.append(random.randrange(0,35))
    food.append(random.randrange(0,35))
    food.append(random.randrange(0,35))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        display.fill("white")

        draw_map()
    #snake1
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w] and Move1 != [0,1]:
            Move1 = [0,-1]
        elif pressed_keys[K_s] and Move1 != [0,-1]:
            Move1 = [0,1]
        elif pressed_keys[K_d] and Move1 != [-1,0]:
            Move1 = [1,0]
        elif pressed_keys[K_a] and Move1 != [1,0]:
            Move1 = [-1,0]

        draw_food(food)
        move_snake(snake1,Move1)
        draw_snake(snake1,"red")
        if check_if_snake_eat_food(snake1,food) == True:
            score1 += difficulty
    #snake2
        if pressed_keys[K_UP] and Move2 != [0,1]:
            Move2 = [0,-1]
        elif pressed_keys[K_DOWN] and Move2 != [0,-1]:
            Move2 = [0,1]
        elif pressed_keys[K_RIGHT] and Move2 != [-1,0]:
            Move2 = [1,0]
        elif pressed_keys[K_LEFT] and Move2 != [1,0]:
            Move2 = [-1,0]
        move_snake(snake2,Move2)
        draw_snake(snake2,"blue")
        if check_if_snake_eat_food(snake2,food) == True:
            score2 += difficulty
        pygame.draw.rect(display, "black", pygame.Rect(0, 0, 700, 20))
        snake2_hit = check_if_hit(snake2,snake1)
        snake1_hit = check_if_hit(snake1,snake2)
        if snake1_hit and snake2_hit == True:
            endGame("Draw")
        elif snake2_hit == True:
            endGame("Player 1")
        elif snake1_hit == True:
            endGame("Player 2")
        display_word("wasd", -30, 10, 35, "red")
        display_word("arrows", 550, 10, 35, "blue")
        display_word("kill the other player to win", 350, 10, 35, "green")
        pygame.display.update()
        pygame.time.delay(slow)
start()