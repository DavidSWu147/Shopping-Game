#created by Kate Wilson
#design for individual shelves of each part of the store, will be filled eventually using the class "product" to input items from the store onto the shelves

import pygame, math
from pygame import *
import time

class Shelving:
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
    self.blue = (0,0,255)

  def draw(self):
    self.screen.fill(self.white)

    shelving1 = pygame.draw.rect(self.screen, self.black, (0,0,900,200), 10)
    shelving2 = pygame.draw.rect(self.screen, self.black, (0,200,900,200), 10)
    shelving3 = pygame.draw.rect(self.screen, self.black, (0,400,900,200), 10)
    
    #shelving instructions text
    shelving_instructions_text = pygame.font.Font("freesansbold.ttf", 15)
    shelving_instructions_text = shelving_instructions_text.render("Instructions: Click on an item to add it to your cart. Use side arrows to navigate the store.", True, self.black, None)
    shelving_instructions_text_rect = shelving_instructions_text.get_rect()
    shelving_instructions_text_center = (150,575)
    self.screen.blit(shelving_instructions_text, shelving_instructions_text_center)

  def handleEvent(self,event):
    pass


