"""
Drawing the Maze
"""

import pygame
import math
pi = math.pi

from Objects import *

#making a complement graph with respect to a complete graph - used for drawing the maze
def graphComplement(graph, completeGraph):
    complement = []
    for edge in completeGraph:
        if edge not in graph:
            complement.append(edge)
    return complement

#define a rotation of a vertex about a given centre - used for maze drawing
def rot(theta,vertex,centre):
    centeredv = vertex - centre
    rotatedv = v(centeredv[0]*math.cos(theta) - centeredv[1]*math.sin(theta), centeredv[0]*math.sin(theta) + centeredv[1]*math.cos(theta))
    finalv = rotatedv + centre
    return finalv

#drawing the maze itself
def drawMaze(l,w,graph,graphComplete,s,gameDisplay,surface):
  
    rect = pygame.Rect((0,0),(s*l,s*w)) #outline of maze
    pygame.draw.rect(surface,(200,200,200,1),rect,5)

    complement = graphComplement(graph, graphComplete)

#drawing the walls
#rotate each edge of the complement graph by pi/2
#this makes the absence of an edge in the maze-tree be drawn as a wall
    for edge in complement:
        rotv1 = rot(pi/2,edge[0],centre(edge))
        rotv2 = rot(pi/2,edge[1],centre(edge))
        if (edge[0][0] == edge[1][0]) or (edge[0][1] == edge[1][1]):
            pygame.draw.line(surface,(200,200,200,1),(rotv1[0],rotv1[1]),(rotv2[0],rotv2[1]),2)

#drawing the finish square
    pygame.draw.rect(surface,(0,200,0,1),((s*(l-0.75),s*(w-0.75)),(s/2,s/2)),0)
    pygame.display.flip()
 
        

 
