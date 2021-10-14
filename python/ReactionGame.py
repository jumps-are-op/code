# Imports
import pygame
import sys
import random
import time

pygame.init()

def display_word(word,color, x,y):
    tmp = main_font.render(f"{word}", True, f"{color}") 
    screen.blit(tmp, tmp.get_rect(center=(x, y)))



# Screen + font
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Reaction Time")
main_font = pygame.font.SysFont("Roboto", 90)


# Game Stats
game_state = "Click to Start"

# Times
start_time, end_time = 0, 0


# Game loop

title = "Reaction Time Game"
while True:
    # Events Logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "Click to Start":
                game_state = "Waiting"

            elif game_state == "Test Starting":
                end_time = time.time()
                game_state = "Showing Results"
            
            elif game_state == "Showing Results":
                game_state = "Click to Start"

    screen.fill("white")

    # Game State Logic
    if game_state == "Click to Start":
        display_word("Click to Start","black",360,360)
        display_word(title,"red",360,50)

    elif game_state == "Waiting":
        screen.fill("yellow")

        display_word("Wait","black",360,360)

        pygame.display.update()

        delay_time = random.randrange(1,5)

        time.sleep(delay_time)

        game_state = "Test Starting"

        start_time = time.time()

    elif game_state == "Test Starting":
        screen.fill("green")
        display_word("Click Now!","black",360,360)

    elif game_state == "Showing Results":
        reaction_time = round ((end_time - start_time ) * 1000)
        display_word(f"Speed: {reaction_time / 1000} s","black",360,360)
        display_word(title,"red",360,50)
        pygame.display.update()
        time.sleep(1)
    
    # Update display
    pygame.display.update()
        
