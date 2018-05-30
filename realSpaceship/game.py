import pygame, sys
import random

#************************************************    BY JRMR     ********************************************
#*********************************************   TRY in PYTHON 3.6  *****************************************

pygame.init()                                       # init the libraries
gameDisplay = pygame.display.set_mode((800,600))    # window size
pygame.display.set_caption('JRMR GAME IN SPACE')    #   name of this window
clock = pygame.time.Clock()                         #fps pk a voir...
background = pygame.image.load("background.jpg")                # background

screen = pygame.display.set_mode([800, 600])    # Create an 800x600 sized screen


    
def checkScore( enemyC, persoC):
    if(persoC.missile1.lock == 1):
        if((persoC.missile1.y < enemyC.y+15) & (persoC.missile1.y > enemyC.y - 95) & (persoC.missile1.x < enemyC.x+45) & (persoC.missile1.x > enemyC.x )):
            persoC.score += 1
            persoC.missile1.lock = 0
            enemyC.vie = 0
            print(persoC.score)
                       
    
class enemy :
    x = 0
    y = 0
    skin_enemy = pygame.image.load("enemy.gif")                # enemy skin    
    skin_enemy = pygame.transform.scale(skin_enemy,(70,70))         # resize skin enemy in 70px, 70px
    vie = 0
    
    def move(self):
        if(self.vie == 0) :
            self.vie = 130
            self.x = random.randrange(90,690)
            self.y = random.randrange(80,430)
        self.vie -= 1    
        screen.blit(self.skin_enemy, [self.x, self.y])


class fire:
    skin_laser = pygame.image.load("laser_anim.gif")                # laser skin    
    skin_laser = pygame.transform.scale(skin_laser,(20,20))         # resize skin laser in 20px, 20px
    y = 30
    x = 0
    lock = 0
        
    def move(self):
        self.y -= 7
        if(self.y < 50 ) :
            self.lock = 0
            
        screen.blit(self.skin_laser, [self.x, self.y])
        
    
class persoMain:                                #   main player

    name = "default"
    skin_perso = pygame.image.load("spaceship.png")                # player skin    
    skin_perso = pygame.transform.scale(skin_perso,(80,80))         # resize skin player in 80px, 80px

    missile1 = fire()

    score = 0
    x = 120                                                         # x axe to move
    y = 520                                                          # fix Y coo

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
            self.missile1.y = 510
            self.missile1.lock = 1
            

faucon = persoMain()        # create player
faucon.name = "chewbacca"   # LOL
font = pygame.font.SysFont("comicsansms", 25)           # font pous les scores

boite_a_caca1 = enemy()


while True:                                                 # main game loop                          
    for event in pygame.event.get():                        # event clavier            
        if event.type == pygame.QUIT:                       # condition to leave the game
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            faucon.fire()

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render("Score {0}".format(faucon.score), False, (255, 128, 0))    # get score
    
    screen.fill((255, 255, 255))

    
    screen.blit(background, [0, 0])                                      #   coo pour l images   
    faucon.refresh()                                            # update player on background
    clock.tick(60)                                          # setting in 60 FPS ( i know...)

    boite_a_caca1.move()
    checkScore(boite_a_caca1,faucon)
    background.blit(text,(25,25))                                           # print score on background
    pygame.display.update()                                 # update screen
