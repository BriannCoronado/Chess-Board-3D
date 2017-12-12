# Import a library of functions called 'pygame'
import pygame
from math import pi
from math import cos
from math import pi
from math import sqrt
from math import atan
from math import sin
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

#Transformacion de 3D a 2D
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
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # Clear the screen and set the screen background
    screen.fill(WHITE)



    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
    #base tipo 3D del tablero(cafe obscuro)
    pygame.draw.polygon(screen,(164,110,69), [[48, 500], [552, 500], [552, 550],[48,550]], 0)

    #lineas usando la proyeccion de los puntos esquina superiores con profundidad 400
    esqizq1=[-252,100,300]
    esqder1=[252,100,300]
    esqizqtransfor=Transformation(esqizq1)
    esqdertransfor=Transformation(esqder1)
    
    pygame.draw.line(screen,(164,110,69), [48,500], [esqizqtransfor[0],esqizqtransfor[1]], 6)
    pygame.draw.line(screen,(164,110,69), [esqizqtransfor[0], esqizqtransfor[1]], [esqdertransfor[0],esqdertransfor[1]], 6)
    pygame.draw.line(screen,(164,110,69), [esqdertransfor[0],esqdertransfor[1]], [552,500], 6)
    #cuadros del tablero
    #hacer un cuadrado y transformarlo ( hacer esto para los 8 cuadrados)
    #cuadro=[a1,a2,a3,a4]
    for j in range(8):
        for i in range(8):
            a1=[-252+63*j,100,37*i]
            a2=[-189+63*j,100,37*i]
            a3=[-252+63*j,100,37*(i+1)]
            a4=[-189+63*j,100,37*(i+1)]
            a1=Transformation(a1)
            a2=Transformation(a2)
            a3=Transformation(a3)
            a4=Transformation(a4)
            if j!=3 and j!=4:
                if j%2==0:
            
                    if i%2==1:
                        pygame.draw.polygon(screen,(247,221,190),[a1,a2,a4,a3],0)
                    else:
                        pygame.draw.polygon(screen,(100,70,35),[a1,a2,a4,a3],0)
    
                if j%2==1:
    
                    if i%2==0:
                        pygame.draw.polygon(screen,(247,221,190),[a1,a2,a4,a3],0)
                    else:
                        pygame.draw.polygon(screen,(100,70,35),[a1,a2,a4,a3],0)
    for j in range(2):

        for i in range(8):
            a1=[-63+63*j,100,37*i]
            a2=[0+63*j,100,37*i]
            a3=[-63+63*j,100,37*(i+1)]
            a4=[0+63*j,100,37*(i+1)]
        
            a1=Transformation(a1)
            a2=Transformation(a2)
            a3=Transformation(a3)
            a4=Transformation(a4)
            if j%2==0:

                if i%2==0:
                    pygame.draw.polygon(screen,(247,221,190),[a1,a2,a4,a3],0)
                else:
                    pygame.draw.polygon(screen,(100,70,35),[a1,a2,a4,a3],0)
            else:
                if i%2==1:
                    pygame.draw.polygon(screen,(247,221,190),[a1,a2,a4,a3],0)
                else:
                    pygame.draw.polygon(screen,(100,70,35),[a1,a2,a4,a3],0)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
# Be IDLE friendly
pygame.quit()
