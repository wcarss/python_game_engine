import pygame, sys
from pygame.locals import *

# set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pygame.init()

# set up the window
screen = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

def setup_update(alpha):
    screen.fill(white)
    pygame.draw.circle(screen, red, (60, 60), 3, 0)
    #pygame.draw.line(screen, blue, (60, 60), (120, 60), 4)
    #pygame.draw.line(screen, blue, (120, 60), (60, 120))
    #pygame.draw.line(screen, blue, (60, 120), (120, 120), 4)
    #pygame.draw.circle(screen, blue, (300, 50), 20, 0)
    #pygame.draw.ellipse(screen, red, (300, 250, 40, 80), 1)
    pygame.draw.rect(screen, red, (200, 150, 100, 50), 1)
    
    pixObj = pygame.PixelArray(screen)
    pixObj[480][380] = black
    pixObj[482][382] = black
    pixObj[484][384] = black
    pixObj[486][386] = black
    pixObj[488][388] = black
    del pixObj

# run the game loop
t = 0
while True:
    t = (t + 1) % 255
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    setup_update(t)
    pygame.display.update()

