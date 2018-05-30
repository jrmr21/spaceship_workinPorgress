import pygame, sys

#************************************************    BY JRMR     ********************************************
#*********************************************   TRY in PYTHON 3.6  *****************************************

pygame.init()                                       # init the libraries
gameDisplay = pygame.display.set_mode((800,600))    # window size
pygame.display.set_caption('JRMR GAME IN SPACE')    #   name of this window
clock = pygame.time.Clock()                         #fps pk a voir...
background = pygame.image.load("background.jpg")                # background

screen = pygame.display.set_mode([800, 600])    # Create an 800x600 sized screen


class fire:
    skin_laser = pygame.image.load("laser_anim.gif")                # laser skin    
    skin_laser = pygame.transform.scale(skin_laser,(20,20))         # resize skin laser in 20px, 20px
    y = 30
    x = 0
    lock = 0
        
    def move(self):
        self.y += 5
        if(self.y > 550 ) :
            self.lock = 0
            
        screen.blit(self.skin_laser, [self.x, self.y])
        
    
class persoMain:                                #   main player

    name = "default"
    skin_perso = pygame.image.load("spaceship.png")                # player skin    
    skin_perso = pygame.transform.scale(skin_perso,(80,80))         # resize skin player in 80px, 80px

    missile1 = fire()

    score = 0
    x = 120                                                         # x axe to move
    y = 50                                                          # fix Y coo

    def nom(self):
        print(persoMain.name)

    def refresh(self):
        self.player_position = pygame.mouse.get_pos()                                 # connect mous with spaceship
        self.x = self.player_position[0]                                # get mouse pos
        
        if(self.x < 35):                                                # condition to block spaceship
            self.x = 35                                                 # to leave the map
        if(self.x > 745):
            self.x = 745
        screen.blit(self.skin_perso, [self.x - 30, self.y - 30])        # display skin on X, Y

        #************************** missil run *****************
        if(self.missile1.lock == 1 ):
            self.missile1.move()

        
        
    def fire(self):
        print("fire")
        if(self.missile1.lock == 0):
            self.missile1.x = self.x
            self.missile1.y = 30
            self.missile1.lock = 1
            

faucon = persoMain()        # create player
faucon.name = "chewbacca"   # LOL
font = pygame.font.SysFont("comicsansms", 25)


while True:                                                 # main game loop                          
    for event in pygame.event.get():                        # event clavier            
        if event.type == pygame.QUIT:                       # condition to leave the game
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            faucon.fire()

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render("Score {0}".format(faucon.score), False, (255, 128, 0))    # get score
    background.blit(text,(25,25))                                           # print score on background
    screen.fill((255, 255, 255))
   
    screen.blit(background, [0, 0])                                      #   coo pour l images   
    faucon.refresh()                                            # update player on background
    clock.tick(60)                                          # setting in 60 FPS ( i know...)
    pygame.display.update()                                 # update screen
    



