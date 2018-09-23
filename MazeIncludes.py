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

#cat images
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
dirList = ["left", "right", "up", "down"]
dirDict = {"left":v(-s,0,s), "right":v(s,0,s), "up":v(0,-s,s), "down":v(0,s,s)}

###--------------------------------------------###

### Non-member functions ###

### --- Dijkstra's algorithm --- ###

def checkVertex( vertexToCheck, graph, checkedVertices, pathtracer, posTo ):
    
    # Check if we're at posTo
    if vertexToCheck == posTo:
        checkedVertices.append(vertexToCheck)
        return
    
    toCheckRef = getRef(vertexToCheck, graph.height)
    
    # ref counting starts at 1, and list indexing starts at 0, so we need the '-1's
    for tempRef in range(1, graph.size + 1): 
        
        # See if vertex is adjacent to vertexToCheck
        if (graph.adjacencyMatrix[tempRef-1][toCheckRef-1] == 1):
            # and if we've found a new minimal path to vertex - second condition allows us to add new vertices
            if (graph.vertexWeights[toCheckRef-1] + 1  <= graph.vertexWeights[tempRef-1]) or (graph.vertexWeights[tempRef-1] == 0): 
                # Update graph.vertexWeights 
                graph.vertexWeights[tempRef-1] = graph.vertexWeights[toCheckRef-1] + 1
                # Update pathfinder 
                [x, y] = convertRefToCoords(graph, tempRef, s)
                insert(pathtracer, v(x, y, s), vertexToCheck)
                
    checkedVertices.append(vertexToCheck)
    

def getNextMove( posFrom, posTo, graph ):
   
    checkedVertices = [] 
    candidates = []
    pathtracer = pathfinder(posFrom) # Will store pairs of vertices, [vertex, vertex from which the shortest path goes to vertex]
    # e.g. if a -> b in the shortest path, then pathfinder will include b:a
    
    # Special case: posFrom = posTo
    if posFrom == posTo: 
        return None
    
    # Initial condition: check the start vertex 
    checkVertex(posFrom, graph, checkedVertices, pathtracer, posTo)
    
    # Now, pathfinder is updated with vertices adjacent to start
    # and checkedVertices contains start
    # and graph's weights have been updated 
    while checkedVertices[-1] != posTo: 
        # Get candidates for next check, and choose the minimal one 
        candidates = [] # Stores candidateVertices
        x = 0
        y = 0
        vertex = v(x, y, s)
        for vertexRef in range(1, graph.size + 1): 
            [x, y] = convertRefToCoords(graph, vertexRef, s)
            vertex = v(x, y, s)
            # Check if unchecked and connected to a checked vertex 
            if ( vertex not in checkedVertices ) and ( graph.vertexWeights[vertexRef-1] > 0 ):
                vertex.weight = graph.vertexWeights[vertexRef-1]
                candidates.append( vertex )
                
        # Choosing minimal candidate 
        # Use an insertion sort 
        for i in range( len(candidates) ): 
            for j in range(i): 
                indexToCheck = i - j - 1
                if candidates[i].weight < candidates[indexToCheck].weight: 
                    candidates[i], candidates[indexToCheck] = candidates[indexToCheck], candidates[i]
                else: 
                    break
        
        # We're passing candidates so that we don't check unnecessary vertices
        checkVertex( candidates[0], graph, checkedVertices, pathtracer, posTo ) 
    
    # Last element in checkedVertices is now posTo
    returnElement = posTo
    while search(pathtracer, returnElement) != posFrom: 
        returnElement = search(pathtracer, returnElement)
        
    # Now, we've got the element after poFrom in the shortest path to posTo
    return returnElement

### --- end of Dijkstra's algorithm --- ###

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

# Move opponent towards player
def getOpponentDirection(posChar, posOpponent, graph, moveVal):
    # Need moveVal = 0 for move to take place
    if moveVal != 0: 
        return None 
    else: 
        nextMovePos = getNextMove(posOpponent, posChar, graph)
        if nextMovePos[0] > posOpponent[0]: 
            return "right"
        elif nextMovePos[0] < posOpponent[0]: 
            return "left"
        elif nextMovePos[1] > posOpponent[1]: 
            return "up"
        elif nextMovePos[1] < posOpponent[1]: 
            return "down"
        else: 
            return None
    
#see if you can move to a given place, from a given place, on a given graph
def moveTest(vertex, direction, graph):
    try:
        endVertex = vertex + dirDict[direction]
    except: # direction = None
        return False
    
    vertexRef = getRef(vertex, graph.height)
    endVertexRef = getRef(endVertex, graph.height)
    
    return graph.adjacencyMatrix[vertexRef][endVertexRef] == 1
    

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
