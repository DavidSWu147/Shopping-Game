import sys, pygame
from MainMenu import MainMenu
from StoreFront import StoreFront
from InputBudget import InputBudget

'''
@author David Wu
'''
class MasterClass(object):
    
    def __init__(self):
        pygame.init()

        self.initializeClasses()

        self.displaySize = (900,600)
        self.masterScreen = pygame.display.set_mode(self.displaySize)
        self.panelName = 'Dollar Chopper'
        pygame.display.set_caption(self.panelName)

        #class with the current screen
        self.currentClass = None
        #current screen to be blitted on to the masterScreen (not the class)
        self.currentScreen = None 

        self.BLACK = (0,0,0)
        self.GRAY = (128,128,128)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)        

    def initializeClasses(self):
        self.mainMenu = MainMenu(self)
        self.storeFront = StoreFront(self)
        self.inputBudget = InputBudget(self)

    def __str__(self):
        return 'Master Class'

    def run(self):
        self.currentClass = self.mainMenu
        self.currentScreen = self.mainMenu.screen
        self.draw()
        
        self.hasExited = False
        while not self.hasExited:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.hasExited = True
                elif self.currentClass != None:
                    command = self.currentClass.handleEvent(event)
                    if command == 'Query':
                        self.currentClass = None
                        self.currentScreen = None
                    elif command == 'InputBudget':
                        self.currentClass = self.inputBudget
                        self.currentScreen = self.inputBudget.screen
                    elif command == 'StoreFront':
                        self.currentClass = self.storeFront
                        self.currentScreen = self.storeFront.screen
                    elif command == 'MainMenu':
                        self.currentClass = self.mainMenu
                        self.currentScreen = self.mainMenu.screen

            self.draw()

    def draw(self):
        self.masterScreen.fill(self.GRAY)

        if self.currentScreen == None:
            self.masterScreen.fill(self.GRAY)
        else:
            self.currentClass.draw()
            self.masterScreen.blit(self.currentScreen,(0,0))

        pygame.display.update()

obj = MasterClass()
obj.run()