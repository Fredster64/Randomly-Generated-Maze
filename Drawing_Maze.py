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
    rotatedv = v(centeredv[0]*math.cos(theta) - centeredv[1]*math.sin(theta), centeredv[0]*math.sin(theta) + centeredv[1]*math.cos(theta), centeredv.s)
    finalv = rotatedv + centre
    return finalv

#drawing the maze itself
def drawMaze(graph, s, gameDisplay, surface):
  
    # length and width of maze
    l = graph.breadth
    w = graph.height

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
            if ( complement.adjacencyMatrix[i][j] == 1 ) and ( i != j ): 
                # Get vertex coords and add relevant edge 
                [v1_x, v1_y] = convertRefToCoords(graph, i+1, s)
                [v2_x, v2_y] = convertRefToCoords(graph, j+1, s)
                v1 = v(v1_x, v2_x, s)
                v2 = v(v2_x, v2_y, s)
                edgeToAdd = edge(v1, v2)
                # Rotate vertices about centre of edgeToAdd
                rotv1 = rot(pi/2, v1, centre(edgeToAdd))
                rotv2 = rot(pi/2, v2, centre(edgeToAdd))
                # Draw the edge onto the screen 
                pygame.draw.line(surface, (200, 200, 200, 1), (rotv1[0], rotv1[1]), (rotv2[0], rotv2[1]), 2 )

    #drawing the finish square
    pygame.draw.rect(surface,(0,200,0,1),((s*(l-0.75),s*(w-0.75)),(s/2,s/2)),0)
    pygame.display.flip()
    
    return
