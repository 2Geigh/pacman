import pygame
pygame.init();

#dimensions and attributes for the game's viewport window
windowWidth = 224 #px
windowHeight = 288 #px
windowTitle = "Pac-Man"

#boolean status that when toggled to False closes the viewport window
windowRunning = True;

#creating the viewport window
pygame.display.set_mode((windowWidth,windowHeight));
pygame.display.set_caption(windowTitle);

#keep viewport window open if game is running
while (windowRunning):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            windowRunning = false;