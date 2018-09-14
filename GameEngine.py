"""
Methods for the Game Engine 
"""

import pygame

from Objects import *
from MazeIncludes import *
import Creating_Maze as cm
import Drawing_Maze as dm

class GameEngine: 

  def __init__(self): #Starts the game
  
    #Game start dialogue
    print("Welcome to the maze!")
    print("You start in the top-left corner and can move left, right, up or down.")
    print("Please choose how long and wide you want the maze to be.")
    self.l = cm.getDimension("length")
    self.w = cm.getDimension("width")

    #getting sprites for player and opponent
    playerSpriteDict = getSprites(0)
    
    if playerSpriteDict == catSpriteDict:
        opponentSpriteDict = dogSpriteDict
    else:
        opponentSpriteDict = catSpriteDict
    
    pygame.display.init
    self.gameDisplay = pygame.display.set_mode([s*l,s*w])
    pygame.display.set_caption("Maze")
    self.surface = pygame.display.get_surface()
    
    print("Loading...")
    
    #making maze
    self.gC = cm.graphComplete(l-1,w-1,s)
    self.maze = cm.makeTree(gC,l-1,w-1,s)
    
    #Drawing maze 
    self.posChar = v(s/2,s/2)
    self.posOpponent = v(s*l - s/2, s/2)
    dm.drawMaze(l,w,maze,gC,s,gameDisplay,surface)
    print("Loaded.\nYour aim is to reach the green square without getting caught by the enemy.\nGood Luck!")
    self.moveCount = 0
    self.player = char(playerSpriteDict,posChar)
    self.opponent = char(opponentSpriteDict, posOpponent)
    self.playerDirection = None
    self.opponentDirection = None
    self.opponentMoveCount = 1
    
    #drawing player
    gameDisplay.blit(player.spriteDict["down"],(posChar[0]-(s/2)+5,posChar[1]-(s/2)+5))
    pygame.display.update()
    self.playerSprite = player.spriteDict["down"]

    #drawing opponent
    gameDisplay.blit(opponent.spriteDict["down"],(posOpponent[0]-(s/2)+5,posOpponent[1]-(s/2)+5))
    pygame.display.update()
    self.opponentSprite = opponent.spriteDict["down"]
    
    def gameLoop(self): # The main game loop 
      
      opponentMoveCount = 0 #Used to control how often opponent moves
      
      while True:
    
        #moving player
        self.playerDirection = getDirection()
        if self.playerDirection != None:
            self.playerSprite = player.spriteDict[playerDirection]
        if moveTest(self.posChar,self.playerDirection,self.maze) == True:
            self.posChar = moveOnce(self.player,maze,self.playerDirection,dirDict)
            self.moveCount += 1
        blackAround(self.posChar,self.surface, s)

        #moving opponent
        if self.moveCount != 0:
            self.opponentDirection = getOpponentDirection(self.posChar, self.posOpponent, opponentMoveCount % 450)
            while moveTest(self.posOpponent, self.opponentDirection, self.maze) == False and self.opponentDirection != None:
                self.opponentDirection = getOpponentDirection(self.posChar, self.posOpponent, self.opponentMoveCount % 450)

            if self.opponentDirection != None:
                self.posOpponent = moveOnce(self.opponent, self.maze, self.opponentDirection, dirDict)

        else:
            self.opponentDirection = None

        blackAround(self.posOpponent, self.surface, s)
        opponentMoveCount += 1
        
        #the green square (at end)
        pygame.draw.rect(self.surface,(0,200,0,1),((s*(l-0.75),s*(w-0.75)),(s/2,s/2)),0)

        #the player
        gameDisplay.blit(self.playerSprite,(int(self.posChar[0]-(s/2)+5),int(self.posChar[1]-(s/2)+5)))

        #the opponent
        gameDisplay.blit(self.opponentSprite,(int(self.posOpponent[0]-(s/2)+5),int(self.posOpponent[1]-(s/2)+5)))
        pygame.display.flip()

        #collision with opponent
        if self.posChar == self.posOpponent:
            endGame(collisionText, self.moveCount)
            return

        #getting to the green square
        if self.posChar == v(s*(l-1)+(s/2),s*(w-1)+(s/2)):
            endGame(winText, self.moveCount)
            return
      
