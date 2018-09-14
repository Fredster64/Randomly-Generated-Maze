"""
Making a randomly-generated Maze
"""
"""
Needs to be tidied up!
"""

import Drawing_Maze as dm
import Creating_Maze as cm
from Objects import *
from MazeIncludes import *

from random import randint
import pygame
import math

#The game loop
def gameLoop():
    
    #setting up
    print("Welcome to the maze!")
    print("You start in the top-left corner and can move left, right, up or down.")
    print("Please choose how long and wide you want the maze to be.")
    l = cm.getDimension("length")
    w = cm.getDimension("width")

    #getting sprites for player and opponent
    playerSpriteDict = getSprites(0)
    
    if playerSpriteDict == catSpriteDict:
        opponentSpriteDict = dogSpriteDict
    else:
        opponentSpriteDict = catSpriteDict
    
    pygame.display.init
    gameDisplay = pygame.display.set_mode([s*l,s*w])
    pygame.display.set_caption("Maze")
    surface = pygame.display.get_surface()
    
    print("Loading...")
    
    #making maze
    gC = cm.graphComplete(l-1,w-1,s)
    maze = cm.makeTree(gC,l-1,w-1,s)
    
    #drawing maze
    posChar = v(s/2,s/2)
    posOpponent = v(s*l - s/2, s/2)
    dm.drawMaze(l,w,maze,gC,s,gameDisplay,surface)
    print("Loaded.\nYour aim is to reach the green square without getting caught by the enemy.\nGood Luck!")
    moveCount = 0
    player = char(playerSpriteDict,posChar)
    opponent = char(opponentSpriteDict, posOpponent)
    playerDirection = None
    opponentDirection = None
    opponentMoveCount = 1
    
    #drawing player
    gameDisplay.blit(player.spriteDict["down"],(posChar[0]-(s/2)+5,posChar[1]-(s/2)+5))
    pygame.display.update()
    playerSprite = player.spriteDict["down"]

    #drawing opponent
    gameDisplay.blit(opponent.spriteDict["down"],(posOpponent[0]-(s/2)+5,posOpponent[1]-(s/2)+5))
    pygame.display.update()
    opponentSprite = opponent.spriteDict["down"]
    
    #moving around
    while True:

        #moving player
        playerDirection = getDirection()
        if playerDirection != None:
            playerSprite = player.spriteDict[playerDirection]
        if moveTest(posChar,playerDirection,maze) == True:
            posChar = moveOnce(player,maze,playerDirection,dirDict)
            moveCount += 1
        blackAround(posChar,surface, s)

        #moving opponent
        if moveCount != 0:
            opponentDirection = getOpponentDirection(posChar, posOpponent, opponentMoveCount % 450)
            while moveTest(posOpponent, opponentDirection, maze) == False and opponentDirection != None:
                opponentDirection = getOpponentDirection(posChar, posOpponent, opponentMoveCount % 450)

            if opponentDirection != None:
                posOpponent = moveOnce(opponent, maze, opponentDirection, dirDict)

        else:
            opponentDirection = None

        blackAround(posOpponent, surface, s)
        opponentMoveCount += 1
        
        #the green square (at end)
        pygame.draw.rect(surface,(0,200,0,1),((s*(l-0.75),s*(w-0.75)),(s/2,s/2)),0)

        #the player
        gameDisplay.blit(playerSprite,(int(posChar[0]-(s/2)+5),int(posChar[1]-(s/2)+5)))

        #the opponent
        gameDisplay.blit(opponentSprite,(int(posOpponent[0]-(s/2)+5),int(posOpponent[1]-(s/2)+5)))
        pygame.display.flip()

        #collision with opponent
        if posChar == posOpponent:
            endGame(collisionText, moveCount)
            break

        #getting to the green square
        if posChar == v(s*(l-1)+(s/2),s*(w-1)+(s/2)):
            endGame(winText, moveCount)
            break

if __name__ == "__main__":
    gameLoop()




