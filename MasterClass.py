import sys, pygame
from MainMenu import MainMenu
from StoreFront import StoreFront
from InputDepartment import InputDepartment
from InputBudget import InputBudget
from OverallStoreMap import OverallStoreMap

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
        self.DARK_GRAY = (64,64,64)
        self.GRAY = (128,128,128)
        self.LIGHT_GRAY = (192,192,192)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255) 
        self.YELLOW = (255,255,0)
        self.CYAN = (0,255,255)
        self.MAGENTA = (255,0,255)      

        self.foodPrices = {'Bread':2,'Lemonade':3,'Milk':2,'Cereal':3,  \
                'Orange Juice':2,'Apples':1,'Cake':7,'Lettuce':1,'Eggs':2}
        self.homePrices = {'Wood':16,'Windows':40,'Wallpaper':12,'Paint':5, \
                'Chair':28,'Photo Frame':20,'Lamp':32,'Candle':3,'Painting':8}
        self.entertainmentPrices = {'Rocking Horse':14,'Chutes and Ladders':6,'Playing Cards':1,'Soccer Ball':5, \
                'My First Fairy Tales':10,'Skateboard':9,'Frisbee':3,'Ping Pong Set':4,'Doll':4}

    def initializeClasses(self):
        self.mainMenu = MainMenu(self)
        self.storeFront = StoreFront(self)
        self.inputDepartment = InputDepartment(self)
        self.inputBudget = InputBudget(self)       
        self.overallStoreMap = OverallStoreMap(self)

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
                    elif command == 'OverallStoreMap':
                        self.currentClass = self.overallStoreMap
                        self.currentScreen = self.overallStoreMap.screen
                    elif command == 'InputDepartment':
                        self.currentClass = self.inputDepartment
                        self.currentScreen = self.inputDepartment.screen
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