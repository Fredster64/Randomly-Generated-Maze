"""
Global variables and non-member functions for the maze
"""

from Objects import * #Some global variables are objects
import pygame #Used in non-member functions
from random import randint #Used for getting opponent direction

### Global Variables ###

#Display size of each square 'unit' of the maze
sqSize = 30
s = int(sqSize)

#player images
catUpImg = pygame.image.load('Sprites/cat_up.png')
catDownImg = pygame.image.load('Sprites/cat_down.png')
catLeftImg = pygame.image.load('Sprites/cat_left.png')
catRightImg = pygame.image.load('Sprites/cat_right.png')
catSpriteDict = {"up":catUpImg, "down":catDownImg, "left":catLeftImg, "right":catRightImg}

#dog images
dogUpImg = pygame.image.load('Sprites/dog_up.png')
dogDownImg = pygame.image.load('Sprites/dog_down.png')
dogLeftImg = pygame.image.load('Sprites/dog_left.png')
dogRightImg = pygame.image.load('Sprites/dog_right.png')
dogSpriteDict = {"up":dogUpImg, "down":dogDownImg, "left":dogLeftImg, "right":dogRightImg}

#texts for end game
collisionText = "Oh no! You were caught by the enemy.\nYou lasted {0} moves."
winText = "Well done! You have completed the maze.\nYou completed it in {0} moves."

#Directions you can move in
dirList = ["left","right","up","down"]
dirDict = {"left":v(-s,0),"right":v(s,0),"up":v(0,-s),"down":v(0,s)}

###--------------------------------------------###

### Non-member functions ###

#register key input
def getDirection():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               return "down"
            elif event.key == pygame.K_UP:
                return "up"
            elif event.key == pygame.K_LEFT:
                return "left"
            elif event.key == pygame.K_RIGHT:
                return "right"

            else:
                return None

#move opponent towards player
def getOpponentDirection(posChar, posOpponent, moveVal):
    if moveVal != 0:
        return None
    else:
        likelyDirections = []
        if posChar[0] < posOpponent[0]:
            likelyDirections.append("left")
        elif posChar[0] > posOpponent[0]:
            likelyDirections.append("right")

        if posChar[1] < posOpponent[1]:
            likelyDirections.append("up")
        elif posChar[1] > posOpponent[1]:
            likelyDirections.append("down")

        weightList = [1, 1, 1, 1] #chances for [left, right, up, down]
        for i in range(4):
            if dirList[i] in likelyDirections:
                weightList[i] *= 3

        possibleDirections = []
        for i in range(4):
            for k in range(weightList[i]):
                possibleDirections.append(dirList[i])

        return possibleDirections[randint(0, len(possibleDirections) - 1)]
    

#see if you can move to a given place, from a given place, on a given graph
def moveTest(vertex,direction,graph):
    try:
        endVertex = vertex + dirDict[direction]
    except:
        return False
    for edg in graph:
        if edge(vertex,endVertex) == edg or edge(endVertex,vertex) == edg:
            return True
        
    return False

#getting the sprites for the player's character
def getSprites(count):
    if count == 0:
        print("Would you like to play as a cat or a dog?")
    else:
        print("Please type 'cat' or 'dog'.")
        
    answer = input()
    
    if answer == "cat":
        spriteDict = catSpriteDict
    elif answer == "dog":
        spriteDict = dogSpriteDict
    else:
        spriteDict = getSprites(1)

    return spriteDict

#ending the game
def endGame(text, moveCount):
    print(text.format(moveCount))
    pygame.time.delay(1000)
    pygame.display.quit()
