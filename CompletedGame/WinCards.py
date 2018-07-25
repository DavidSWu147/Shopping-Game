# @author Kate Wilson

import pygame, math, sys
from pygame import *
from math import *
from pygame.locals import*

class WinCards:

    def __init__(self,mC):
        pygame.init()

        self.masterClass = mC

        self.panelName = 'WinCards'

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = ((0, 0, 255))
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.gray= (128,128, 128)

        self.displaySize = (900, 600)   #will have problems since used to be 650 height
        self.screen = pygame.Surface(self.displaySize)

        self.foodItems = self.masterClass.foodItems
        self.homeItems = self.masterClass.homeItems
        self.entertainmentItems = self.masterClass.entertainmentItems
        self.allItems = {'Food':self.foodItems,'Home':self.homeItems,'Entertainment':self.entertainmentItems}

        self.flag = False

        self.Positions = []

        pos1 = (700, 0)
        self.Positions.append(pos1)
        pos2 = (100, 200)
        self.Positions.append(pos2)
        pos3 = (300, 200)
        self.Positions.append(pos3)
        pos4 = (500, 200)
        self.Positions.append(pos4)
        pos5 = (700, 200)
        self.Positions.append(pos5)
        pos6 = (100, 400)
        self.Positions.append(pos6)
        pos7 = (300, 400)
        self.Positions.append(pos7)
        pos8 = (500, 400)
        self.Positions.append(pos8)
        pos9 = (700, 400)
        self.Positions.append(pos9)

    
    def draw(self):
        self.screen.fill(self.white)

   
        if self.flag or self.wentOverBudget() or self.unboughtItems():
            self.flag = True
            if self.wentOverBudget():
                WinFont = pygame.font.SysFont("monospace", 20, True)
                Debt1_Name= WinFont.render("You went over budget! Please select which items", 1, self.black)
                self.screen.blit(Debt1_Name, (30, 60))
                Debt2_Name= WinFont.render("you would like to change on your shopping list.", 1, self.black)
                self.screen.blit(Debt2_Name, (30, 85))
            elif self.unboughtItems() or self.flag:
                WinFont = pygame.font.SysFont("monospace", 20, True)
                name1 = WinFont.render("You still have items to buy! Please select which items", 1, self.black)
                self.screen.blit(name1, (30, 60))
                name2 = WinFont.render("you would like to change on your shopping list.", 1, self.black)
                self.screen.blit(name2, (30, 85))

            deptChoice = self.masterClass.inputDepartment.departmentChoice

            for dx in range(0,600,200):
                for dy in range(0,210,70):
                    pygame.draw.rect(self.screen,self.black,[150+dx,200+dy,200,70],1)
                    pygame.draw.rect(self.screen,self.black,[150+dx,200+dy,35,35],1)
                    pygame.draw.rect(self.screen,self.black,[150+dx+165,200+dy,35,35],1)
                    pygame.draw.rect(self.screen,self.black,[150+dx+165,200+dy+35,35,35],1)
                    self.fontMaster = pygame.font.SysFont('Calibri',48)
                    self.text = self.fontMaster.render('+',False,self.gray)
                    self.screen.blit(self.text,(321+dx,196+dy))
                    self.fontMaster = pygame.font.SysFont('Calibri',64)
                    self.text = self.fontMaster.render('-',False,self.gray)
                    self.screen.blit(self.text,(323+dx,221+dy))
            
            #Fill with possible choices and quantity desired
            self.fontMaster = pygame.font.SysFont('Calibri',24)
            self.currentItems = self.allItems[deptChoice]
            dx = 0
            dy = 0
            for item in self.currentItems:
                self.text = self.fontMaster.render(self.formatName(item),True,self.black)
                self.screen.blit(self.text,(155+dx,245+dy))
                if item in self.masterClass.inputShoppingList.shoppingList:
                    self.text = self.fontMaster.render(str(self.masterClass.inputShoppingList.shoppingList[item]),True,self.black)
                    self.screen.blit(self.text,(161+dx,207+dy))
                #double iteration
                dy += 70
                if dy >= 210:
                    dy = 0
                    dx += 200

            #Draw a help button
            pygame.draw.rect(self.screen,self.black,[50,0,50,50],2)
            self.fontMaster = pygame.font.SysFont('Calibri',48,True,False)
            self.text = self.fontMaster.render('?',True,self.black)
            self.screen.blit(self.text,(64,6))
        else:   
            WinFont = pygame.font.SysFont("monospace", 24, True)
            name= WinFont.render("You won! Great job staying focused and on budget!", 1, self.green)
            self.screen.blit(name, (100, 60))
        
        #Draw an OK button
        fontObj = pygame.font.SysFont('Calibri',48,True)
        name = fontObj.render('OK',True,self.black)
        self.screen.blit(name,(400,500))
        pygame.draw.rect(self.screen,self.black,(350,490,165,60),1)

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos() 
            if 50 < self.curPos[0] and self.curPos[0] < 100 \
                        and 0 < self.curPos[1] and self.curPos[1] < 50:
                if self.flag or self.wentOverBudget() or self.unboughtItems():
                    self.masterClass.help.setPreviousScreen(self.panelName)
                    return 'Help'
            elif 350 < self.curPos[0] and self.curPos[0] < 515 \
            and 490 < self.curPos[1] and self.curPos[1] < 550:
                if self.flag or self.wentOverBudget() or self.unboughtItems():
                    self.flag = False
                    return 'OverallStoreMap'
                else:
                    return 'MainMenu'
            elif self.flag or self.wentOverBudget() or self.unboughtItems():
                for x in range(150,750,200):
                    for y in range(200,410,70):
                        if x+165 < self.curPos[0] and self.curPos[0] < x+200:
                            if y < self.curPos[1] and self.curPos[1] < y+35:
                                self.masterClass.inputShoppingList.incrementItem(x,y+40)
                            elif y+35 < self.curPos[1] and self.curPos[1] < y+70:
                                self.masterClass.inputShoppingList.decrementItem(x,y+40)

    def getBudget(self):
        return self.masterClass.inputBudget.initialBudget

    def formatName(self,item):
        diff = 15 - len(item)
        newItem = ''
        newItem += ' ' * (diff//2)
        newItem += item
        newItem += ' ' * round(diff/2)
        return newItem
       
    def wentOverBudget(self):
        return self.masterClass.overallStoreMap.remainingObj.remaining < 0

    def unboughtItems(self):        
        map = self.masterClass.overallStoreMap
        for itemName in map.shoppingListObj.shoppingList:           
            if map.shoppingListObj.findItem(map.cartObj.cartList,itemName) != None:
                item = map.shoppingListObj.findItem(map.cartObj.cartList,itemName)
                if map.shoppingListObj.shoppingList[itemName] > map.cartObj.quantitiesBought[item]:
                    return True
            else:
                return True
        return False

    
        
        
        


