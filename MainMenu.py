import sys, pygame, time



class MainMenu(object):  

    def __init__(self):
        pygame.init()

        self.displaySize = (900,600)
        self.screen = pygame.display.set_mode(self.displaySize)
        self.panelName = "Main Menu"
        pygame.display.set_caption(self.panelName)

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

    def __str__(self):
        return self.panelName

    def run(self):
        self.screen.fill(self.WHITE)
        pygame.display.update()
        
        self.hasExited = False
        while not self.hasExited:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.hasExited = True

            self.screen.fill(self.WHITE)
            pygame.display.update()

            

obj = MainMenu()
obj.run()

