import pygame, sys
from pygame.locals import *
from Player import Player
from Invader import Invader

class Game:

    def __init__(self, fps, invaders_speed, bullet_speed, player_speed):                
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((800, 600))
        self.FPS_CLOCK = pygame.time.Clock()
        self.FPS_RATE = fps                
        self.INVADERS_SPEED = invaders_speed
        self.BULLET_SPEED = bullet_speed
        self.SpriteSwapRef = 0
        self.Bot1Invaders = []
        self.Bot2Invaders = []
        self.Mid1Invaders = []
        self.Mid2Invaders = []
        self.TopInvaders = []
        self.Bullets = []      

        
        if self.loadSprites() == True:
            self.DISPLAYSURF.blit(self.sprt_bgImage, (0, 0))
        else:
            print("Could not load the sprites needed")
            pygame.quit()
            sys.exit()
        
        self.Player = Player(384, 580, self.sprt_ship, player_speed)
        self.setupInvaders()
            

    #Loads the sprites needed
    #Returns True if everything went OK
    #Returns False if one or more sprites could not be loaded 
    def loadSprites(self):
        statusFlag = True
        try:
            self.sprt_bgImage = pygame.image.load("assets/background_image.jpg")
            self.sprt_icon = pygame.image.load("assets/icon.png")
            self.sprt_bot1 = pygame.image.load("assets/bot1.png")
            self.sprt_bot2 = pygame.image.load("assets/bot2.png")
            self.sprt_mid1 = pygame.image.load("assets/mid1.png")
            self.sprt_mid2 = pygame.image.load("assets/mid2.png")
            self.sprt_top1 = pygame.image.load("assets/top1.png")
            self.sprt_top2 = pygame.image.load("assets/top2.png")
            self.sprt_ship = pygame.image.load("assets/ship.png")
            self.sprt_bullet = pygame.image.load("assets/bullet.png")
        except:
            statusFlag = False
        
        return statusFlag

    def drawPlayer(self):
        self.DISPLAYSURF.blit(self.Player.Sprite, (self.Player.X, self.Player.Y))

    def drawInvaders(self):
        for i in range(0, 9):
            self.DISPLAYSURF.blit(self.Bot1Invaders[i].actual_sprite, (self.Bot1Invaders[i].X, self.Bot1Invaders[i].Y))
            self.DISPLAYSURF.blit(self.Bot2Invaders[i].actual_sprite, (self.Bot2Invaders[i].X, self.Bot2Invaders[i].Y))
            self.DISPLAYSURF.blit(self.Mid1Invaders[i].actual_sprite, (self.Mid1Invaders[i].X, self.Mid1Invaders[i].Y))
            self.DISPLAYSURF.blit(self.Mid2Invaders[i].actual_sprite, (self.Mid2Invaders[i].X, self.Mid2Invaders[i].Y))
            self.DISPLAYSURF.blit(self.TopInvaders[i].actual_sprite, (self.TopInvaders[i].X, self.TopInvaders[i].Y))
    
    
    def setupInvaders(self):
        for i in range(0, 9):
            self.Bot1Invaders.append(Invader(i*35 + 245, 190, self.sprt_bot1, self.sprt_bot2, self.INVADERS_SPEED))
            self.Bot2Invaders.append(Invader(i*35 + 245, 160, self.sprt_bot1, self.sprt_bot2, self.INVADERS_SPEED))
            self.Mid1Invaders.append(Invader(i*35 + 245, 130, self.sprt_mid1, self.sprt_mid2, self.INVADERS_SPEED))
            self.Mid2Invaders.append(Invader(i*35 + 245, 100, self.sprt_mid1, self.sprt_mid2, self.INVADERS_SPEED))
            self.TopInvaders.append(Invader(i*35 + 249, 70, self.sprt_top1, self.sprt_top2, self.INVADERS_SPEED))



    #Starts the game loop
    def StartGameLoop(self):
        while True:

            #Handle Events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_LEFT]:
                self.Player.moveLeft()

            if keys_pressed[pygame.K_RIGHT]:
                self.Player.moveRight()
            
            self.DISPLAYSURF.blit(self.sprt_bgImage, (0, 0))
            self.drawInvaders()
            self.drawPlayer()
            pygame.display.update()
            self.FPS_CLOCK.tick(self.FPS_RATE)
        
