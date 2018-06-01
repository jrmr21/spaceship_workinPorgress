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
    i = date.second                                     # get start second
    while True:                                 # infinit looooooop ( do loop a history function RIP xDD )
        date = datetime.datetime.now()          # get time NOW
        if(date.second > i + 3):                # in 3s in the future
            program()                           # run game
    
    
    
def checkScore( enemyC, persoC):            # check if you kik an enemy
    if(persoC.missile1.lock == 1 and enemyC.explosion == 0):        # if your missil is lock and enemy don't explodes
        if((persoC.missile1.y < enemyC.y+70) & (persoC.missile1.y > enemyC.y - 70) & (persoC.missile1.x < enemyC.x+70) & (persoC.missile1.x > enemyC.x )):
            persoC.score += 1           # score ++
            persoC.missile1.lock = 0    # unlock missil
            enemyC.vie = 0              # kill enemy
            enemyC.explosion = 15       # run explosion enemy for 15 looping
            
                       
def checkBoss( enemyC, persoC):             # check if you kik the boss
    if(persoC.missile1.lock == 1):          #   check if you missil is lock
        if((persoC.missile1.y < enemyC.y+15) & (persoC.missile1.y > enemyC.y - 95) & (persoC.missile1.x < enemyC.x+45) & (persoC.missile1.x > enemyC.x )):
            persoC.score += 2           # add 2 in your score
            persoC.missile1.lock = 0        # unlock missil
            enemyC.POWER -= 1           # remove 1 HP in the boss
            if(enemyC.POWER < 1):        # if the boss is dead
                persoC.score += 5           # add 5point in your score

            
class boss :                    #   boss object
    x = 120                     # default X
    y = 45                       # default Y
    xpos = 0                # objectif to move axe X
    ypos = 0                # objectif to move axe Y
    POWER = 0               #life BOSS
    vitesse = 3                 # speed move (3px)
    
    skin_boss1 = pygame.image.load("boss1.png")                # boss GOOD skin    
    skin_boss1 = pygame.transform.scale(skin_boss1,(85,100))         # resize skin enemy in 85px, 100px

    skin_boss2 = pygame.image.load("boss2.png")                # boss NORMAL skin    
    skin_boss2 = pygame.transform.scale(skin_boss2,(85,100))         # resize skin enemy in 85px, 100px

    skin_boss3 = pygame.image.load("boss3.png")                # boss my ass is teflon ? skin    
    skin_boss3 = pygame.transform.scale(skin_boss3,(85,100))         # resize skin enemy in 85px, 100px
    
    axeX = 0            # axe X checkup if you finish move to X
    axeY = 0            # axe Y checkup if you finish move to Y
    def move(self):
        if(self.POWER == 0 or self.axeY == 1 & self.axeX == 1 ): # check if boss is dead or boss finish to move
            self.xpos = random.randrange(90, 710)           # random X goal
            self.ypos = random.randrange(80, 390)           # random Y goal
            self.vitesse = random.randrange(3, 7)           # speed random (muAHAHA ! )
            self.axeX = 0                              # reste goal moving to X
            self.axeY = 0                              # reste goal moving to Y
            
            
        if(self.POWER == 0) :       # if boss is dead reset her life
            self.POWER = 10

        if( self.x < self.xpos - 5):             # condition to going to X goal and stop to moving if it's okay       
           self.x += self.vitesse
        elif ( self.x > self.xpos + 5):
           self.x -= self.vitesse
        else :
            self.axeX= 1 
           
        if( self.y < self.ypos - 5):            # condition to going to Y goal and stop to moving if it's okay
           self.y += self.vitesse
        elif ( self.y > self.ypos + 5):
           self.y -= self.vitesse
        else :
            self.axeY = 1 
        
        if(self.POWER > 8 ) :                                   # change skin about your life
            screen.blit(self.skin_boss1, [self.x, self.y])
        elif(self.POWER > 5 ) :
            screen.blit(self.skin_boss2, [self.x, self.y])
        else:
            screen.blit(self.skin_boss3, [self.x, self.y])
        

class enemy :
    x = 0                   # default X position 
    y = 0                   # default Y position 
    skin_enemy = pygame.image.load("enemy.gif")                # enemy skin    
    skin_enemy = pygame.transform.scale(skin_enemy,(70,70))         # resize skin enemy in 70px, 70px
    
    skin_boum = pygame.image.load("boum.png")                # enemy skin    
    skin_boum = pygame.transform.scale(skin_boum,(70,70))         # resize skin enemy in 70px, 70px
    vie = 0                                                   # enemy live (to respawn)
    explosion = 0                                            #   explosion life
    def move(self):                             #   move function
        if(self.vie != 0):                  #   if enemi are not dead
            self.vie -= 1                                     # decrease life
            screen.blit(self.skin_enemy, [self.x, self.y])      # display skin enemy
            
        elif(self.explosion != 0):          # if you are kik you decrease explosion life to 0
            self.explosion -= 1         # decrease expllosion life
            screen.blit(self.skin_boum, [self.x, self.y])       # display skin of explosion
            
        else :
            self.vie = random.randrange(95,155)     # random reset life to respawn
            self.x = random.randrange(90,690)       # random reset x coo
            self.y = random.randrange(80,430)       # random reset y coo
            
            

