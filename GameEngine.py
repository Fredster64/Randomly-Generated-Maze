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
    self.gameDisplay = pygame.display.set_mode([s*self.l, s*self.w])
    pygame.display.set_caption("Maze")
    self.surface = pygame.display.get_surface()
    
    print("Loading...")
    
    #making maze
    self.maze = cm.makeTree(self.l, self.w, s)
    
    #Drawing maze 
    posChar = v(s/2, s/2, s) # top-left of screen
    posOpponent = v(s*self.l - s/2, s/2, s) # top-right of screen
    dm.drawMaze(self.maze, s, self.gameDisplay, self.surface)
    print("Loaded.\nYour aim is to reach the green square without getting caught by the enemy.\nGood Luck!")
    self.player = char(playerSpriteDict, posChar)
    self.opponent = char(opponentSpriteDict, posOpponent)
    
    #drawing player
    drawChar(self.player, self.gameDisplay, s)
    pygame.display.update()

    #drawing opponent
    drawChar(self.opponent, self.gameDisplay, s)
    pygame.display.update()
    
###-----------------------------------###

  #check whether the game has ended
  #also ends the game if it has
def endCheck(self, moveCount): 

  #collision with opponent
    if self.player.pos == self.opponent.pos:
        endGame(collisionText, moveCount)
        return True

    #getting to the green square
    if self.player.pos == v(s*(self.l) - (s/2), s*(self.w) - (s/2), s):
        endGame(winText, moveCount)
        return True

    return False
    
###-----------------------------------###
    
def gameLoop(self): # The main game loop 

  opponentMoveCount = 1 #Used to control how often opponent moves
  moveCount = 0 #How many moves the player has made

  while True:

    #moving player
    self.player.currentDirection = getDirection()
    if self.player.currentDirection != None:
        changeSprite(self.player) #Changes sprite regardless of whether move is valid 
    if moveTest(self.player.pos, self.player.currentDirection, self.maze):
        moveOnce(self.player, dirDict)
        moveCount += 1
    blackAround(self.player.pos, self.surface)

    #moving opponent
    if moveCount != 0:
        self.opponent.currentDirection = getOpponentDirection(self.player.pos, self.opponent.pos, self.maze, opponentMoveCount )
        # Check for validity
        if moveTest(self.opponent.pos, self.opponent.currentDirection, self.maze):
            changeSprite(self.opponent)
            moveOnce(self.opponent, dirDict)

    # Opponent can't move before player starts 
    else:
        self.opponent.currentDirection = None

    blackAround(self.opponent.pos, self.surface)
    opponentMoveCount += 1
    # Loop to 0 if exceeds 500
    # Means that the opponent will move every 500 loops
    opponentMoveCount %= 1000

    #drawing the green target square
    pygame.draw.rect(self.surface, (0,200,0,1), ((s*(self.l-0.75), s*(self.w-0.75)), (s/2,s/2)), 0)

    #the player
    drawChar(self.player, self.gameDisplay, s)

    #the opponent
    drawChar(self.opponent, self.gameDisplay, s)

    pygame.display.flip() #update display

    if endCheck(self, moveCount): 
      return

