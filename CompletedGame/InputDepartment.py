import sys, pygame

class InputDepartment(object):  

    def __init__(self, mC):
        pygame.init()

        self.masterClass = mC

        self.displaySize = (900,600)
        self.screen = pygame.Surface(self.displaySize)
        self.panelName = 'InputDepartment'

        self.BLACK = (0,0,0)
        self.GRAY = (128,128,128)
        self.WHITE = (255,255,255)
        self.fontMaster = None

        self.departmentChoice = ''

    def __str__(self):
        return self.panelName     

    def draw(self):
        self.screen.fill(self.WHITE)

        pygame.draw.rect(self.screen,self.BLACK,[100,100,700,400],5)
        pygame.draw.rect(self.screen,self.BLACK,[300,300,100,100],2)
        pygame.draw.rect(self.screen,self.BLACK,[400,300,100,100],2)
        pygame.draw.rect(self.screen,self.BLACK,[500,300,100,100],2)

        self.fontMaster = pygame.font.SysFont('Calibri',48)
        self.text = self.fontMaster.render('Choose a part of the Store',True,self.BLACK)
        self.screen.blit(self.text,(185,180))

        self.fontMaster = pygame.font.SysFont('Calibri',36)
        self.text = self.fontMaster.render('Food',True,self.BLACK)
        self.screen.blit(self.text,(315,336))

        self.text = self.fontMaster.render('Home',True,self.BLACK)
        self.screen.blit(self.text,(410,320))
        self.text = self.fontMaster.render('Decor',True,self.BLACK)
        self.screen.blit(self.text,(408,360))

        self.fontMaster = pygame.font.SysFont('Calibri',24)
        self.text = self.fontMaster.render('Enter-',True,self.BLACK)
        self.screen.blit(self.text,(520,330))
        self.text = self.fontMaster.render('tainment',True,self.BLACK)
        self.screen.blit(self.text,(507,360))

        #Draw a back button
        pygame.draw.rect(self.screen,self.BLACK,[0,0,50,50],2)
        pygame.draw.polygon(self.screen,self.BLACK,[(40,10),(10,25),(40,40)],0) 
        #Draw a help button
        pygame.draw.rect(self.screen,self.BLACK,[50,0,50,50],2)
        self.fontMaster = pygame.font.SysFont('Calibri',48,True,False)
        self.text = self.fontMaster.render('?',True,self.BLACK)
        self.screen.blit(self.text,(64,6))

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos()     
            if 0 < self.curPos[0] and self.curPos[0] < 50 \
                        and 0 < self.curPos[1] and self.curPos[1] < 50:
                return 'StoreFront' 
            elif 50 < self.curPos[0] and self.curPos[0] < 100 \
                        and 0 < self.curPos[1] and self.curPos[1] < 50:
                self.masterClass.help.setPreviousScreen(self.panelName)
                return 'Help'
            elif 300 < self.curPos[0] and self.curPos[0] < 400 \
                        and 300 < self.curPos[1] and self.curPos[1] < 400:
                self.departmentChoice = 'Food'
                return 'InputBudget'
            elif 400 < self.curPos[0] and self.curPos[0] < 500 \
                        and 300 < self.curPos[1] and self.curPos[1] < 400:
                self.departmentChoice = 'Home'
                return 'InputBudget'
            elif 500 < self.curPos[0] and self.curPos[0] < 600 \
                        and 300 < self.curPos[1] and self.curPos[1] < 400:
                self.departmentChoice = 'Entertainment'
                return 'InputBudget'
