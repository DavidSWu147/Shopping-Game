import pygame
import math
from pygame import *
from pygame.locals import*

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
blue = ((0, 0, 255))
green = (0, 255, 0)
red = (255, 0, 0)
pink= (255,200, 200)

class product:

    def __init__(self, screen, name, image, price, Color, X, Y):
        pygame.init()

        self.image = pygame.image.load(image)
        self.Color= Color
        self.X= X
        self.Y= Y
        self.price= price
        self.screen = screen
        self.name = name

        self.font = pygame.font.SysFont("monospace", 20, True)
        self.renderabletext= self.font.render(self.price, 1, self.Color)
        
        self.rect = pygame.Rect(X,Y,200,200)

        #screen.blit(self.renderabletext, (self.X + 50, self.Y + 180))
        # self.box= pygame.draw.polygon(self, Color, [(X,Y), (X + dX, Y), (X + dX, Y + dY), (X, Y + dY)])
    
    def collision(self, click):
        return self.rect.collidepoint(click)
    
    def draw(self):
        self.screen.blit(self.image, (self.X, self.Y))
        self.screen.blit(self.renderabletext, (self.X + 50, self.Y + 180))

class stoppoint:

    def __init__(self, X, Y, color, name, screen):
        self.X= X
        self.Y= Y
        self.color= color
        self.name = name
        self.body= pygame.draw.polygon(screen, (0,0,0), [(self.X,self.Y), (self.X + 30, self.Y), (self.X + 15, self.Y + 27)])
    def collision(self, click):
        return self.body.collidepoint(click)

# Test 1
"""
displaySize= (900, 600)
screen = display.set_mode(displaySize)
screen.fill(white)




pygame.display.update()
clock = time.Clock()
running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    
    
    

    
    
    orangejuice = product(screen, "orangejuice.jpg", "$2.00", black, 180, 0)
    bread = product(screen, "bread.jpg", "$2.00", black, 420, 0)
    lemonade = product(screen, "lemonade.jpg", "$3.00", black, 660, 0)
    milk = product(screen, "milk.jpg", "$2.00", black, 180, 200)
    cereal = product(screen, "cereal.jpg", "$3.00", black, 420, 200)
    apples = product(screen, "apple.jpg", "$1.00", black, 660, 200)
    cake = product(screen, "cake.jpg", "$7.00", black, 180, 400)
    lettuce = product(screen, "lettuce.jpg", "$1.00", black, 420, 400)
    eggs = product(screen, "egg.jpg", "$2.00", black, 660, 400)
    
    rockinghorse = product(screen, "rockinghorse.jpg", "$14.00", black, 180, 0)
    chutesandladders = product(screen, "chutesandladders.jpg", "$6.00", black, 420, 0)
    playingcards = product(screen, "playingcards.jpg", "$1.00", black, 660, 0)
    soccerball = product(screen, "soccerball.jpg", "$5.00", black, 180, 200)
    myfirstfairytales = product(screen, "myfirstfairytales.jpg", "$10.00", black, 420, 200)
    skateboard = product(screen, "skateboard.jpg", "$9.00", black, 660, 200)
    frisbee = product(screen, "frisbee.jpg", "$3.00", black, 180, 400)
    pingpongset = product(screen, "pingpongset.jpg", "$4.00", black, 420, 400)
    dolls = product(screen, "doll.jpg", "$4.00", black, 660, 400)

    wood = product(screen, "plywood.jpg", "$16.00", black, 180, 0)
    windows = product(screen, "window.jpg", "$40.00", black, 420, 0)
    wallpaper = product(screen, "wallpaper.jpg", "$12.00", black, 660, 0)
    paint = product(screen, "paint.jpg", "$5.00", black, 180, 200)
    chair = product(screen, "chair.jpg", "$28.00", black, 420, 200)
    photoframe = product(screen, "photoframe.jpg", "$20.00", black, 660, 200)
    lamp = product(screen, "lamp.jpg", "$32.00", black, 180, 400)
    candle = product(screen, "candle.jpg", "$3.00", black, 420, 400)
    painting = product(screen, "painting.jpg", "$8.00", black, 660, 400)



    pygame.display.update()
"""