import sys, pygame
import math
import time

class Help(object):

    def __init__(self,mC):
        pygame.init()

        self.masterClass = mC

        self.displaySize = (900,600)
        self.screen = pygame.Surface(self.displaySize)
        self.panelName = 'Help'

        self.BLACK = (0,0,0)
        self.GRAY = (128,128,128)
        self.WHITE = (255,255,255)
        self.fontMaster = None

        self.previousScreen = ''

    def __str__(self):
        return self.panelName

    def draw(self):
        self.screen.fill(self.WHITE)

        #Draw a back button
        pygame.draw.rect(self.screen,self.BLACK,[0,0,50,50],2)
        pygame.draw.polygon(self.screen,self.BLACK,[(40,10),(10,25),(40,40)],0)

        self.fontMaster = pygame.font.SysFont('Calibri',36)
        self.text = self.fontMaster.render('Welcome to the Help Screen!',True,self.BLACK)
        self.screen.blit(self.text,(260,10))

        self.fontMaster = pygame.font.SysFont('Calibri',18)

        self.text = self.fontMaster.render('The goal of the game is to buy everything on the shopping list while staying within the budget.',True,self.BLACK)
        self.screen.blit(self.text,(20,80))
        self.text = self.fontMaster.render('Start the game by clicking to enter the store, then input a choice of department, a budget, and a shopping list.',True,self.BLACK)
        self.screen.blit(self.text,(20,120))
        self.text = self.fontMaster.render('Use the keyboard to input the budget. Use the       and       buttons to adjust the quantities of items on the shopping list.',True,self.BLACK)
        self.screen.blit(self.text,(20,160))
        self.text = self.fontMaster.render('From the Overall Store Map click on a       stoppoint to go to that store section.',True,self.BLACK)
        self.screen.blit(self.text,(20,200))
        self.text = self.fontMaster.render('Or click         to checkout and see if you won, or       to return to the main menu.',True,self.BLACK)
        self.screen.blit(self.text,(20,240))
        self.text = self.fontMaster.render('On any other screen click       to return to the previous screen. Click       to reach this screen.',True,self.BLACK)
        self.screen.blit(self.text,(20,280))
        self.text = self.fontMaster.render('While in a store section click on an item to add it to your cart.',True,self.BLACK)
        self.screen.blit(self.text,(20,320))
        self.text = self.fontMaster.render('Check your current status in the dashboard located on the left.',True,self.BLACK)
        self.screen.blit(self.text,(20,360))
        self.text = self.fontMaster.render('You can also remove or adjust quantities of items in the dashboard using the       and       buttons.',True,self.BLACK)
        self.screen.blit(self.text,(20,400))
        self.text = self.fontMaster.render('If you can\'t see an item you bought, try scrolling up or down with the       and       buttons.',True,self.BLACK)
        self.screen.blit(self.text,(20,440))
        self.text = self.fontMaster.render('If you exceeded your allotted budget, you will be asked to remove items from your shopping list during checkout.',True,self.BLACK)
        self.screen.blit(self.text,(20,480))
        self.text = self.fontMaster.render('You can buy things not on your shopping list with any extra money. Try to prioritize though!',True,self.BLACK)
        self.screen.blit(self.text,(20,520))
        self.text = self.fontMaster.render('Good luck and try to stay on budget!',True,self.BLACK)
        self.screen.blit(self.text,(20,560))

        pygame.draw.polygon(self.screen,self.BLACK,[(295,200),(303,216),(311,200)],0)

        pygame.draw.rect(self.screen,self.BLACK,[354,158,21,21],1)
        pygame.draw.rect(self.screen,self.BLACK,[408,158,21,21],1)
        pygame.draw.rect(self.screen,self.BLACK,[358,238,21,21],1)
        pygame.draw.rect(self.screen,self.BLACK,[204,278,21,21],1)
        pygame.draw.rect(self.screen,self.BLACK,[502,278,21,21],1)
        pygame.draw.rect(self.screen,self.BLACK,[564,398,21,21],1)
        pygame.draw.rect(self.screen,self.BLACK,[618,398,21,21],1)
        pygame.draw.rect(self.screen,self.BLACK,[513,438,21,21],1)
        pygame.draw.rect(self.screen,self.BLACK,[567,438,21,21],1)

        
        pygame.draw.rect(self.screen,self.BLACK,[75,238,33,21],1)
        self.fontMaster = pygame.font.SysFont('Calibri',8)
        self.text = self.fontMaster.render('Checkout',False,self.BLACK)
        self.screen.blit(self.text,(76,245))

        pygame.draw.line(self.screen,self.BLACK,(362,242),(375,255))
        pygame.draw.line(self.screen,self.BLACK,(362,255),(375,242))
        pygame.draw.polygon(self.screen,self.BLACK,[(221,282),(208,288),(221,295)],0)

        self.fontMaster = pygame.font.SysFont('Calibri',20)
        self.text = self.fontMaster.render('?',False,self.BLACK)
        self.screen.blit(self.text,(507,280))
        self.fontMaster = pygame.font.SysFont('Calibri',26)
        self.text = self.fontMaster.render('+',False,self.BLACK)
        self.screen.blit(self.text,(358,157))
        self.screen.blit(self.text,(568,397))
        self.fontMaster = pygame.font.SysFont('Calibri',32)
        self.text = self.fontMaster.render('-',False,self.BLACK)
        self.screen.blit(self.text,(413,153))
        self.screen.blit(self.text,(414,153)) #double blit for centering purposes
        self.screen.blit(self.text,(623,393))
        self.screen.blit(self.text,(624,393)) #double blit for centering purposes

        pygame.draw.polygon(self.screen,self.BLACK,[(516,452),(523,444),(531,452)])
        pygame.draw.polygon(self.screen,self.BLACK,[(570,444),(577,452),(585,444)])

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos()
            if 0 < self.curPos[0] and self.curPos[0] < 50 \
                            and 0 < self.curPos[1] and self.curPos[1] < 50:
                return self.previousScreen

    def setPreviousScreen(self,ps):
        self.previousScreen = ps