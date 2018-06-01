import pygame, sys, random, datetime

#************************************************    BY JRMR     ********************************************
#*********************************************   TRY in PYTHON 3.6  *****************************************

pygame.init()                                       # init the libraries
gameDisplay = pygame.display.set_mode((800,600))    # window size
pygame.display.set_caption('JRMR GAME IN SPACE')    #   name of this window
clock = pygame.time.Clock()                         #fps pk a voir...
background = pygame.image.load("background.jpg")                # background

screen = pygame.display.set_mode([800, 600])    # Create an 800x600 sized screen


def menu():
    menu = pygame.image.load("menu.png")                # background
    pygame.transform.scale(menu,(800,600))         # resize skin enemy in 70px, 70px
    screen.blit(menu, [-130, 0])                                      #   coo pour l images   
    pygame.display.update()                                 # update screen
    date = datetime.datetime.now()
    i = date.second
    while True:
        date = datetime.datetime.now()
        if(date.second > i + 3):
            program()
    
    
    
def checkScore( enemyC, persoC):
    if(persoC.missile1.lock == 1 and enemyC.explosion == 0):
        if((persoC.missile1.y < enemyC.y+70) & (persoC.missile1.y > enemyC.y - 70) & (persoC.missile1.x < enemyC.x+70) & (persoC.missile1.x > enemyC.x )):
            persoC.score += 1
            persoC.missile1.lock = 0
            enemyC.vie = 0
            enemyC.explosion = 15
            
                       
def checkBoss( enemyC, persoC):
    if(persoC.missile1.lock == 1):
        if((persoC.missile1.y < enemyC.y+15) & (persoC.missile1.y > enemyC.y - 95) & (persoC.missile1.x < enemyC.x+45) & (persoC.missile1.x > enemyC.x )):
            persoC.score += 2
            persoC.missile1.lock = 0
            enemyC.POWER -= 1
            if(enemyC.POWER < 1):
                persoC.score += 5

            
class boss :
    x = 120
    y = 45
    xpos = 0
    ypos = 0
    POWER = 0
    vitesse = 3
    
    skin_boss1 = pygame.image.load("boss1.png")                # enemy skin    
    skin_boss1 = pygame.transform.scale(skin_boss1,(85,100))         # resize skin enemy in 70px, 70px

    skin_boss2 = pygame.image.load("boss2.png")                # enemy skin    
    skin_boss2 = pygame.transform.scale(skin_boss2,(85,100))         # resize skin enemy in 70px, 70px

    skin_boss3 = pygame.image.load("boss3.png")                # enemy skin    
    skin_boss3 = pygame.transform.scale(skin_boss3,(85,100))         # resize skin enemy in 70px, 70px
    
    axeX = 0
    axeY = 0
    def move(self):
        if(self.POWER == 0 or self.axeY == 1 & self.axeX == 1 ):
            
            self.xpos = random.randrange(90, 710)
            self.ypos = random.randrange(80, 390)
            self.vitesse = random.randrange(3, 7)
            self.axeX = 0
            self.axeY = 0
            
            
        if(self.POWER == 0) :
            self.POWER = 10

        if( self.x < self.xpos - 5):
           self.x += self.vitesse
        elif ( self.x > self.xpos + 5):
           self.x -= self.vitesse
        else :
            self.axeX= 1 
           
        if( self.y < self.ypos - 5):
           self.y += self.vitesse
        elif ( self.y > self.ypos + 5):
           self.y -= self.vitesse
        else :
            self.axeY = 1 
        
        if(self.POWER > 8 ) :
            screen.blit(self.skin_boss1, [self.x, self.y])
        elif(self.POWER > 5 ) :
            screen.blit(self.skin_boss2, [self.x, self.y])
        else:
            screen.blit(self.skin_boss3, [self.x, self.y])
        

