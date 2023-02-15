import pygame
from pygame.locals import *
import classes

pygame.init();

#dimensions and attributes for the game's viewport window
window_width = 1000 #px
window_height = 333 #px
window_title = "Pong"

#boolean status that when toggled to False closes the viewport window
window_run_status = True

#creating the viewport window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,255,255)

background_colour = (0,0,0)

#specifications of each sprite on-screen
paddle_height = 50
paddle_width = 10
paddle_thickness = 1
ball_diameter = 15
ball_width = ball_diameter
ball_height = ball_diameter
ball_thickness = paddle_thickness

#initial positions for player 1, player 2, and the ball
player1_initial_top = (window_height / 2) - (paddle_height / 2)
player1_initial_left = window_width * 0.05
player1_initial_speed_horizontal = 0
player1_initial_speed_vertical = 0
player1_colour = WHITE

player2_initial_top = player1_initial_top
player2_initial_left = (window_width - (window_width * 0.05))
player2_initial_speed_horizontal = 0
player2_initial_speed_vertical = 0

ball_initial_top = ((window_height / 2) - (ball_diameter / 2))
ball_initial_left = ((window_width / 2) - (ball_diameter / 2))
ball_initial_speed_horizontal = 0
ball_initial_speed_vertical = 0

"""#dynamic characteristics of the game objects
player1_position = [player1_initial_left,player1_initial_top] #[x,y]
player2_position = [player2_initial_left,player2_initial_top] #[x,y]
ball_position = [ball_initial_left, ball_initial_top] #[x,y]
ball_velocity = [0,0] #[x,y]
paddle_speed = 1

#[left, top, width, height]
player1 = pygame.draw.rect(window, red, [player1_initial_left, player1_initial_top, paddle_width, paddle_height], paddle_thickness)
player2 = pygame.draw.rect(window, blue, [player2_initial_left, player2_initial_top, paddle_width, paddle_height], paddle_thickness)
ball = pygame.draw.rect(window, white, [ball_initial_left, ball_initial_top, ball_width, ball_height], ball_thickness)
pygame.display.flip()
"""

player1 = classes.Player(player1_initial_left, player1_initial_top, player1_initial_speed_horizontal, player1_initial_speed_vertical, paddle_height, paddle_width, player1_colour)

#player1 = pygame.Rect(player1_initial_left, player1_initial_top, paddle_width, paddle_height)

#keep viewport window open if game is running
while (window_run_status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_run_status = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.move_up()
    elif keys[pygame.K_DOWN]:
        player1.move_down()

    #update sprites
    player1.update()

    #clear the window
    window.fill(background_colour)

    #draw player sprite
    player1.draw(window)

    #update the display
    pygame.display.update()
    

pygame.quit()
quit()
