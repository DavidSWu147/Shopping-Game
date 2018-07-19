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

class Product(object):
    
    def __init__(self, screen, image, price, Color, X, Y):       
        self.image = pygame.image.load(image).convert()
        self.Color= Color
        self.X= X
        self.Y= Y
        self.price= price

    def draw(self,screen):
        screen.blit(self.image, (self.X, self.Y))
        myFont = pygame.font.SysFont("monospace", 20, True)
        product_Name= myFont.render(self.price, 1, self.Color)
        screen.blit(product_Name, (self.X + 50, self.Y + 180))
        # self.box= pygame.draw.polygon(self, Color, [(X,Y), (X + dX, Y), (X + dX, Y + dY), (X, Y + dY)])

class stoppoint:

    def __init__(self, X, Y, color, screen):
        self.X= X
        self.Y= Y
        self.color= color
        self.body= pygame.draw.polygon(screen, color, [(self.X,self.Y), (self.X + 30, self.Y), (self.X + 15, self.Y + 27)])
        

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
    
    
    

    

    orangejuice = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\orangejuice.jpg", "$2.00", black, 180, 0)
    bread = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\bread.jpg", "$2.00", black, 420, 0)    
    lemonade = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lemonade.jpg", "$3.00", black, 660, 0)
    milk = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\milk.jpg", "$2.00", black, 180, 200)
    cereal = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\cereal.jpg", "$3.00", black, 420, 200)
    apples = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\apple.jpg", "$1.00", black, 660, 200)
    cake = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\cake.jpg", "$7.00", black, 180, 400)
    lettuce = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lettuce.jpg", "$1.00", black, 420, 400)
    eggs = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\egg.jpg", "$2.00", black, 660, 400)
    
    rockinghorse = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\rockinghorse.jpg", "$14.00", black, 180, 0)
    chutesandladders = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\chutesandladders.jpg", "$6.00", black, 420, 0)
    playingcards = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\playingcards.jpg", "$1.00", black, 660, 0)
    soccerball = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\soccerball.jpg", "$5.00", black, 180, 200)
    myfirstfairytales = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\myfirstfairytales.jpg", "$10.00", black, 420, 200)
    skateboard = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\skateboard.jpg", "$9.00", black, 660, 200)
    frisbee = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\frisbee.jpg", "$3.00", black, 180, 400)
    pingpongset = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\pingpongset.jpg", "$4.00", black, 420, 400)
    dolls = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\doll.jpg", "$4.00", black, 660, 400)

    wood = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\plywood.jpg", "$16.00", black, 180, 0)
    windows = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\window.jpg", "$40.00", black, 420, 0)
    wallpaper = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\wallpaper.jpg", "$12.00", black, 660, 0)
    paint = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\paint.jpg", "$5.00", black, 180, 200)
    chair = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\chair.jpg", "$28.00", black, 420, 200)
    photoframe = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\photoframe.jpg", "$20.00", black, 660, 200)
    lamp = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lamp.jpg", "$32.00", black, 180, 400)
    candle = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\candle.jpg", "$3.00", black, 420, 400)
    painting = Product(screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\painting.jpg", "$8.00", black, 660, 400)
    
    wood.draw(screen)

    pygame.display.update()
"""