class enemy :
    x = 0
    y = 0
    skin_enemy = pygame.image.load("enemy.gif")                # enemy skin    
    skin_enemy = pygame.transform.scale(skin_enemy,(70,70))         # resize skin enemy in 70px, 70px
    
    skin_boum = pygame.image.load("boum.png")                # enemy skin    
    skin_boum = pygame.transform.scale(skin_boum,(70,70))         # resize skin enemy in 70px, 70px
    vie = 0
    explosion = 0
    def move(self):            
            
        if(self.vie != 0):
            self.vie -= 1    
            screen.blit(self.skin_enemy, [self.x, self.y])
            
        elif(self.explosion != 0):
            self.explosion -= 1    
            screen.blit(self.skin_boum, [self.x, self.y])
            
        else :
            self.vie = random.randrange(95,155)
            self.x = random.randrange(90,690)
            self.y = random.randrange(80,430)
            
            

class fire:
    skin_laser = pygame.image.load("laser_anim.gif")                # laser skin    
    skin_laser = pygame.transform.scale(skin_laser,(30,30))         # resize skin laser in 20px, 20px
    y = 30
    x = 0
    lock = 0
        
    def move(self):
        self.y -= 9
        if(self.y < 50 ) :
            self.lock = 0
            
        screen.blit(self.skin_laser, [self.x, self.y])
        
    
class persoMain:                                #   main player

    name = "default"
    skin_perso = pygame.image.load("spaceship1.png")                # player skin    
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
        if(self.missile1.lock == 0):
            self.missile1.x = self.x - 5
            self.missile1.y = 510
            self.missile1.lock = 1

def fin(score):

    fichier = open("score.txt", "r")
    bestScore = int(fichier.read())
    fichier.close()
    if(score > bestScore):
        bestScore = score
        fichier = open("score.txt", "w")
        fichier.write(str(score))
        fichier.close()
    
    menu = pygame.image.load("end.png")                # background
    pygame.transform.scale(menu,(800,600))         # resize skin enemy in 70px, 70px
    screen.blit(menu, [0, 0])                                      #   coo pour l images

    font = pygame.font.SysFont("arial", 45)           # font pous les scores
    textScore = font.render("ton score : {0}".format(score), False, (0, 0, 0))    # get score
    screen.blit(textScore,(350,270))

    font = pygame.font.SysFont("arial", 50)           # font pous les scores
    textScore = font.render("meilleur score : {0}".format(bestScore), False, (0, 0, 0))    # get score
    screen.blit(textScore,(350,400))
    
    pygame.display.update()                                 # update screen
    while True:                                                 # main game loop                          
        for event in pygame.event.get():                        # event clavier            
            if event.type == pygame.QUIT:                       # condition to leave the game
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                program()

    
def program() :
    faucon = persoMain()        # create player
    faucon.name = "chewbacca"   # LOL

    boite_a_caca = [enemy(), enemy(), enemy(), enemy(), enemy(), enemy()]
    BIGboss = boss()

    font = pygame.font.SysFont("comicsansms", 25)           # font pous les scores

    minutes = 1
    secondes = 60
    timeTemporaire = 0
    while True:                                                 # main game loop                          
        for event in pygame.event.get():                        # event clavier            
            if event.type == pygame.QUIT:                       # condition to leave the game
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                faucon.fire()
        
        
        screen.blit(background, [0, 0])                                      #   coo pour l images   
        faucon.refresh()                                            # update player on background

        text = font.render("Score {0}".format(faucon.score), False, (255, 128, 0))    # get score
        screen.blit(text,(25,25))                                           # print score on background
        
        for i in range(6):
            boite_a_caca[i].move()
            checkScore(boite_a_caca[i], faucon)


        BIGboss.move()
        checkBoss(BIGboss, faucon)

        date = datetime.datetime.now()
        
        if(timeTemporaire != date.second):
            timeTemporaire = date.second
            if(secondes < 1 ):
                minutes -=1
                if(minutes < 0):
                    fin(faucon.score)
                secondes = 60
            secondes -= 1
        
        textMinutes = font.render("temps: {0}".format(minutes), False, (255, 128, 0))    # get score
        screen.blit(textMinutes,(615,25))
        textSecondes = font.render(": {0}".format(secondes), False, (255, 128, 0))    # get score
        screen.blit(textSecondes,(730,25))
        
        clock.tick(30)
        pygame.display.update()                                 # update screen


menu()
