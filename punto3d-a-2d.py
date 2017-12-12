
# Import a library of functions called 'pygame'
import pygame
from math import sin
from math import cos
from math import pi
from math import sqrt
from math import atan
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [600, 600]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")


#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
a=[0,0]
j=0
def Transformation(xyz):
    a=[0,0]
    if xyz[0]>0:
        m=(xyz[1]-600)/xyz[0]
        q=int((xyz[2]*xyz[0])/600)
        b=xyz[0]-q
        a[0]=300+b
        a[1]=600-int(m*b+600)
    if xyz[0]<0:
        m=(xyz[1]-600)/xyz[0]
        q=int((xyz[2]*xyz[0])/600)
        b=xyz[0]-q
        a[0]=300+b
        a[1]=600-int(m*b+600)

    if xyz[0]==0:
        a[0]=300
        q=int(xyz[2]*(600-xyz[1])/600)
        a[1]=600-xyz[1]-q
    return a

while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(80)
    p=[250,100,0+j]
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # Clear the screen and set the screen background

    
    if j<=600:    
        screen.fill(WHITE)
    
        p1=Transformation(p)
        pygame.draw.circle(screen, RED, [p1[0], p1[1]], 8)
        pygame.draw.line(screen,BLACK,[300,0],[300,600],3)    
    j=j+1
    pygame.display.flip()
# Be IDLE friendly
pygame.quit()
