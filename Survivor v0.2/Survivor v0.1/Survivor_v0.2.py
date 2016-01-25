print("Welcome sir")
import pygame
import sys
import os
from time import*
from Assets import *
from pygame.locals import *
from win32api import GetSystemMetrics

print ("Width =", GetSystemMetrics(0))
print ("Height =", GetSystemMetrics(1))

#window size
pygame.init()
size = width, height = GetSystemMetrics(0),GetSystemMetrics(1)
screen = pygame.display.set_mode(size)
offset = 50
board_size = 10
pygame.display.set_caption('Survivor')




#assets
if size == (1600, 900):
    Wallpaper = pygame.image.load("MenuWallpaper900p.png")
if size == (1920, 1080):
    Wallpaper = pygame.image.load("MenuWallpaper1080p.png")
if size == (1366,768):
    Wallpaper = pygame.image.load("MenuWallpaper796p.png")
if size == (1600, 900):
    Board = pygame.image.load("BoardGame900p.png")
if size == (1920, 1080):
    Board = pygame.image.load("BoardGame1080p.png")
QuitButton = pygame.image.load("QuitButton.png")
QuitB = pygame.image.load("QuitButton.png")
StartButton = pygame.image.load("StartButton.png")
StartB = pygame.image.load("StartButton.png")
ManualButton = pygame.image.load("ManualButton.png")
ManualB = pygame.image.load("ManualButton.png")
LogoCorner = pygame.image.load("LogoSmall.png")

#Music
#music
pygame.mixer.init()
pygame.mixer.music.load("TitleMusic.mp3",)
pygame.mixer.music.play()

clock = pygame.time.Clock()
time = clock

#wallpaper logic
def wall(xw,yw):
    screen.blit(Wallpaper,(xw,yw))

#QuitButton logic
def Quit(xq,yq):
    screen.blit(QuitButton,(xq,yq))

#StartButton logic
def Start(xs,ys):
    screen.blit(StartButton,(xs,ys))

#Logo logic
def Logo(xl,yl):
    screen.blit(LogoCorner,(xl,yl))

#ManualButton logic
def Manual(xm,ym):
    screen.blit(ManualButton,(xm,ym))

#hierdoor blijft t beeld staan for some reason + Fullscreen
def CornerTile(x,y):
    x = (0)
    y = (0)
    gameDisplay.blit(boardgame,(x,y))

def Player1Glove(List):
    x = PlayerList1.Position_X
    y = PlayerList1.Position_Y
    gameDisplay.blit(Player1,(x,y))

def Player2Glove(List):
    x = PlayerList2.Position_X
    y = PlayerList2.Position_Y
    gameDisplay.blit(Player2,(x,y))

def Player3Glove(List):
    x = PlayerList3.Position_X
    y = PlayerList3.Position_Y
    gameDisplay.blit(Player3,(x,y))
def Player4Glove(List):
    x = PlayerList4.Position_X
    y = PlayerList4.Position_Y
    gameDisplay.blit(Player4,(x,y))
Willem is raar
DISPLAYSURF = pygame.display.set_mode((0,0),FULLSCREEN)
gameExit = True
crashed = False
while not crashed:
    xs = (width * 0.6)
    ys = (height * 0.2)
    xm = (width * 0.6)
    ym = (height * 0.4)
    xq = (width * 0.6)
    yq = (height * 0.6)
    xw = (width * 0)
    yw = (height * 0)
    xl = (width * 0.8)
    yl = (height * 0.8)
   
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = False
                crashed = True
        if event.type == pygame.QUIT:
            crashed = True

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            crashed = True

    else:
        if crashed == False:
            wall(xw,yw)
            Quit(xq,yq)
            Start(xs,ys)
            #Logo(xl,yl)
            Manual(xm,ym)


            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    mousex, mousey = pygame.mouse.get_pos()

                    ####Lijst van buttons met class maken dat je makkelijk een button kan toewijzen.

                    #Mouse hoover
            if size == (1600, 900):
                if event.type == MOUSEMOTION and mousex > 960 and mousex < 1360  and mousey > 540 and mousey < 690:
                    QuitButton = pygame.image.load("QuitButton2.png")
                else:
                    QuitButton = QuitB
                if event.type == MOUSEMOTION and mousex > 960 and mousex < 1360  and mousey > 180 and mousey < 330:
                    StartButton = pygame.image.load("StartButton2.png")
                else:
                    StartButton = StartB
                if event.type == MOUSEMOTION and mousex > 960 and mousex < 1360  and mousey > 360 and mousey < 510:
                    ManualButton = pygame.image.load("ManualButton2.png")
                else:
                    ManualButton = ManualB


                #Scaling 
