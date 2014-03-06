import pygame, sys
from pygame.locals import *

class Point(object):
    maximum_x_size = None
    maximum_y_size = None

    @classmethod
    def setup_class(cls, maximum_x_size, maximum_y_size):
        cls.maximum_x_size = maximum_x_size
        cls.maximum_y_size = maximum_y_size

    def __init__(self, x, y):
        x = int(x)
        if x < 0 or x > self.maximum_x_size:
            raise ValueError("invalid value for x")
        if y < 0 or y > self.maximum_y_size:
            raise ValueError("invalid value for y")
        self.x = x
        self.y = y

class Person(object):
    @classmethod
    def setup_class(self, screen):
        self.screen = screen

    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.circle(
            self.screen,
            Colors.red,
            (self.location.x, self.location.y),
            3,
            0
        )

class Colors(object):
    # set up the colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

class Game(object):
    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y

        # set up the window
        pygame.init()
        self.screen = pygame.display.set_mode((window_x, window_y), 0, 32)
        pygame.display.set_caption('Drawing')
        self.setup_game()

    def setup_game(self):
        Point.setup_class(self.window_x, self.window_y)
        Person.setup_class(self.screen)
        self.draw_list = [
            Person(60, 60),
            Person(120, 60)
        ]

    def loop(self):
        t = 0
        while True:
            t = (t + 1) % 255
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.setup_update(t)
            pygame.display.update()

    def setup_update(self, time):
        self.screen.fill(Colors.white)
        for entity in self.draw_list:
            entity.draw()
        #pygame.draw.line(self.screen, Colors.blue, (60, 60), (120, 60), 4)
        #pygame.draw.line(self.screen, Colors.blue, (120, 60), (60, 120))
        #pygame.draw.line(self.screen, Colors.blue, (60, 120), (120, 120), 4)
        #pygame.draw.circle(self.screen, Colors.blue, (300, 50), 20, 0)
        #pygame.draw.ellipse(self.screen, Colors.red, (300, 250, 40, 80), 1)
        pygame.draw.rect(self.screen, Colors.red, (200, 150, 100, 50), 1)
    
        pixObj = pygame.PixelArray(self.screen)
        pixObj[480][380] = Colors.black
        pixObj[482][382] = Colors.black
        pixObj[484][384] = Colors.black
        pixObj[486][386] = Colors.black
        pixObj[488][388] = Colors.black
        del pixObj

if __name__ == '__main__':
    g = Game(640, 480)
    g.loop()
