import pygame

player_speed_x = 0.75
player_speed_y = 0.75

class Player(pygame.sprite.Sprite):
    def __init__(self, x:int, y:int, speed_x:int, speed_y:int, height:int, width:int, colour:tuple) -> None:
        super().__init__()
        self.position = (x,y)
        self.speed = (speed_x, speed_y)
        self.height = height
        self.width = width
        self.colour = colour

    def update(self):
        self.position = (self.position[0] + self.speed[0], self.position[1] - self.speed[1])
        self.speed = (0,0)
    
    def draw(self, surface) :
        pygame.draw.rect(surface, self.colour, [self.position[0], self.position[1], self.width, self.height])
        #pygame.draw.rect(window, blue, [player2_initial_left, player2_initial_top, paddle_width, paddle_height], paddle_thickness)

    def move_up(self):
        self.speed = (0, player_speed_y)

    def move_down(self):
        self.speed = (0, -player_speed_y)

    def move_left(self):
        self.speed = (-player_speed_x, 0)

    def move_right(self):
        self.speed = (player_speed_x, 0)


class ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y) -> None:
        super().__init__()
        self.position = (x,y)
        self.speed = (speed_x, speed_y)

    def update(self):
        self.position = (self.position[0] + self.speed[0], self.position[1] - self.speed[1])
    
    def draw(self, surface) :
        pygame.draw.circle(surface, (255, 0, 0), self.position, 10)

    def collide_along_x(self):
        self.speed = (-self.speed[0], self.speed[1])
    def collide_along_y(self):
        self.speed = (self.speed[0], -self.speed[1])