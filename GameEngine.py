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
    posChar = v(s/2,s/2)
    posOpponent = v(s*l - s/2, s/2)
    dm.drawMaze(l,w,maze,gC,s,gameDisplay,surface)
    print("Loaded.\nYour aim is to reach the green square without getting caught by the enemy.\nGood Luck!")
    self.player = char(playerSpriteDict, posChar)
    self.opponent = char(opponentSpriteDict, posOpponent)
    
    #drawing player
    self.gameDisplay.blit(player.currentSprite,(self.player.pos[0]-(s/2)+5,self.player.pos[1]-(s/2)+5))
    pygame.display.update()

    #drawing opponent
    self.gameDisplay.blit(opponent.currentSprite,(self.opponent.pos[0]-(s/2)+5,self.opponent.pos[1]-(s/2)+5))
    pygame.display.update()
    
###-----------------------------------###

  #check whether the game has ended
  #also ends the game if it has
  def endCheck(self, moveCount): 
    
    #collision with opponent
      if self.player.pos == self.opponent.pos:
          endGame(collisionText, moveCount)

      #getting to the green square
      if self.player.pos == v(s*(l-1)+(s/2),s*(w-1)+(s/2)):
          endGame(winText, moveCount)
          
      return
    
###-----------------------------------###
    
  def gameLoop(self): # The main game loop 

    opponentMoveCount = 1 #Used to control how often opponent moves
    moveCount = 0 #How many moves the player has made

    while True:

      #moving player
      self.player.currentDirection = getDirection()
      if self.player.currentDirection != None:
          changeSprite(self.player) #Changes sprite regardless of whether move is valid 
      if moveTest(self.posChar,self.playerDirection,self.maze):
          moveOnce(self.player, maze)
          moveCount += 1
      blackAround(self.player.pos, self.surface, s)

      #moving opponent
      if moveCount != 0:
          self.opponent.currentDirection = getOpponentDirection(self.player.pos, self.opponent.pos, opponentMoveCount % 450)
          while (not moveTest(self.opponent.pos, self.opponent.currentDirection, self.maze) ) and ( self.opponent.currentDirection != None):
              self.opponent.pos = getOpponentDirection(self.player.pos, self.opponent.pos, opponentMoveCount % 450)

          if self.opponent.currentDirection != None:
              moveOnce(self.opponent, self.maze)

      else:
          self.opponent.currentDirection = None

      blackAround(self.opponent.pos, self.surface, s)
      opponentMoveCount += 1

      #drawing the green target square
      pygame.draw.rect(self.surface,(0,200,0,1),((s*(l-0.75),s*(w-0.75)),(s/2,s/2)),0)

      #the player
      drawChar(self.player, self.gameDisplay, s)

      #the opponent
      drawChar(self.player, self.gameDisplay, s)
      
      pygame.display.flip() #update display
      
      endCheck(self, moveCount)

