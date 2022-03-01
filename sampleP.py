#from tkinter.tix import DirSelectDialog
import pygame                           #module
from pygame.locals import *

pygame.init()                          #initialising pygame

#create game window
screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height)) #this will create the game window using .display
pygame.display.set_caption('Platformer') #this puts the caption in the top left window of the display

#load images
sun_img = pygame.image.load('/Users/surya/Desktop/IMP Docs/Final Docs/Decisions/Stevens/Agile Contents/sampleimg/sun.jpeg')
sky_img = pygame.image.load('/Users/surya/Desktop/IMP Docs/Final Docs/Decisions/Stevens/Agile Contents/sampleimg/sky.jpeg')


run = True
while run == True:
    screen.blit(sky_img, (0,0))
    screen.blit(sun_img, (100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
    
    pygame.display.update()

pygame.quit()


