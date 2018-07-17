import sys, pygame

class InputBudget(object):

    def __init__(self, mC):
        pygame.init()

        self.masterClass = mC

        self.displaySize = (900,600)
        self.screen = pygame.Surface(self.displaySize)
        self.panelName = 'InputBudget'

        self.BLACK = (0,0,0)
        self.GRAY = (128,128,128)
        self.WHITE = (255,255,255)
        self.fontMaster = None

        self.initialBudget = 0
        self.recommendedBudgets = {'':(0,0),'Food':(20,30),'Home':(150,200),'Entertainment':(50,60)}

    def __str__(self):
        return self.panelName        

    def draw(self):
        self.screen.fill(self.WHITE)

        pygame.draw.rect(self.screen,self.BLACK,[100,100,700,400],5) 
        pygame.draw.rect(self.screen,self.BLACK,[200,300,500,100],2)

        self.fontMaster = pygame.font.SysFont('Calibri',48)
        self.text = self.fontMaster.render('Set Your Budget',False,self.BLACK)
        self.screen.blit(self.text,(290,210))

        #Draw a back button
        pygame.draw.rect(self.screen,self.BLACK,[0,0,50,50],2)
        pygame.draw.polygon(self.screen,self.BLACK,[(40,10),(10,25),(40,40)],0)

        #Draw the budget in dollars
        self.fontMaster = pygame.font.SysFont('Calibri',64)
        self.text = self.fontMaster.render('$' + str(self.initialBudget) + '.00',False,self.BLACK)
        self.screen.blit(self.text,(220,320))

        #Recommended budget at the bottom
        self.departmentChoice = self.masterClass.inputDepartment.departmentChoice
        self.rec = self.recommendedBudgets[self.departmentChoice]
        self.fontMaster = pygame.font.SysFont('Calibri',32)
        self.text = self.fontMaster.render('Recommended Budget: $' + \
                str(self.rec[0]) + ' ~ $' + str(self.rec[1]),False,self.BLACK)
        self.screen.blit(self.text,(220,440))

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos()
            if 0 < self.curPos[0] and self.curPos[0] < 50 \
                        and 0 < self.curPos[1] and self.curPos[1] < 50:
                self.initialBudget = 0
                return 'InputDepartment'
        elif event.type == pygame.KEYUP:
            self.curKey = event.key

            if self.curKey == pygame.K_RETURN:
                return 'OverallStoreMap'
            elif self.curKey == pygame.K_BACKSPACE:
                self.initialBudget = 0
            elif self.initialBudget < 100:
                if self.curKey == pygame.K_1:    
                    self.initialBudget = self.initialBudget * 10 + 1
                elif self.curKey == pygame.K_2:
                    self.initialBudget = self.initialBudget * 10 + 2
                elif self.curKey == pygame.K_3:
                    self.initialBudget = self.initialBudget * 10 + 3
                elif self.curKey == pygame.K_4:
                    self.initialBudget = self.initialBudget * 10 + 4
                elif self.curKey == pygame.K_5:
                    self.initialBudget = self.initialBudget * 10 + 5
                elif self.curKey == pygame.K_6:
                    self.initialBudget = self.initialBudget * 10 + 6
                elif self.curKey == pygame.K_7:
                    self.initialBudget = self.initialBudget * 10 + 7
                elif self.curKey == pygame.K_8:
                    self.initialBudget = self.initialBudget * 10 + 8
                elif self.curKey == pygame.K_9:
                    self.initialBudget = self.initialBudget * 10 + 9
                elif self.curKey == pygame.K_0:
                    self.initialBudget = self.initialBudget * 10 

        self.draw()

        

    