####################################################################################################################################################################################
            if size == (1920,1080):             #1080p
                if event.type == MOUSEBUTTONUP and mousex > 1152 and mousex < 1552  and mousey > 216 and mousey < 366:
                    crashed = True      #Fight
                    gameExit = False
                if event.type == MOUSEBUTTONUP and mousex > 1152 and mousex < 1552  and mousey > 648 and mousey < 798:
                    crashed = True      #Quit
                if event.type == MOUSEBUTTONUP and mousex > 1152 and mousex < 1552  and mousey > 432 and mousey < 582:
                    print("Manual is still missing")      #Manual

            if size == (1600, 900):             #900p
                if event.type == MOUSEBUTTONUP and mousex > 960 and mousex < 1360  and mousey > 180 and mousey < 330:
                    crashed = True      #Fight
                    gameExit = False
                if event.type == MOUSEBUTTONUP and mousex > 960 and mousex < 1360  and mousey > 540 and mousey < 690:
                    crashed = True      #Quit
                if event.type == MOUSEBUTTONUP and mousex > 960 and mousex < 1360  and mousey > 360 and mousey < 510:
                    print("Manual is still missing")    #Manual

            if size == (1366, 768):             #768
                if event.type == MOUSEBUTTONUP and mousex > 820 and mousex < 1360  and mousey > 154 and mousey < 304:
                    crashed = True
                    gameExit = False  #Fight
                if event.type == MOUSEBUTTONUP and mousex > 820 and mousex < 1220  and mousey > 461 and mousey < 611:
                    crashed = True     #quit
                if event.type == MOUSEBUTTONUP and mousex > 820 and mousex < 1360  and mousey > 307 and mousey < 457:
                    print("Manual is still missing")  #Manual

            pygame.display.update()

            
    clock.tick(60)


display_width = 600
display_height = 800
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
boardgame = pygame.image.load ("Board.png")
gameDisplay = pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption('Survivor')
Player1 = pygame.image.load("BoksHandschoen3.png")
Player2 = pygame.image.load("BoksHandschoen.png")
Player3 = pygame.image.load("BoksHandschoen4.png")
Player4 = pygame.image.load("BoksHandschoen2.png")
DISPLAYSURF = pygame.display.set_mode((0,0),FULLSCREEN)

while not gameExit:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameExit = True
            if event.key == pygame.K_1:
                PlayerList1 = PlayerList1.tail
            if event.key == pygame.K_2:
                PlayerList2 = PlayerList2.tail
            if event.key == pygame.K_3:
                PlayerList3 = PlayerList3.tail
            if event.key == pygame.K_4:
                PlayerList4 = PlayerList4.tail
    if PlayerList1.Name == "Pos41":
        PlayerList1 = PlayerPosList1
    if PlayerList2.Name == "Pos11":
        PlayerList2 = PlayerPosList2
    if PlayerList3.Name == "Pos21":
        PlayerList3 = PlayerPosList3
    if PlayerList4.Name == "Pos31":
        PlayerList4 = PlayerPosList4
    gameDisplay.fill(white)
    CornerTile(0,0)
    Player1Glove(PlayerList1)
    Player2Glove(PlayerList2)
    Player3Glove(PlayerList3)
    Player4Glove(PlayerList4)
    pygame.display.flip()

pygame.quit()
quit()


