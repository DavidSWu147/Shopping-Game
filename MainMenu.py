import sys, pygame

class MainMenu(object):  

    def __init__(self):
        pygame.init()

        self.displaySize = (900,600)
        self.screen = pygame.display.set_mode(self.displaySize)
        self.panelName = 'Main Menu'
        pygame.display.set_caption(self.panelName)

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.fontMaster = None

    def __str__(self):
        return self.panelName

    def run(self):
        self.draw()
        
        self.hasExited = False
        while not self.hasExited:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.hasExited = True

            self.draw()            

    def draw(self):
        self.screen.fill(self.WHITE)    

        self.fontMaster = pygame.font.SysFont('Calibri',64,True,False)
        self.text = self.fontMaster.render('Dollar Chopper',False,self.BLACK)
        self.screen.blit(self.text,(250,100))

        pygame.draw.rect(self.screen,self.BLACK,[300,300,300,100],5)
        self.fontMaster = pygame.font.SysFont('Calibri',36)
        self.text = self.fontMaster.render('Click Here to Enter',False,self.BLACK)
        self.screen.blit(self.text,(317,332))

        pygame.display.update()
            

obj = MainMenu()
obj.run()

