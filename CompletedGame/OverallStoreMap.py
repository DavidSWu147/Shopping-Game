import pygame, math, sys
from pygame import *
import time
from Classes import *

pygame.init()
black = (0,0,0)

# screen = pygame.display.set_mode([900,600])

#STORE SECTION CODE
class StoreSection:
    def __init__(self,name,products):
        self.name = name
        self.products = products
    def draw(self):
        for product in self.products:
            product.draw()
    def collision(self):
        for product in self.products:
            return products.collidepoint()
            
class stoppoint:

    def __init__(self, X, Y, color, name, screen):
        self.X= X
        self.Y= Y
        self.color= color
        self.name = name
        self.body= pygame.draw.polygon(screen, (0,0,0), [(self.X,self.Y), (self.X + 30, self.Y), (self.X + 15, self.Y + 27)])
    def collision(self, click):
        return self.body.collidepoint(click)

class Budget:
    
    def __init__(self, x, y, screen, text, budget, texttype, textsize):
        self.x= x
        self.y = y
        self.screen = screen
        self.budget = budget
        self.text = text + '$' + str(budget)
        self.font = pygame.font.Font(texttype, textsize)
        self.renderabletext = self.font.render(self.text, True, (0,0,0))

    def draw(self):
        self.screen.blit(self.renderabletext, (self.x,self.y))

    def setBudget(self,text,budget,texttype,textsize):
        self.budget = budget
        self.text = text + '$' + str(budget)
        self.font = pygame.font.Font(texttype, textsize)
        self.renderabletext = self.font.render(self.text, True, (0,0,0))

class product:

    def __init__(self, screen, name, image, price, Color, X, Y):
        pygame.init()

        self.image = pygame.image.load(image)
        self.Color= Color
        self.X= X
        self.Y= Y
        self.price= price
        self.screen = screen
        self.name = name

        self.font = pygame.font.SysFont("monospace", 20, True)
        self.renderabletext= self.font.render(self.price, 1, self.Color)
        
        self.rect = pygame.Rect(X,Y,200,200)
    
    def collision(self, click):
        return self.rect.collidepoint(click)
    
    def draw(self):
        self.screen.blit(self.image, (self.X, self.Y))
        self.screen.blit(self.renderabletext, (self.X + 50, self.Y + 180))
           

