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

        self.initialBudget = 0.0

    def __str__(self):
        return self.panelName        

    def draw(self):
        self.screen.fill(self.WHITE)

        pygame.draw.rect(self.screen,self.BLACK,[100,100,700,400],5) 

        #Draw a back button
        pygame.draw.rect(self.screen,self.BLACK,[0,0,50,50],2)
        pygame.draw.polygon(self.screen,self.BLACK,[(40,10),(10,25),(40,40)],0)

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos()
            if 0 < self.curPos[0] and self.curPos[0] < 50 \
                        and 0 < self.curPos[1] and self.curPos[1] < 50:
                return 'StoreFront'
        

    