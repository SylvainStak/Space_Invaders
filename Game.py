import pygame, sys
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
from Player import Player
from Invader import Invader
from Bullet import Bullet

class Game:

    def __init__(self, fps, invaders_speed, bullet_speed, player_speed):                
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.display.set_caption('Space Invaders by SylvainStak')
        self.DISPLAYSURF = pygame.display.set_mode((800, 600))
        self.FPS_CLOCK = pygame.time.Clock()
        self.FPS_RATE = fps                
        self.INVADERS_SPEED = invaders_speed
        self.BULLET_SPEED = bullet_speed
        self.MoveRefX = 400
        self.MoveRefSpeed = invaders_speed
        self.SpriteSwapCounter = 0
        self.SpriteSwapCounterJump = invaders_speed
        self.Bot1Invaders = []
        self.Bot2Invaders = []
        self.Mid1Invaders = []
        self.Mid2Invaders = []
        self.TopInvaders = []
        self.Bullets = []      

        
        if self.loadSprites() == True and self.loadSounds() == True:
            self.DISPLAYSURF.blit(self.sprt_bgImage, (0, 0))
        else:
            print("Could not load the sprites needed")
            pygame.quit()
            sys.exit()
        pygame.display.set_icon(self.sprt_icon)
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

    def loadSounds(self):
        statusFlag = True
        try:
            self.sound_game_over = pygame.mixer.Sound("assets/audio/game_over.wav")            
            self.sound_win = pygame.mixer.Sound("assets/audio/win.wav")
            self.sound_shoot = pygame.mixer.Sound("assets/audio/shoot.wav")
            self.sound_invader_kill = pygame.mixer.Sound("assets/audio/invader_kill.wav")
        except: 
            statusFlag = False

        return statusFlag
    

    def drawPlayer(self):
        self.DISPLAYSURF.blit(self.Player.Sprite, (self.Player.X, self.Player.Y))

    def drawInvaders(self):
        for i in self.Bot1Invaders:
            self.DISPLAYSURF.blit(i.actual_sprite, (i.X, i.Y))
        
        for i in self.Bot2Invaders:
            self.DISPLAYSURF.blit(i.actual_sprite, (i.X, i.Y))

        for i in self.Mid1Invaders:
            self.DISPLAYSURF.blit(i.actual_sprite, (i.X, i.Y))

        for i in self.Mid2Invaders:
            self.DISPLAYSURF.blit(i.actual_sprite, (i.X, i.Y))

        for i in self.TopInvaders:
            self.DISPLAYSURF.blit(i.actual_sprite, (i.X, i.Y))
        
            
        
    def drawBullets(self):
        for i in range(0, len(self.Bullets)):
            if self.Bullets[i].Y > 0:
                self.DISPLAYSURF.blit(self.Bullets[i].Sprite, (self.Bullets[i].X, self.Bullets[i].Y))

    def moveInvaders(self):
        self.MoveRefX += self.MoveRefSpeed        


        for i in self.Bot1Invaders:
            i.move(self.MoveRefX)

        for i in self.Bot2Invaders:
            i.move(self.MoveRefX)

        for i in self.Mid1Invaders:
            i.move(self.MoveRefX)

        for i in self.Mid2Invaders:
            i.move(self.MoveRefX)

        for i in self.TopInvaders:
            i.move(self.MoveRefX)

        if self.MoveRefX > 600:
            self.MoveRefX = 600
            self.MoveRefSpeed = -self.MoveRefSpeed
        if self.MoveRefX < 200:
            self.MoveRefX = 200
            self.MoveRefSpeed = -self.MoveRefSpeed
    
    def moveBullets(self):
        for i in self.Bullets:
            if i.Y > -3:
                i.move()

    
    def setupInvaders(self):
        for i in range(0, 9):
            self.Bot1Invaders.append(Invader(i*35 + 245, 190, self.sprt_bot1, self.sprt_bot2, self.INVADERS_SPEED))
            self.Bot2Invaders.append(Invader(i*35 + 245, 160, self.sprt_bot1, self.sprt_bot2, self.INVADERS_SPEED))
            self.Mid1Invaders.append(Invader(i*35 + 245, 130, self.sprt_mid1, self.sprt_mid2, self.INVADERS_SPEED))
            self.Mid2Invaders.append(Invader(i*35 + 245, 100, self.sprt_mid1, self.sprt_mid2, self.INVADERS_SPEED))
            self.TopInvaders.append(Invader(i*35 + 249, 70, self.sprt_top1, self.sprt_top2, self.INVADERS_SPEED))

    def swapInvaderSprite(self):
        self.SpriteSwapCounter += self.SpriteSwapCounterJump

        if self.SpriteSwapCounter == 50:    
            for i in self.Bot1Invaders:
                i.changeSprite()
            for i in self.Bot2Invaders:
                i.changeSprite()
            for i in self.Mid1Invaders:
                i.changeSprite()
            for i in self.Mid2Invaders:
                i.changeSprite()
            for i in self.TopInvaders:
                i.changeSprite()
            

            self.SpriteSwapCounter = 0 


    def checkWin(self):
         if(len(self.Bot1Invaders) == 0 and
            len(self.Bot2Invaders) == 0 and
            len(self.Mid1Invaders) == 0 and
            len(self.Mid2Invaders) == 0 and
            len(self.TopInvaders) == 0):           
            
            pygame.mixer.Sound.play(self.sound_win)
            Tk().wm_withdraw()
            messagebox.showinfo('You Win', 'YOU WIN!!!\nBullets fired: ' + str(len(self.Bullets)))
            del self.Bullets[:]
            self.setupInvaders()
            self.MoveRefX = 400

    def checkGameOver(self):
        Bot1Out = False
        Bot2Out = False
        Mid1Out = False
        Mid2Out = False
        TopOut = False

        for i in self.Bot1Invaders:
            if i.Y > 550:
                Bot1Out = True
        for i in self.Bot2Invaders:
            if i.Y > 550:
                Bot2Out = True
        for i in self.Mid1Invaders:
            if i.Y > 550:
                Mid1Out = True
        for i in self.Mid2Invaders:
            if i.Y > 550:
                Mid2Out = True
        for i in self.TopInvaders:
            if i.Y > 550:
                TopOut = True

        if(Bot1Out == True or
           Bot2Out == True or
           Mid1Out == True or
           Mid2Out == True or
           TopOut == True):
           invadersLeft = len(self.Bot1Invaders) + len(self.Bot2Invaders) + len(self.Mid1Invaders) + len(self.Mid2Invaders) + len(self.TopInvaders)
           del self.Bot1Invaders[:]
           del self.Bot2Invaders[:]
           del self.Mid1Invaders[:]
           del self.Mid2Invaders[:]
           del self.TopInvaders[:]
           self.MoveRefX = 400
           pygame.mixer.Sound.play(self.sound_game_over)
           Tk().wm_withdraw()
           messagebox.showinfo('Game Over', 'GAME OVER!!!\n\nInvaders Left: ' + str(invadersLeft) + '\nBullets fired: ' + str(len(self.Bullets)))
           self.setupInvaders()
           del self.Bullets[:]
           self.MoveRefX = 400
    
    def checkCollision(self):
        Bot1_del = []
        Bot2_del = []
        Mid1_del = []
        Mid2_del = []
        Top_del = []

        if len(self.Bullets) > 0:
            if len(self.Bot1Invaders) > 0:
                for i in range(0, len(self.Bot1Invaders)):
                    for j in range(0, len(self.Bullets)):
                        if self.Bullets[j].X >= self.Bot1Invaders[i].X and self.Bullets[j].X <= self.Bot1Invaders[i].X + 24:
                            if self.Bullets[j].Y >= self.Bot1Invaders[i].Y and self.Bullets[j].Y <= self.Bot1Invaders[i].Y + 24:
                                Bot1_del.append(i)
                                self.Bullets[j].Y = 0

            for i in Bot1_del:
                del self.Bot1Invaders[i]
                pygame.mixer.Sound.play(self.sound_invader_kill)

            if len(self.Bot2Invaders) > 0:
                for i in range(0, len(self.Bot2Invaders)):
                    for j in range(0, len(self.Bullets)):
                        if self.Bullets[j].X >= self.Bot2Invaders[i].X and self.Bullets[j].X <= self.Bot2Invaders[i].X + 24:
                            if self.Bullets[j].Y >= self.Bot2Invaders[i].Y and self.Bullets[j].Y <= self.Bot2Invaders[i].Y + 24:
                                Bot2_del.append(i)
                                self.Bullets[j].Y = 0

            for i in Bot2_del:
                del self.Bot2Invaders[i]
                pygame.mixer.Sound.play(self.sound_invader_kill)

            if len(self.Mid1Invaders) > 0:
                for i in range(0, len(self.Mid1Invaders)):
                    for j in range(0, len(self.Bullets)):
                        if self.Bullets[j].X >= self.Mid1Invaders[i].X and self.Bullets[j].X <= self.Mid1Invaders[i].X + 24:
                            if self.Bullets[j].Y >= self.Mid1Invaders[i].Y and self.Bullets[j].Y <= self.Mid1Invaders[i].Y + 24:
                                Mid1_del.append(i)
                                self.Bullets[j].Y = 0

            for i in Mid1_del:
                del self.Mid1Invaders[i]
                pygame.mixer.Sound.play(self.sound_invader_kill)

            if len(self.Mid2Invaders) > 0:
                for i in range(0, len(self.Mid2Invaders)):
                    for j in range(0, len(self.Bullets)):
                        if self.Bullets[j].X >= self.Mid2Invaders[i].X and self.Bullets[j].X <= self.Mid2Invaders[i].X + 24:
                            if self.Bullets[j].Y >= self.Mid2Invaders[i].Y and self.Bullets[j].Y <= self.Mid2Invaders[i].Y + 24:
                                Mid2_del.append(i)
                                self.Bullets[j].Y = 0

            for i in Mid2_del:
                del self.Mid2Invaders[i]
                pygame.mixer.Sound.play(self.sound_invader_kill)

            if len(self.TopInvaders) > 0:
                for i in range(0, len(self.TopInvaders)):
                    for j in range(0, len(self.Bullets)):
                        if self.Bullets[j].X >= self.TopInvaders[i].X and self.Bullets[j].X <= self.TopInvaders[i].X + 24:
                            if self.Bullets[j].Y >= self.TopInvaders[i].Y and self.Bullets[j].Y <= self.TopInvaders[i].Y + 24:
                                Top_del.append(i)
                                self.Bullets[j].Y = 0

            for i in Top_del:
                del self.TopInvaders[i]      
                pygame.mixer.Sound.play(self.sound_invader_kill)

            


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
            
            if keys_pressed[pygame.K_x]:
                allowed = True
                for i in self.Bullets:
                    if i.Y > 75:
                        allowed = False
                
                if allowed == True:
                    pygame.mixer.Sound.play(self.sound_shoot)
                    self.Bullets.append(Bullet(self.Player.X + 16, self.Player.Y, self.sprt_bullet, self.BULLET_SPEED))
       
            
            self.DISPLAYSURF.blit(self.sprt_bgImage, (0, 0))
            self.drawBullets()
            self.moveInvaders()
            self.moveBullets()
            self.swapInvaderSprite()
            self.drawInvaders()
            self.drawPlayer()                        
            self.checkGameOver()
            self.checkWin()
            self.checkCollision()
            pygame.display.update()
            self.FPS_CLOCK.tick(self.FPS_RATE)
        