class OverallStoreMap(object):

    def __init__(self, mC):
        pygame.init()

        self.masterClass = mC
        # setting up the window
        self.display_width = 900
        self.display_height = 600

        
        self.panelName = 'OverallStoreMap'
        self.displayStoreSection = False
        self.clickname = ""
        self.clickstoresection = None

        self.screenSize = (self.display_width, self.display_height)

        self.white = (255,255,255)
        self.black = (0,0,0)
        self.blue = (0,0,255)
        self.bisque = (255,228,196)

        self.screen = pygame.Surface(self.screenSize)

        self.StoreSectionlist = []
        self.stoppointlist = []

        foodSectionproducts = []
        homedecorSectionproducts = []
        entertainmentSectionproducts = []

        orangejuice = product(self.screen, "Orange Juice", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\orangejuice.jpg", "$2.00", black, 180, 0)        
        bread = product(self.screen, "Bread", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\bread.jpg", "$2.00", black, 420, 0)
        lemonade = product(self.screen, "Lemonade", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lemonade.jpg", "$3.00", black, 660, 0)
        milk = product(self.screen, "Milk", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\milk.jpg", "$2.00", black, 180, 200)
        cereal = product(self.screen, "Cereal", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\cereal.jpg", "$3.00", black, 420, 200)
        apples = product(self.screen, "Apples", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\apple.jpg", "$1.00", black, 660, 200)
        cake = product(self.screen, "Cake", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\cake.jpg", "$7.00", black, 180, 400)
        lettuce = product(self.screen, "Lettuce", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lettuce.jpg", "$1.00", black, 420, 400)
        eggs = product(self.screen, "Eggs", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\egg.jpg", "$2.00", black, 660, 400)
        
        foodSectionproducts.append(orangejuice)       
        foodSectionproducts.append(bread)
        foodSectionproducts.append(lemonade)
        foodSectionproducts.append(milk)
        foodSectionproducts.append(cereal)
        foodSectionproducts.append(apples)
        foodSectionproducts.append(cake)
        foodSectionproducts.append(lettuce)
        foodSectionproducts.append(eggs)
    
        rockinghorse = product(self.screen, "Rocking Horse", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\rockinghorse.jpg", "$14.00", black, 180, 0)
        chutesandladders = product(self.screen, "Chutes&Ladders", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\chutesandladders.jpg", "$8.00", black, 420, 0)
        playingcards = product(self.screen, "Playing Cards", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\playingcards.jpg", "$1.00", black, 660, 0)
        soccerball = product(self.screen, "Soccer Ball", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\soccerball.jpg", "$5.00", black, 180, 200)
        myfirstfairytales = product(self.screen, "1st Fairy Tales", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\myfirstfairytales.jpg", "$10.00", black, 420, 200)
        skateboard = product(self.screen, "Skateboard", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\skateboard.jpg", "$9.00", black, 660, 200)
        frisbee = product(self.screen, "Frisbee", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\frisbee.jpg", "$3.00", black, 180, 400)
        pingpongset = product(self.screen, "Ping Pong Set", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\pingpongset.jpg", "$4.00", black, 420, 400)
        dolls = product(self.screen, "Doll", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\doll.jpg", "$4.00", black, 660, 400)

        entertainmentSectionproducts.append(rockinghorse)
        entertainmentSectionproducts.append(chutesandladders)
        entertainmentSectionproducts.append(playingcards)
        entertainmentSectionproducts.append(soccerball)
        entertainmentSectionproducts.append(myfirstfairytales)
        entertainmentSectionproducts.append(skateboard)
        entertainmentSectionproducts.append(frisbee)
        entertainmentSectionproducts.append(pingpongset)
        entertainmentSectionproducts.append(dolls)

        wood = product(self.screen, "Wood", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\plywood.jpg", "$16.00", black, 180, 0)
        windows = product(self.screen, "Windows", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\window.jpg", "$40.00", black, 420, 0)
        wallpaper = product(self.screen, "Wallpaper", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\wallpaper.jpg", "$12.00", black, 660, 0)
        paint = product(self.screen, "Paint", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\paint.jpg", "$5.00", black, 180, 200)
        chair = product(self.screen, "Chair", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\chair.jpg", "$18.00", black, 420, 200)
        photoframe = product(self.screen, "Photo Frame", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\photoframe.jpg", "$6.00", black, 660, 200)
        lamp = product(self.screen, "Lamp", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\lamp.jpg", "$20.00", black, 180, 400)
        candle = product(self.screen, "Candle", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\candle.jpg", "$3.00", black, 420, 400)
        painting = product(self.screen, "Painting", "C:\\Users\\Bdavi\\Python Workspace\\.vscode\\Project\\Images\\painting.jpg", "$8.00", black, 660, 400)

        homedecorSectionproducts.append(wood)
        homedecorSectionproducts.append(windows)
        homedecorSectionproducts.append(wallpaper)
        homedecorSectionproducts.append(paint)
        homedecorSectionproducts.append(chair)
        homedecorSectionproducts.append(photoframe)
        homedecorSectionproducts.append(lamp)
        homedecorSectionproducts.append(candle)
        homedecorSectionproducts.append(painting)

        # create store sections using class definitions
        foodSection = StoreSection("food", foodSectionproducts)
        homedecorSection = StoreSection("homedecor", homedecorSectionproducts)
        entertainmentSection = StoreSection("entertainment", entertainmentSectionproducts)      

        #stoppoints
        foodStoppoint = stoppoint (375, 170, self.black, "food", self.screen)
        homedecorStoppoint = stoppoint (700, 300, self.black, "homedecor", self.screen)
        entertainmentStoppoint = stoppoint (375, 400, self.black, "entertainment", self.screen)

        self.StoreSectionlist.append(foodSection)
        self.StoreSectionlist.append(homedecorSection)
        self.StoreSectionlist.append(entertainmentSection)

        self.stoppointlist.append(foodStoppoint)
        self.stoppointlist.append(homedecorStoppoint)
        self.stoppointlist.append(entertainmentStoppoint)

        budget = self.masterClass.getBudget()
        self.budgetObj = Budget(10,60, self.screen, "Budget: ", budget, "freesansbold.ttf", 14)
        remaining = budget
        self.remainingObj = Remaining(10,80, self.screen, "Remaining: ", remaining, "freesansbold.ttf", 14)
        self.shoppingListObj = ShoppingList()
        self.cartObj = Cart()

    def draw(self):
        #Overall Store Map, created by Kate Wilson
        self.screen.fill(self.white)

        if not self.displayStoreSection:

            food_area = pygame.draw.rect(self.screen, self.black, (140,0,760,150),15)
            home_decor_area = pygame.draw.rect(self.screen, self.black, (750,150,150,750), 15)
            entertainment_area = pygame.draw.rect(self.screen, self.black, (140,450,610,150), 15)

            #food area text
            food_area_text = pygame.font.Font("freesansbold.ttf", 20)
            food_area_text = food_area_text.render("Food", True, self.black, None)
            food_area_textrect = food_area_text.get_rect()
            food_area_text_center = (360,75)
            self.screen.blit(food_area_text, food_area_text_center)

            #home decor area text
            home_decor_area_text = pygame.font.Font("freesansbold.ttf", 20)
            home_decor_area_text = home_decor_area_text.render("Home Decor", True, self.black, None)
            home_decor_area_textrect = home_decor_area_text.get_rect()
            home_decor_area_text_center = (765,300)
            self.screen.blit(home_decor_area_text, home_decor_area_text_center)

            #entertainment area text
            entertainment_area_text = pygame.font.Font("freesansbold.ttf", 20)
            entertainment_area_text = entertainment_area_text.render("Entertainment", True, self.black, None)
            entertainment_area_textrect = entertainment_area_text.get_rect()
            entertainment_area_text_center = (360, 500)
            self.screen.blit(entertainment_area_text, entertainment_area_text_center)

            self.foodStoppoint = stoppoint (375, 170, self.black, "food", self.screen)
            self.homedecorStoppoint = stoppoint (700, 300, self.black, "homedecor", self.screen)
            self.entertainmentStoppoint = stoppoint (375, 400, self.black, "entertainment", self.screen)

            #Draw an X button
            pygame.draw.rect(self.screen,self.black,[0,0,50,50],2)
            pygame.draw.line(self.screen,self.black,[8,8],[42,42],5)
            pygame.draw.line(self.screen,self.black,[8,42],[42,8],5)

            #Draw a checkout button
            #The item is the first appearance of the checkout button.
            CheckFont = pygame.font.Font('freesansbold.ttf', 30)
            Button_name= CheckFont.render("Checkout", True, (0,0,0))
            CheckButton= Button_name.get_rect()
            CheckButton.center = (180,390)
            self.screen.blit(Button_name, CheckButton.center)
            pygame.draw.rect(self.screen,self.black,(176,378,150,50),5)
        else:
            self.clickstoresection.draw()

            #Draw a back button
            pygame.draw.rect(self.screen,self.black,[0,0,50,50],2)
            pygame.draw.polygon(self.screen,self.black,[(40,10),(10,25),(40,40)],0)

        #Draw a help button
        pygame.draw.rect(self.screen,self.black,[50,0,50,50],2)
        self.fontMaster = pygame.font.SysFont('Calibri',48,True,False)
        self.text = self.fontMaster.render('?',True,self.black)
        self.screen.blit(self.text,(64,6))

        #Annie's Code
        #The origin of the display, where x = 0 and y = 0, is the top left of the self.screen. Both axes increase positively towards the bottom right of the self.screen.
        
        self.budgetObj.draw()  
        
        self.remainingObj.draw()

        fontObj = pygame.font.Font('freesansbold.ttf', 14) 
        textObj3 = fontObj.render('Shopping List:',True,self.black,self.bisque)
        textRectObj3 = textObj3.get_rect()
        textRectObj3.center = (60,110)
        self.screen.blit(textObj3,textRectObj3)

        self.shoppingListObj.draw(self.screen,10,125,self.cartObj.cartList,self.cartObj.quantitiesBought)

        textObj4 = fontObj.render('Cart:',True,self.black,self.bisque)
        textRectObj4 = textObj4.get_rect()
        textRectObj4.center = (30,320)
        self.screen.blit(textObj4,textRectObj4)

        #Draw a scroll bar and boxes
        pygame.draw.rect(self.screen,self.black,(5,340,20,240),1)
        pygame.draw.rect(self.screen,self.black,(5,340,20,20),1)
        pygame.draw.rect(self.screen,self.black,(5,560,20,20),1)
        pygame.draw.polygon(self.screen,self.black,[(7,354),(15,346),(23,354)])
        pygame.draw.polygon(self.screen,self.black,[(7,566),(15,574),(23,566)])

        pygame.draw.rect(self.screen,self.black,(25,340,100,240),1)
        for i in range(340,580,40):
            pygame.draw.rect(self.screen,self.black,(25,i,100,40),1)
            pygame.draw.rect(self.screen,self.black,(25,i,20,20),1)
            pygame.draw.rect(self.screen,self.black,(85,i,20,20),1)
            pygame.draw.rect(self.screen,self.black,(105,i,20,20),1)
            fontObj = pygame.font.SysFont('Calibri',26)
            text = fontObj.render('+',False,self.black)
            self.screen.blit(text,(105+4,i-2))
            fontObj = pygame.font.SysFont('Calibri',32)
            text = fontObj.render('-',False,self.black)
            self.screen.blit(text,(85+5,i-6))

        self.cartObj.draw(self.screen,27,365)

        pygame.draw.line(self.screen,self.black,(140,0),(140,600),15) # draw line

        

    #IN PROGRESS
    def handleEvent(self,event):      
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            if 0 < click[0] and click[0] < 50 \
                        and 0 < click[1] and click[1] < 50:
                if not self.displayStoreSection:
                    return 'MainMenu'
                else:
                    self.displayStoreSection = False
                    self.clickname = ""
                    self.clickstoresection = None
            elif 50 < click[0] and click[0] < 100 \
                        and 0 < click[1] and click[1] < 50:
                self.masterClass.help.setPreviousScreen(self.panelName)
                return 'Help'
            elif 176 < click[0] and click[0] < 326 \
                        and 378 < click[1] and click[1] < 428:
                return 'WinCards'
            elif 5 < click[0] and click[0] < 25 \
                        and 340 < click[1] and click[1] < 360:
                self.cartObj.scrollUp()
            elif 5 < click[0] and click[0] < 25 \
                        and 560 < click[1] and click[1] < 580:
                self.cartObj.scrollDown()
            elif click[0] < 140: 
                for i in range(340,580,40):
                    if i < click[1] and click[1] < i+20:
                        if 85 < click[0] and click[0] < 105:
                            index = (i - 340) // 40
                            if self.cartObj.scrollPosition+index < len(self.cartObj.cartList):
                                self.cartObj.removeFromCart(self.cartObj.cartList[self.cartObj.scrollPosition+index])
                        elif 105 < click[0] and click[0] < 125:
                            index = (i - 340) // 40
                            if self.cartObj.scrollPosition+index < len(self.cartObj.cartList):
                                self.cartObj.addToCart(self.cartObj.cartList[self.cartObj.scrollPosition+index])
            else:
                if not self.displayStoreSection:   
                    for stoppoint in self.stoppointlist:
                        if stoppoint.collision(click):
                            self.clickname = stoppoint.name      
                else:
                    for item in self.clickstoresection.products:
                        if item.collision(click):
                            self.cartObj.addToCart(item)   

        remaining = self.remainingObj.calculateRemaining(self.budgetObj.budget,self.cartObj.quantitiesBought)
        self.remainingObj.setRemaining("Remaining: ", remaining, "freesansbold.ttf", 14)

        if self.clickname != "":
            for StoreSection in self.StoreSectionlist:
                if StoreSection.name == self.clickname:
                    self.clickstoresection = StoreSection
        if self.clickstoresection != None:
            self.displayStoreSection = True
            self.draw()
        else:
            self.displayStoreSection = False
            self.draw()

            
            
