import sys, pygame

class MainMenu(object):  

    def __init__(self, mC):
        pygame.init()

        self.masterClass = mC

        self.displaySize = (900,600)
        self.screen = pygame.Surface(self.displaySize)
        self.panelName = 'MainMenu'

        self.BLACK = (0,0,0)
        self.GRAY = (128,128,128)
        self.WHITE = (255,255,255)
        self.fontMaster = None

        self.clock = pygame.time.Clock()

    def __str__(self):
        return self.panelName            

    def draw(self):
        self.screen.fill(self.WHITE)  

        bgImage = pygame.image.load("C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\mainbackground.jpg")
        self.screen.blit(bgImage,(-self.xtime(pygame.time.get_ticks()),-self.ytime(pygame.time.get_ticks()))) 

        self.fontMaster = pygame.font.SysFont('Calibri',64,True,False)
        self.text = self.fontMaster.render('Dollar Chopper',True,self.WHITE)
        self.screen.blit(self.text,(250,100))

        pygame.draw.rect(self.screen,self.WHITE,[300,300,300,100])
        pygame.draw.rect(self.screen,self.BLACK,[300,300,300,100],5)
        self.fontMaster = pygame.font.SysFont('Calibri',36)
        self.text = self.fontMaster.render('Click Here to Enter',True,self.BLACK)
        self.screen.blit(self.text,(317,332))

    def handleEvent(self,event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.curPos = pygame.mouse.get_pos()
            if 300 < self.curPos[0] and self.curPos[0] < 600 \
                        and 300 < self.curPos[1] and self.curPos[1] < 400:
                return 'StoreFront'

    def xtime(self,time):
        bicentitime = time // 50
        bicentitime = bicentitime % 1000
        if bicentitime < 380:
            return bicentitime
        elif 380 <= bicentitime and bicentitime < 500:
            return 380
        elif 500 <= bicentitime and bicentitime < 880:
            return 880 - bicentitime
        elif 880 <= bicentitime:
            return 0

    def ytime(self,time):
        bicentitime = time // 50
        bicentitime = bicentitime % 1000
        if bicentitime < 380:
            return 0
        elif 380 <= bicentitime and bicentitime < 500:
            return bicentitime - 380
        elif 500 <= bicentitime and bicentitime < 880:
            return 120
        elif 880 <= bicentitime:
            return 1000 - bicentitime
    

           