class fire:
    skin_laser = pygame.image.load("laser_anim.gif")                # laser skin    
    skin_laser = pygame.transform.scale(skin_laser,(30,30))         # resize skin laser in 20px, 20px
    y = 30                              # set default Y
    x = 0                                # set default X
    lock = 0                            # unlock missil ( default value)
        
    def move(self):
        self.y -= 9                         # move missil 9px per 9px
        if(self.y < 50 ) :                  # if the missil end to move you unlock 
            self.lock = 0    
        screen.blit(self.skin_laser, [self.x, self.y])  # display the missil
        
    
class persoMain:                                #   main player

    name = "default"
    skin_perso = pygame.image.load("spaceship1.png")                # player skin    
    skin_perso = pygame.transform.scale(skin_perso,(80,80))         # resize skin player in 80px, 80px

    missile1 = fire()                   # creat object missil

    score = 0
    x = 120                   # x axe to move
    y = 520                  # fix Y coo

    def nom(self):
        print(persoMain.name)

    def refresh(self):
        self.player_position = pygame.mouse.get_pos()                # connect mous with spaceship
        self.x = self.player_position[0]                                # get mouse pos
        
        if(self.x < 35):                                                # condition to block spaceship
            self.x = 35                                                 # to leave the map
        if(self.x > 745):
            self.x = 745
        screen.blit(self.skin_perso, [self.x - 30, self.y - 30])        # display skin on X, Y

        #************************** missil run *****************
        if(self.missile1.lock == 1 ):           # if the missil is lock
            self.missile1.move()            # move the missil
        
    def fire(self):                                 # if the missil don't exist
        if(self.missile1.lock == 0):
            self.missile1.x = self.x - 5            # set the X pos under 5px to mouse (the center gamer)
            self.missile1.y = 510                   # set the Y start pos to start
            self.missile1.lock = 1                  # you lock the missil (to move)

def fin(score):

    fichier = open("score.txt", "r")            # open best score file
    bestScore = int(fichier.read())             # read value (convert char to int)
    fichier.close()                             # close file
    if(score > bestScore):                      # check if your are the best, or no...
        bestScore = score                       # if you are the best you update bestscore
        fichier = open("score.txt", "w")            # write score 
        fichier.write(str(score))                   # write score in char (convert in to char)
        fichier.close()                             # close file
    
    menu = pygame.image.load("end.png")                # background
    pygame.transform.scale(menu,(800,600))         # resize background
    screen.blit(menu, [0, 0])                                      #   coo pour l images

    font = pygame.font.SysFont("arial", 45)           # font pous les scores
    textScore = font.render("ton score : {0}".format(score), False, (0, 0, 0))    # get score
    screen.blit(textScore,(350,270))

    font = pygame.font.SysFont("arial", 50)           # font pous les best scores
    textScore = font.render("meilleur score : {0}".format(bestScore), False, (0, 0, 0))    # get score
    screen.blit(textScore,(350,400))
    
    pygame.display.update()                                 # update screen
    click = 4                                                   # anti spam
    while True:                                                 # main game loop                          
        for event in pygame.event.get():                        # event clavier            
            if event.type == pygame.QUIT:                       # condition to leave the game
                pygame.quit()
                sys.exit()                                      # quit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click -= 1                                      # additional mouse click ( anti spam)
                if(click < 1 ) :
                    program()                                   # run program again

    
def program() :
    faucon = persoMain()                # create player
    faucon.name = "chewbacca"           # LOL

    boite_a_caca = [enemy(), enemy(), enemy(), enemy(), enemy(), enemy()]   # liste d'ennemi
    BIGboss = boss()                                                        # generation du boss

    font = pygame.font.SysFont("comicsansms", 25)           # font pous les scores

    minutes = 1                                 # reglage temps chrono
    secondes = 60
    timeTemporaire = 0
    while True:                                                 # main game loop                          
        for event in pygame.event.get():                        # event clavier            
            if event.type == pygame.QUIT:                       # condition to leave the game
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:          #   gamer fire run
                faucon.fire()
        
        
        screen.blit(background, [0, 0])                                      #   coo pour l images   
        faucon.refresh()                                            # update player on background

        text = font.render("Score {0}".format(faucon.score), False, (255, 128, 0))    # get score
        screen.blit(text,(25,25))                                           # print score on background
        
        for i in range(6):                      # check and move all enemys
            boite_a_caca[i].move()                  # move
            checkScore(boite_a_caca[i], faucon)     # check 


        BIGboss.move()                      #   move the boss on the screen
        checkBoss(BIGboss, faucon)          # check if you kik the boss

        date = datetime.datetime.now()      # get time
        
        if(timeTemporaire != date.second):      # if it's 1second
            timeTemporaire = date.second
            if(secondes < 1 ):                  # if it's 1 minutes
                minutes -=1                 # decrease 1 minute
                if(minutes < 0):            # if minutes it's == 0 it's end game
                    fin(faucon.score)       # call end display with gamer score
                secondes = 60               #   reset second (60)
            secondes -= 1                   # decrease 1 second
        
        textMinutes = font.render("temps: {0}".format(minutes), False, (255, 128, 0))    # display sec
        screen.blit(textMinutes,(615,25))
        textSecondes = font.render(": {0}".format(secondes), False, (255, 128, 0))    # display min
        screen.blit(textSecondes,(730,25))
        
        clock.tick(30)                                      # set FPS (game speed)
        pygame.display.update()                                 # update screen


menu()          # run menu and all game
