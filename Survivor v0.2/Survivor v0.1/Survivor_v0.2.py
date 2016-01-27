
print("Welcome sir")
import pygame
import sys
import os
from time import *
from Assets import *
from pygame.locals import *

#window size
pygame.init()
width = 1100
height = 600
size = ((width,height))
screen = pygame.display.set_mode(size)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (20,66,122)
offset = 50
board_size = 10
pygame.display.set_caption('Survivor')
boardgame = pygame.image.load ("TheBoard.png")
gameDisplay = pygame.display.set_mode(size)
Player1 = pygame.image.load("BoksHandschoen3.png")
Player2 = pygame.image.load("BoksHandschoen.png")
Player3 = pygame.image.load("BoksHandschoen4.png")
Player4 = pygame.image.load("BoksHandschoen2.png")

#assets
Wallpaper = pygame.image.load("WallpaperW.png")
QuitButton = pygame.image.load("QuitButton.png")
QuitB = pygame.image.load("QuitButton.png")
QuitButton2 = pygame.image.load("QuitButton2.png")
StartButton = pygame.image.load("StartButton.png")
StartB = pygame.image.load("StartButton.png")
StartButton2 = pygame.image.load("StartButton2.png")
ManualButton = pygame.image.load("ManualButton.png")
ManualB = pygame.image.load("ManualButton.png")
ManualButton2 = pygame.image.load("ManualButton2.png")

crashed = False
gameExit = False


#Music
pygame.mixer.init()
pygame.mixer.music.load("TitleMusic.mp3",)
pygame.mixer.music.play()

clock = pygame.time.Clock()
time = clock

#wallpaper logic
def wall(xw,yw):
    screen.blit(Wallpaper,(xw,yw))

#QuitButton logic
def Quit(xq,yq,QuitButton):
    screen.blit(QuitButton,(xq,yq))

#StartButton logic
def Start(xs,ys,StartButton):
    screen.blit(StartButton,(xs,ys))

#Logo logic
def Logo(xl,yl):
    screen.blit(LogoCorner,(xl,yl))

#ManualButton logic
def Manual(xm,ym,ManualButton):
    screen.blit(ManualButton,(xm,ym))

#Game assets logic
def CornerTile(x,y):
    x = (0)
    y = (0)
    gameDisplay.blit(boardgame,(x,y))

def Player1Glove(l1):
    x = l1.Position_X
    y = l1.Position_Y
    gameDisplay.blit(Player1,(x,y))

def Player2Glove(l2):
    x = l2.Position_X
    y = l2.Position_Y
    gameDisplay.blit(Player2,(x,y))

def Player3Glove(l3):
    x = l3.Position_X
    y = l3.Position_Y
    gameDisplay.blit(Player3,(x,y))
def Player4Glove(l4):
    x = l4.Position_X
    y = l4.Position_Y
    gameDisplay.blit(Player4,(x,y))

#MAINMENU
def MainMenu(crash,Exit,ManualButton, QuitButton,StartButton):
    crash = False
    xs = (width * 0.5)
    ys = (height * 0.10)
    xm = (width * 0.5)
    ym = (height * 0.4)
    xq = (width * 0.5)
    yq = (height * 0.7)
    xw = (width * 0)
    yw = (height * 0)
    xl = (width * 0.8)
    yl = (height * 0.8)
    while not crash:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    crash = True
            if event.type == pygame.QUIT:
                crash = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                crash = True
        else:
            if crash == False:
                wall(xw,yw)
                Quit(xq,yq,QuitButton)
                Start(xs,ys,StartButton)
                Manual(xm,ym,ManualButton)
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mousex, mousey = pygame.mouse.get_pos()

                #MOUSE HOOVER
                if event.type == MOUSEMOTION and mousex > 550 and mousex < 950  and mousey > 60 and mousey < 210:
                        StartButton = StartButton2
                else:
                        StartButton = StartB
                if event.type == MOUSEMOTION and mousex > 550 and mousex < 950  and mousey > 240 and mousey < 390:
                        ManualButton = ManualButton2
                else:
                        ManualButton = ManualB
                if event.type == MOUSEMOTION and mousex > 550 and mousex < 950  and mousey > 420 and mousey < 570:
                        QuitButton = QuitButton2
                else:
                        QuitButton = QuitB

                #KNOP INTERACTIE 
                if event.type == MOUSEBUTTONUP and mousex > 550 and mousex < 950  and mousey > 60 and mousey < 210:
                    Exit = False #fight
                    BoardGame(PlayerList1,PlayerList2,PlayerList3,PlayerList4,Exit,crash)
                if event.type == MOUSEBUTTONUP and mousex > 550 and mousex < 950  and mousey > 240 and mousey < 390:
                    print("Manual is still missing")      #Manual
                    
                if event.type == MOUSEBUTTONUP and mousex > 550 and mousex < 950  and mousey > 420 and mousey < 570:
                    pygame.quit()
                    quit()
                        
        pygame.display.update()
    clock.tick(60)



def BoardGame(l1,l2,l3,l4,Exit,crash):
    pygame.display.set_mode(size)
    Exit = False
    pygame.display.set_caption('Survivor')
    while not Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MainMenu(crash,Exit,ManualButton, QuitButton,StartButton)
                    
                if event.key == pygame.K_1:
                    print (event)
                    l1 = l1.tail
                if event.key == pygame.K_2:
                    print (event)
                    l2 = l2.tail
                if event.key == pygame.K_3:
                    print (event)
                    l3 = l3.tail
                if event.key == pygame.K_4:
                    print (event)
                    l4 = l4.tail
        if l1.Name == "Pos41":
            l1 = PlayerPosList1
        if l2.Name == "Pos11":
            l2 = PlayerPosList2
        if l3.Name == "Pos21":
            l3 = PlayerPosList3
        if l4.Name == "Pos31":
            l4 = PlayerPosList4
        gameDisplay.fill(blue)
        CornerTile(0,0)
        Player1Glove(l1)
        Player2Glove(l2)
        Player3Glove(l3)
        Player4Glove(l4)
        pygame.display.update()

# Aanroepencode
MainMenu(crashed,gameExit,ManualButton, QuitButton,StartButton)
pygame.quit()
quit()

