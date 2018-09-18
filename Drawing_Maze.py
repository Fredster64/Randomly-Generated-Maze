"""
Drawing the Maze
"""

import pygame
import math
pi = math.pi

from Objects import *

#define a rotation of a vertex about a given centre - used for maze drawing
def rot(theta, vertex, centre):
    centeredv = vertex - centre
    rotatedv = v(centeredv[0]*math.cos(theta) - centeredv[1]*math.sin(theta), centeredv[0]*math.sin(theta) + centeredv[1]*math.cos(theta))
    finalv = rotatedv + centre
    return finalv

#drawing the maze itself
def drawMaze(graph, s, gameDisplay, surface):
  
    # length and width of maze
    l = graph.breadth
    w = graph.width

    rect = pygame.Rect((0,0), (s*l,s*w)) #outline of maze
    pygame.draw.rect(surface, (200, 200, 200, 1), rect, 5)

    # Get complement graph 
    complement = getComplement(graph)

#drawing the walls
#rotate each edge of the complement graph by pi/2
#this makes the absence of an edge in the maze-tree be drawn as a wall
    for i in range(graph.size): 
        for j in range(i):
            # reference i and reference j are connected just in case adjacencyMatrix[i][j] = 1
            if complement.adjacencyMatrix[i][j] == 1: 
                # Get vertex coords and add relevant edge 
                v1 = convertRefToCoords(graph, i, s)
                v2 = convertRefToCoords(graph, j, s)
                edgeToAdd = edge(v1, v2)
                # Rotate vertices about centre of edgeToAdd
                rotv1 = rot(pi/2, v1, centre(edge))
                rotv2 = rot(pi/2, v2, centre(edge))
                # Draw the edge onto the screen 
                pygame.draw.line(surface, (200, 200, 200, 1), (rotv1[0], rotv1[1]), (rotv2[0], rotv2[1]), 2 )

    #drawing the finish square
    pygame.draw.rect(surface,(0,200,0,1),((s*(l-0.75),s*(w-0.75)),(s/2,s/2)),0)
    pygame.display.flip()
    
    return
