#by Evan D.
#The item is the first appearance of the checkout button.
def CheckoutButton (X,Y)
    CheckFont = pygame.font.Font('freesansbold.ttf', 30)
    Button_name= CheckFont.render("Checkout", True, red)
    CheckButton= Button_name.get_rect()
    CheckButton_center = (X,Y)
    screen.blit(Button_name, CheckButton_center)
    pygame.display.update()
