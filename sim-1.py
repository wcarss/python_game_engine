import pygame, sys
from pygame.locals import *

MAXX_SIZE = 600
MAXY_SIZE = 480

class Point(object):
    def __init__(self, x, y):
        x = int(x)
        if x < 0 or x > MAX_SIZE:
            raise ValueError("invalid value for x")
        if y < 0 or y > MAXY_SIZE:
            raise ValueError("invalid value for y")
        self.x = x
        self.y = y

class Person(object):
    def __init__(self, x, y):
        self.location = Point(x, y)

class Colors(object):
    # set up the colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

class Game(object):
    def __init__(self):
        pygame.init()

        # set up the window
        self.screen = pygame.display.set_mode((MAXX_SIZE, MAXY_SIZE), 0, 32)
        pygame.display.set_caption('Drawing')

        # run the game loop
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
        pygame.draw.circle(self.screen, Colors.red, (60, 60), 3, 0)
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
    g = Game()
