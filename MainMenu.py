import sys, pygame

class MainMenu(object):  

    def __init__(self, mC):
        pygame.init()

        self.masterClass = mC

        self.displaySize = (900,600)
        self.screen = pygame.Surface(self.displaySize)
        self.panelName = 'Main Menu'

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.fontMaster = None

    def __str__(self):
        return self.panelName
    
    '''
    Don't call this method!
    Will not work because screen has not been set using display.set_mode()
    '''
    def run(self):
        self.draw()
        pygame.display.update()
        
        self.hasExited = False
        while not self.hasExited:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.hasExited = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.curPos = pygame.mouse.get_pos()
                    if 300 < self.curPos[0] and self.curPos[0] < 600 \
                            and 300 < self.curPos[1] and self.curPos[1] < 400:
                        self.hasExited = True

            self.draw() 
            pygame.display.update()           

    def draw(self):
        self.screen.fill(self.WHITE)    

        self.fontMaster = pygame.font.SysFont('Calibri',64,True,False)
        self.text = self.fontMaster.render('Dollar Chopper',False,self.BLACK)
        self.screen.blit(self.text,(250,100))

        pygame.draw.rect(self.screen,self.BLACK,[300,300,300,100],5)
        self.fontMaster = pygame.font.SysFont('Calibri',36)
        self.text = self.fontMaster.render('Click Here to Enter',False,self.BLACK)
        self.screen.blit(self.text,(317,332))

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos()
            if 300 < self.curPos[0] and self.curPos[0] < 600 \
                        and 300 < self.curPos[1] and self.curPos[1] < 400:
                return 'next screen'

           
