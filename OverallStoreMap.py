#Overall Store Map, created by Kate Wilson
import pygame, math, sys
from pygame import *
import time

class stoppoint:

    def __init__(self, X, Y, color, screen):
        self.X= X
        self.Y= Y
        self.color= color
        self.body= pygame.draw.polygon(screen, (0,0,0), [(self.X,self.Y), (self.X + 30, self.Y), (self.X + 15, self.Y + 27)])

class OverallStoreMap(object):

    def __init__(self, mC):
        pygame.init()

        self.masterClass = mC
        # setting up the window
        self.display_width = 900
        self.display_height = 600

        self.screenSize = (self.display_width, self.display_height)

        self.white = (255,255,255)
        self.black = (0,0,0)
        self.blue = (0,0,255)
        self.bisque = (255,228,196)

        self.screen = pygame.Surface(self.screenSize)

    def draw(self):
        #Overall Store Map, created by Kate Wilson
        self.screen.fill(self.white)

        food_area = pygame.draw.rect(self.screen, self.black, (140,0,760,150),15)
        home_decor_area = pygame.draw.rect(self.screen, self.black, (750,150,150,750), 15)
        entertainment_area = pygame.draw.rect(self.screen, self.black, (140,450,610,150), 15)

        #food area text
        food_area_text = pygame.font.Font("freesansbold.ttf", 20)
        food_area_text = food_area_text.render("Food", True, self.black, None)
        food_area_textrect = food_area_text.get_rect()
        food_area_text_center = (360,75)
        self.screen.blit(food_area_text, food_area_text_center)

        #home decor area text
        home_decor_area_text = pygame.font.Font("freesansbold.ttf", 20)
        home_decor_area_text = home_decor_area_text.render("Home Decor", True, self.black, None)
        home_decor_area_textrect = home_decor_area_text.get_rect()
        home_decor_area_text_center = (765,300)
        self.screen.blit(home_decor_area_text, home_decor_area_text_center)

        #entertainment area text
        entertainment_area_text = pygame.font.Font("freesansbold.ttf", 20)
        entertainment_area_text = entertainment_area_text.render("Entertainment", True, self.black, None)
        entertainment_area_textrect = entertainment_area_text.get_rect()
        entertainment_area_text_center = (360, 500)
        self.screen.blit(entertainment_area_text, entertainment_area_text_center)

        self.foodStoppoint = stoppoint (375, 170, self.black, self.screen)
        self.homedecorStoppoint = stoppoint (700, 300, self.black, self.screen)
        self.entertainmentStoppoint = stoppoint (375, 400, self.black, self.screen)
        #pygame.display.update()

        #Annie's Code
        #The origin of the display, where x = 0 and y = 0, is the top left of the self.screen. Both axes increase positively towards the bottom right of the self.screen.
        fontObj = pygame.font.Font('freesansbold.ttf', 14) 
        textObj1 = fontObj.render('budget:',True,self.black,self.bisque)
        textRectObj1 = textObj1.get_rect()
        textRectObj1.center = (40,20)
        
        #self.screen.fill(self.white) ERROR

        self.screen.blit(textObj1,textRectObj1) # draw budget

        textObj2 = fontObj.render('now:',True,self.black,self.bisque)
        textRectObj2 = textObj2.get_rect()
        textRectObj2.center = (30,80)
        self.screen.blit(textObj2,textRectObj2)

        textObj3 = fontObj.render('shopping list:',True,self.black,self.bisque)
        textRectObj3 = textObj3.get_rect()
        textRectObj3.center = (60,140)
        self.screen.blit(textObj3,textRectObj3)

        textObj4 = fontObj.render('extra:',True,self.black,self.bisque)
        textRectObj4 = textObj4.get_rect()
        textRectObj4.center = (30,370)
        self.screen.blit(textObj4,textRectObj4)

        pygame.draw.line(self.screen,self.black,(140,0),(140,600)) # draw line

    #IN PROGRESS
    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos()
            if  self.foodStoppoint.X < self.curPos[0] and self.curPos[0] < self.foodStoppoint.X + 30 \
            and self.foodStoppoint.Y < self.curPos[1] and self.curPos[1] < self.foodStoppoint.Y + 27:
                #self.screen.fill(white)
                #self.screen.blit(shelving)
                return 'Query'
            if  self.homedecorStoppoint.X < self.curPos[0] and self.curPos[0] < self.homedecorStoppoint.X + 30 \
            and self.homedecorStoppoint.Y < self.curPos[1] and self.curPos[1] < self.homedecorStoppoint.Y + 27:
                #self.screen.fill(white)
                #self.screen.blit(shelving)
                return 'Query'
            if  self.entertainmentStoppoint.X < self.curPos[0] and self.curPos[0] < self.entertainmentStoppoint.X + 30 \
            and self.entertainmentStoppoint.Y < self.curPos[1] and self.curPos[1] < self.entertainmentStoppoint.Y + 27:
                #self.screen.fill(white)
                #self.screen.blit(shelving) 
                return 'Query'



