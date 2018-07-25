'''
@author Annie Li
'''
import pygame
from pygame import *
from InputBudget import InputBudget
from InputDepartment import InputDepartment

from StoreItem import product
from InputShoppingList import InputShoppingList

class Cart(object):
    def __init__(self):
        pygame.init()
        self.cartList = []
        self.quantitiesBought = {}
        self.scrollPosition = 0 

    def draw(self,screen,x,y):
        index = self.scrollPosition
        fontObj = pygame.font.Font('freesansbold.ttf',12)
        for i in range(y,y+240,40):
            if index >= len(self.cartList):
                return

            text = fontObj.render(self.cartList[index].name,True,(0,0,0))
            screen.blit(text,(x,i))
            text = fontObj.render(str(self.quantitiesBought[self.cartList[index]]),True,(0,0,0))
            screen.blit(text,(x+5,i-20))
            index += 1

    def collision(self, click):
        return self.rect.collidepoint(click)
    
    def addToCart(self, product):
        '''
        self.text = "Cart : \n"
        self.text = self.text + self.product+ "\n"
        if item.collision(click):
            product.getimage()
            product.getprice()
            Cart.AddToCart(self.text)
            image.append(CartList)
        '''
        if product in self.cartList:
            if self.quantitiesBought[product] < 9:
                self.quantitiesBought[product] += 1
        else:
            self.cartList.append(product)
            self.quantitiesBought[product] = 1

    def removeFromCart(self, product):
        if product in self.cartList:
            if self.quantitiesBought[product] == 1:
                self.quantitiesBought.pop(product)
                self.cartList.remove(product)
                self.scrollUp()
            else:
                self.quantitiesBought[product] -= 1

    def scrollUp(self):
        if self.scrollPosition > 0:
            self.scrollPosition -= 1

    def scrollDown(self):
        if self.scrollPosition < len(self.cartList) - 6:
            self.scrollPosition += 1

class Budget(object):
    
    def __init__(self, x, y, screen, text, budget, texttype, textsize):
        self.x= x
        self.y = y
        self.screen = screen
        self.budget = budget
        self.text = text + '$' + str(budget)
        self.font = pygame.font.Font(texttype, textsize)        

    def draw(self):       
        self.renderabletext = self.font.render(self.text, True, (0,0,0))
        self.screen.blit(self.renderabletext, (self.x,self.y))

    def setBudget(self,text,budget,texttype,textsize):
        self.budget = budget
        self.text = text + '$' + str(budget)
        self.font = pygame.font.Font(texttype, textsize)

class Remaining(object):
    def __init__(self, x, y, screen, text, remaining, texttype, textsize):
        pygame.init()
        self.x= x
        self.y = y
        self.screen = screen
        self.remaining = remaining
        self.text = text + '$' + str(remaining)
        self.font = pygame.font.Font(texttype, textsize)        

    def draw(self):
        if self.remaining < 0:
            self.renderabletext = self.font.render(self.text, True, (192,0,0))
        else:
            self.renderabletext = self.font.render(self.text, True, (0,0,0))
        self.screen.blit(self.renderabletext, (self.x,self.y))  

    def setRemaining(self,text,remaining,texttype,textsize):
        self.remaining = remaining
        self.text = text + '$' + str(remaining)
        self.font = pygame.font.Font(texttype, textsize)           

    def calculateRemaining(self,budget,quantitiesBought):
        remaining = budget
        for item in quantitiesBought:
            remaining -= int(item.price[1:-3]) * quantitiesBought[item] 
        return remaining
    
class ShoppingList(object):
    def __init__(self):
        pygame.init()
        self.shoppingList = {}

    def draw(self, screen, x, y, cartList, quantitiesBought):
        itemNo = 0
        fontObj = pygame.font.Font('freesansbold.ttf',12)
        for itemName in self.shoppingList:
            item = self.findItem(cartList,itemName)
            if item == None:
                quantity = 0
            else:
                quantity = quantitiesBought[item]
            text = itemName + ": " + str(quantity) + "/" + str(self.shoppingList[itemName])
            if quantity < self.shoppingList[itemName]:
                renderabletext = fontObj.render(text,True,(192,0,0))   
            else:
                renderabletext = fontObj.render(text,True,(0,192,0))  
            screen.blit(renderabletext,(x,y+itemNo*20))
            itemNo += 1

    def findItem(self, cartList, itemName):
        for item in cartList:
            if item.name == itemName:
                return item

    def collision(self, click):
        return self.rect.collidepoint(click)
    def addToShoppinglist(self, item):
        '''
        self.text = 'ShoppingList : \n'
        print(self.masterClass.inputShoppingList.shoppinglist)
        '''
        pass
    
