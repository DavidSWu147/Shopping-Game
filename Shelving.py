#created by Kate Wilson
#design for individual shelves of each part of the store, will be filled eventually using the class "product" to input items from the store onto the shelves

import pygame, math
from pygame import *
import time
from Product import Product

class Shelving(object):
  def __init__(self,mC):
    pygame.init()

    self.masterClass = mC

    # setting up the window
    self.display_width = 900
    self.display_height = 600

    self.screenSize = (self.display_width, self.display_height)
    self.screen = pygame.Surface(self.screenSize)

    self.white = (255,255,255)
    self.black = (0,0,0)
    black = (0,0,0)
    self.blue = (0,0,255)
        
    self.orangejuice = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\orangejuice.jpg", "$2.00", black, 180, 0)
    self.bread = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\bread.jpg", "$2.00", black, 420, 0)    
    self.lemonade = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lemonade.jpg", "$3.00", black, 660, 0)
    self.milk = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\milk.jpg", "$2.00", black, 180, 200)
    self.cereal = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\cereal.jpg", "$3.00", black, 420, 200)
    self.apples = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\apple.jpg", "$1.00", black, 660, 200)
    self.cake = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\cake.jpg", "$7.00", black, 180, 400)
    self.lettuce = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lettuce.jpg", "$1.00", black, 420, 400)
    self.eggs = Product(self.screen, "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\egg.jpg", "$2.00", black, 660, 400)
    

  def draw(self):
    self.screen.fill(self.white)

    self.drawItems()

    shelving1 = pygame.draw.rect(self.screen, self.black, (0,0,900,200), 5)
    shelving2 = pygame.draw.rect(self.screen, self.black, (0,200,900,200), 5)
    shelving3 = pygame.draw.rect(self.screen, self.black, (0,400,900,200), 5)
    
    #shelving instructions text
    shelving_instructions_text = pygame.font.Font("freesansbold.ttf", 15)
    shelving_instructions_text = shelving_instructions_text.render("Instructions: Click on an item to add it to your cart. Use side arrows to navigate the store.", True, self.black, None)
    shelving_instructions_text_rect = shelving_instructions_text.get_rect()
    shelving_instructions_text_center = (150,575)
    self.screen.blit(shelving_instructions_text, shelving_instructions_text_center)    

  def drawItems(self):
    
    
    self.orangejuice.draw(self.screen)
    self.bread.draw(self.screen)
    self.lemonade.draw(self.screen)
    self.milk.draw(self.screen)
    self.cereal.draw(self.screen)
    self.apples.draw(self.screen)
    self.cake.draw(self.screen)
    self.lettuce.draw(self.screen)
    self.eggs.draw(self.screen)
    
    """
    rockinghorse = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\rockinghorse.jpg", "$14.00", black, 180, 0)
    chutesandladders = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\chutesandladders.jpg", "$6.00", black, 420, 0)
    playingcards = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\playingcards.jpg", "$1.00", black, 660, 0)
    soccerball = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\soccerball.jpg", "$5.00", black, 180, 200)
    myfirstfairytales = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\myfirstfairytales.jpg", "$10.00", black, 420, 200)
    skateboard = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\skateboard.jpg", "$9.00", black, 660, 200)
    frisbee = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\frisbee.jpg", "$3.00", black, 180, 400)
    pingpongset = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\pingpongset.jpg", "$4.00", black, 420, 400)
    dolls = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\doll.jpg", "$4.00", black, 660, 400)

    wood = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\plywood.jpg", "$16.00", black, 180, 0)
    windows = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\window.jpg", "$40.00", black, 420, 0)
    wallpaper = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\wallpaper.jpg", "$12.00", black, 660, 0)
    paint = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\paint.jpg", "$5.00", black, 180, 200)
    chair = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\chair.jpg", "$28.00", black, 420, 200)
    photoframe = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\photoframe.jpg", "$20.00", black, 660, 200)
    lamp = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lamp.jpg", "$32.00", black, 180, 400)
    candle = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\candle.jpg", "$3.00", black, 420, 400)
    painting = Product(self.screen), "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\painting.jpg", "$8.00", black, 660, 400)
    """
  def handleEvent(self,event):
    pass

  


