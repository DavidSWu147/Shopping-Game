import sys, pygame
from MainMenu import MainMenu
from StoreFront import StoreFront
from InputDepartment import InputDepartment
from InputBudget import InputBudget
from InputShoppingList import InputShoppingList
from OverallStoreMap import OverallStoreMap
from WinCards import WinCards
from Help import Help

'''
@author Evan Degroote
@author Kate Wilson
@author Annie (Chu) Li
@author David Wu
'''
class MasterClass(object):
    
    def __init__(self):
        pygame.init()        

        self.foodItems = ['Bread','Lemonade','Milk','Cereal','Orange Juice','Apples','Cake','Lettuce','Eggs']
        self.homeItems = ['Wood','Windows','Wallpaper','Paint','Chair','Photo Frame','Lamp','Candle','Painting']
        self.entertainmentItems = ['Rocking Horse','Chutes&Ladders','Playing Cards','Soccer Ball','1st Fairy Tales','Skateboard','Frisbee','Ping Pong Set','Doll']

        self.foodPrices = {'Bread':2,'Lemonade':3,'Milk':2,'Cereal':3,  \
                'Orange Juice':2,'Apples':1,'Cake':7,'Lettuce':1,'Eggs':2}
        self.homePrices = {'Wood':16,'Windows':40,'Wallpaper':12,'Paint':5, \
                'Chair':18,'Photo Frame':6,'Lamp':20,'Candle':3,'Painting':8}
        self.entertainmentPrices = {'Rocking Horse':14,'Chutes&Ladders':8,'Playing Cards':1,'Soccer Ball':5, \
                '1st Fairy Tales':10,'Skateboard':9,'Frisbee':3,'Ping Pong Set':4,'Doll':4}
        self.displaySize = (900,600)    
        self.masterScreen = pygame.display.set_mode(self.displaySize)
        self.panelName = 'Dollar Chopper'
        pygame.display.set_caption(self.panelName)   

        self.initializeClasses()

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

    def initializeClasses(self):
        
        self.mainMenu = MainMenu(self)
        self.storeFront = StoreFront(self)
        self.inputDepartment = InputDepartment(self)
        self.inputBudget = InputBudget(self)       
        self.inputShoppingList = InputShoppingList(self)
        self.overallStoreMap = OverallStoreMap(self)
        self.winCards = WinCards(self)
        self.help = Help(self)
        
    def __str__(self):
        return 'Master Class'

    def run(self):
        self.currentClass = self.mainMenu
        self.currentScreen = self.mainMenu.screen
        
        self.hasExited = False
        while not self.hasExited:
            self.draw()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.hasExited = True
                elif self.currentClass != None:
                    command = self.currentClass.handleEvent(event)
                    if command == 'Help':
                        self.currentClass = self.help
                        self.currentScreen = self.help.screen
                    elif command == 'WinCards':
                        self.currentClass = self.winCards
                        self.currentScreen = self.winCards.screen
                    elif command == 'OverallStoreMap':
                        self.currentClass = self.overallStoreMap
                        self.currentScreen = self.overallStoreMap.screen
                    elif command == 'InputDepartment':
                        self.currentClass = self.inputDepartment
                        self.currentScreen = self.inputDepartment.screen
                    elif command == 'InputShoppingList':
                        self.currentClass = self.inputShoppingList
                        self.currentScreen = self.inputShoppingList.screen
                    elif command == 'InputBudget':
                        self.currentClass = self.inputBudget
                        self.currentScreen = self.inputBudget.screen
                    elif command == 'StoreFront':
                        self.currentClass = self.storeFront
                        self.currentScreen = self.storeFront.screen
                    elif command == 'MainMenu':
                        self.resetAll()
                        self.currentClass = self.mainMenu
                        self.currentScreen = self.mainMenu.screen

            

    def draw(self):
        self.masterScreen.fill(self.GRAY)

        if self.currentScreen == None:
            self.masterScreen.fill(self.GRAY)
        else:
            self.currentClass.draw()
            self.masterScreen.blit(self.currentScreen,(0,0))

        pygame.display.update()

    def getBudget(self):
        return self.inputBudget.initialBudget

    def resetAll(self):
        self.inputDepartment.departmentChoice = ''
        self.inputBudget.initialBudget = 0
        self.inputShoppingList.shoppingList = {}
        self.inputShoppingList.currentCategory = ''
        self.overallStoreMap.budgetObj.setBudget("Budget: ", 0, "freesansbold.ttf", 14)
        self.overallStoreMap.remainingObj.setRemaining("Remaining: ", 0, "freesansbold.ttf", 14)
        self.overallStoreMap.shoppingListObj.shoppingList = {}
        self.overallStoreMap.cartObj.cartList = []
        self.overallStoreMap.cartObj.quantitiesBought = {}
        self.overallStoreMap.cartObj.scrollPosition = 0

obj = MasterClass()
obj.run()