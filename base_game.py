import pygame
from pygame.locals import *
import classes
from random import random
from random import uniform

pygame.init()

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
paddle_bound_x = (0, window_width)
paddle_bound_y = (0, window_height)
ball_diameter = 15
ball_width = ball_diameter
ball_height = ball_diameter
ball_thickness = paddle_thickness
ball_bound_x = (0 + ball_width/2, window_width - ball_width/2)
ball_bound_y = (0 + ball_width/2, window_height - ball_width/2)

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
player2_colour = BLUE

ball_initial_top = ((window_height / 2) - (ball_diameter / 2))
ball_initial_left = ((window_width / 2) - (ball_diameter / 2))
ball_colour = RED

#setting initial speed and horizontal direction of ball
if random() > 0.5:
    ball_initial_speed_horizontal = 0.66
else:
    ball_initial_speed_horizontal = -0.66

#getting a random vertical velocity so that the ball doesn't have the same tragectory every time
ball_initial_speed_vertical = 0
while ball_initial_speed_vertical == 0:
    ball_initial_speed_vertical = uniform(-0.33, 0.33)

player1 = classes.Player(player1_initial_left, player1_initial_top, player1_initial_speed_horizontal, player1_initial_speed_vertical, paddle_height, paddle_width, player1_colour, paddle_bound_x, paddle_bound_y)
player2 = classes.Player(player2_initial_left, player2_initial_top, player2_initial_speed_horizontal, player2_initial_speed_vertical, paddle_height, paddle_width, player2_colour, paddle_bound_x, paddle_bound_y)
ball = classes.ball(ball_initial_left, ball_initial_top, ball_initial_speed_horizontal, ball_initial_speed_vertical, ball_width, ball_height, ball_bound_x, ball_bound_y, ball_colour)

#keep viewport window open if game is running
while (window_run_status):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_run_status = False

    #controls
    keys = pygame.key.get_pressed()
    #joint controls between player1 and player2
    if keys[pygame.K_w] and keys[pygame.K_UP]:
        player1.move_up()
        player2.move_up()
    elif keys[pygame.K_s] and keys[pygame.K_DOWN]:
        player1.move_down()
        player2.move_down()
    elif keys[pygame.K_w] and keys[pygame.K_DOWN]:
        player1.move_up()
        player2.move_down()
    elif keys[pygame.K_s] and keys[pygame.K_UP]:
        player1.move_down()
        player2.move_up()
    #player1 sole controls
    elif keys[pygame.K_w]:
        player1.move_up()
    elif keys[pygame.K_s]:
        player1.move_down()
    #player2 sole controls
    elif keys[pygame.K_UP]:
        player2.move_up()
    elif keys[pygame.K_DOWN]:
        player2.move_down()
    #quit control
    elif keys[pygame.K_ESCAPE]:
        window_run_status = False


    #ball collision with wall
    if ball.position[0] <= ball.bounds_x[0] or ball.position[0] >= ball.bounds_x[1]:
        ball.collide_along_x()
        #ball.stop()
    if ball.position[1] < 0 or ball.position[1] > window_height:
        ball.collide_along_y()

    #ball collision with paddles
    if ball.hitbox.colliderect(player1.hitbox):
        ball.paddle_collide()
    elif ball.hitbox.colliderect(player2.hitbox):
        ball.paddle_collide()


    #update sprites
    player1.update()
    player2.update()
    ball.update()

    #clear the window
    window.fill(background_colour)

    #draw player sprite
    player1.draw(window)
    player2.draw(window)
    ball.draw(window)

    #update the display
    pygame.display.update()
    

pygame.quit()
quit()
