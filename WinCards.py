# @author Kate Wilson

import pygame, math, sys
from pygame import *
from math import *
from pygame.locals import*

class WinCards:

    def __init__(self,mC):
        pygame.init()

        self.masterClass = mC

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = ((0, 0, 255))
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.pink= (255,200, 200)

        self.displaySize = (900, 600)   #will have problems since used to be 650 height
        self.screen = pygame.Surface(self.displaySize)

        self.Positions = []

        pos1 = (0, 50)
        self.Positions.append(pos1)
        pos2 = (200, 50)
        self.Positions.append(pos2)
        pos3 = (400, 50)
        self.Positions.append(pos3)
        pos4 = (0, 250)
        self.Positions.append(pos4)
        pos5 = (200, 250)
        self.Positions.append(pos5)
        pos6 = (400, 250)
        self.Positions.append(pos6)
        pos7 = (0, 450)
        self.Positions.append(pos7)
        pos8 = (200, 450)
        self.Positions.append(pos8)
        pos9 = (400, 450)
        self.Positions.append(pos9)

    
    def draw(self):
        self.screen.fill(self.white)

        if self.getBudget() >= 0:   #temporary testing

            WinFont = pygame.font.SysFont("monospace", 20, True)
            name= WinFont.render("You've won! Great job staying focused and on budget!", 1, self.green)
            self.screen.blit(name, (60, 275))
    
        if self.getBudget() == 999:
            WinFont = pygame.font.SysFont("monospace", 20, True)
            Debt1_Name= WinFont.render("You went over budget! Please select which items", 1, self.black)
            self.screen.blit(Debt1_Name, (30, 0))
            Debt2_Name= WinFont.render("you would like to remove from your cart.", 1, self.black)
            self.screen.blit(Debt2_Name, (80, 25))

    def handleEvent(self,event):
        pass

    def getBudget(self):
        return self.masterClass.inputBudget.initialBudget
       
        
        
        
        


