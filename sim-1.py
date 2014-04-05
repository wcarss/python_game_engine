import pygame, sys
from pygame.locals import *

class Colors(object):
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

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
    def setup_class(self, screen, event_queue):
        self.screen = screen
        self.event_queue = event_queue

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

class Region(object):
    @classmethod
    def setup_class(self, screen, event_queue):
        self.screen = screen
        self.event_queue = event_queue

    def __init__(self, x, y, w, h, filled=False):
        self.border = 1
        if filled:
            self.border = 0
        self.rect = pygame.rect.Rect(x, y, w, h)

    def draw(self):
        pygame.draw.rect(
            self.screen,
            Colors.red,
            (
                self.rect.x,
                self.rect.y,
                self.rect.w,
                self.rect.h
            ),
            self.border
        )

class Game(object):
    def __init__(self, window_x, window_y):
        self.window_x = window_x
        self.window_y = window_y
        self.event_queue = []

        pygame.init()
        self.screen = pygame.display.set_mode((window_x, window_y), 0, 32)
        pygame.display.set_caption('Drawing')
        self.setup_game()

    def setup_game(self):
        Point.setup_class(self.window_x, self.window_y)
        Person.setup_class(self.screen, self.event_queue)
        Region.setup_class(self.screen, self.event_queue)
        self.draw_list = [
            Person(60, 60),
            Person(120, 60),
            Region(200, 150, 100, 50),
            Region(10, 10, 30, 30),
        ]

    def loop(self):
        t = 0
        while True:
            t = (t + 1) % 255
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.end_game()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE or
                        event.key == pygame.K_q):
                      self.end_game()
            for event in self.event_queue:
                pass

            self.setup_update(t)
            pygame.display.update()

    def setup_update(self, time):
        self.screen.fill(Colors.white)
        for entity in self.draw_list:
            entity.draw()

    def end_game(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    g = Game(640, 480)
    g.loop()
