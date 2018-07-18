import sys, pygame

class InputShoppingList(object):

    def __init__(self, mC):
        pygame.init()

        self.masterClass = mC

        self.displaySize = (900,600)
        self.screen = pygame.Surface(self.displaySize)
        self.panelName = 'InputShoppingList'

        self.BLACK = (0,0,0)
        self.GRAY = (128,128,128)
        self.WHITE = (255,255,255)
        self.fontMaster = None

        #key = item, value = quantity
        self.foodItems = self.masterClass.foodItems
        self.homeItems = self.masterClass.homeItems
        self.entertainmentItems = self.masterClass.entertainmentItems
        self.allItems = {'Food':self.foodItems,'Home':self.homeItems,'Entertainment':self.entertainmentItems}
        self.shoppingList = {}
        self.currentCategory = ''

    def __str__(self):
        return self.panelName        

    def draw(self):
        self.screen.fill(self.WHITE)

        pygame.draw.rect(self.screen,self.BLACK,[100,100,700,400],5) 

        for dx in range(0,600,200):
            for dy in range(0,210,70):
                pygame.draw.rect(self.screen,self.BLACK,[150+dx,240+dy,200,70],1)
                pygame.draw.rect(self.screen,self.BLACK,[150+dx,240+dy,35,35],1)
                pygame.draw.rect(self.screen,self.BLACK,[150+dx+165,240+dy,35,35],1)
                pygame.draw.rect(self.screen,self.BLACK,[150+dx+165,240+dy+35,35,35],1)
                self.fontMaster = pygame.font.SysFont('Calibri',48)
                self.text = self.fontMaster.render('+',False,self.GRAY)
                self.screen.blit(self.text,(321+dx,236+dy))
                self.fontMaster = pygame.font.SysFont('Calibri',64)
                self.text = self.fontMaster.render('-',False,self.GRAY)
                self.screen.blit(self.text,(323+dx,261+dy))
        
        #Fill with possible choices and quantity desired
        self.fontMaster = pygame.font.SysFont('Calibri',24)
        self.departmentChoice = self.getDepartmentChoice()
        self.currentItems = self.allItems[self.departmentChoice]
        dx = 0
        dy = 0
        for item in self.currentItems:
            self.text = self.fontMaster.render(self.formatName(item),False,self.BLACK)
            self.screen.blit(self.text,(155+dx,285+dy))
            if item in self.shoppingList:
                self.text = self.fontMaster.render(str(self.shoppingList[item]),False,self.BLACK)
                self.screen.blit(self.text,(161+dx,247+dy))
            #double iteration
            dy += 70
            if dy >= 210:
                dy = 0
                dx += 200

        #Draw a back button
        pygame.draw.rect(self.screen,self.BLACK,[0,0,50,50],2)
        pygame.draw.polygon(self.screen,self.BLACK,[(40,10),(10,25),(40,40)],0)

        self.fontMaster = pygame.font.SysFont('Calibri',36)
        self.text = self.fontMaster.render('Select items to add to Shopping List',False,self.BLACK)
        self.screen.blit(self.text,(190,130))

        self.fontMaster = pygame.font.SysFont('Calibri',24)
        self.text = self.fontMaster.render('Press Enter to Continue',False,self.BLACK)
        self.screen.blit(self.text,(334,190))

    def handleEvent(self,event):

        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos()
            if 0 < self.curPos[0] and self.curPos[0] < 50 \
                        and 0 < self.curPos[1] and self.curPos[1] < 50:                
                self.shoppingList = {}
                return 'InputBudget'
            else:
                for x in range(150,750,200):
                    for y in range(240,450,70):
                        if x+165 < self.curPos[0] and self.curPos[0] < x+200:
                            if y < self.curPos[1] and self.curPos[1] < y+35:
                                self.incrementItem(x,y)
                            elif y+35 < self.curPos[1] and self.curPos[1] < y+70:
                                self.decrementItem(x,y)
                self.draw()
        elif event.type == pygame.KEYUP:
            self.curKey = event.key
            if self.curKey == pygame.K_RETURN:
                return 'OverallStoreMap'

    def getDepartmentChoice(self):
        return self.masterClass.inputDepartment.departmentChoice

    def formatName(self,item):
        diff = 15 - len(item)
        newItem = ''
        newItem += ' ' * (diff//2)
        newItem += item
        newItem += ' ' * round(diff/2)
        return newItem

    def incrementItem(self,x,y): #coordinates of top left corner of box holding item        
        self.departmentChoice = self.getDepartmentChoice()
        self.currentItems = self.allItems[self.departmentChoice]
        col = int((x-150) / 200)
        row = int((y-240) / 70)
        itemNo = 3*col + row
        item = self.currentItems[itemNo]
        if item in self.shoppingList:
            if self.shoppingList[item] < 9: #stay single digits
                self.shoppingList[item] += 1
        else:
            self.shoppingList[item] = 1

    def decrementItem(self,x,y): #coordinates of top left corner of box holding item        
        self.departmentChoice = self.getDepartmentChoice()
        self.currentItems = self.allItems[self.departmentChoice]
        col = int((x-150) / 200)
        row = int((y-240) / 70)
        itemNo = 3*col + row
        item = self.currentItems[itemNo]
        if item in self.shoppingList:
            if self.shoppingList[item] == 1:
                self.shoppingList.pop(item)
            else:
                self.shoppingList[item] -= 1