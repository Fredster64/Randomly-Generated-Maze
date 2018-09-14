"""
Creating the Maze-Tree
"""

from random import randint
from Objects import *

#used to get length and width of maze
def getDimension(dimension):
    while True:
        try:
            dimRaw = float(input("What {0}? ".format(dimension)))
            dim = int(dimRaw)
            if dim > 1 and dim == dimRaw:
                return dim
            elif dim != dimRaw:
                print("Needs to be an integer!")
            else:
                print("Too small - needs to be at least 2.")
        except:
            print("Invalid input! Give a number:")
            print(" 2-4 for an easy maze;")
            print(" 5-8, or even higher, for a harder maze.")

#drawing graph of all possible paths in maze
def graphComplete(l,w,s):
    graphC = []
    for x in range(l):
        for y in range(w+1):
            graphC.append(edge(v(s*x+(s/2),s*y+(s/2)),v(s*(x+1)+(s/2),s*y+(s/2))))
    for x in range(l+1):
        for y in range(w):
            graphC.append(edge(v(s*x+(s/2),s*y+(s/2)),v(s*x+(s/2),s*(y+1)+(s/2))))
    return graphC

#make a function that returns a  random minimum spanning tree of a graph
def makeTree(graph,l,w,s):
    tree = []
    start = v(s/2,s/2)
    verticesOnTree = [start]
    #Use Prim's Algorithm 
    for _ in range(((l+1)*(w+1))-1):
        candidates = []
        for edg in graph:
            if bool(edg[0] in verticesOnTree) != bool(edg[1] in verticesOnTree):
                candidates.append(edg)
        if candidates != []:
            nextEdge = candidates[randint(0,len(candidates)-1)]
            for i in range(2):
                if nextEdge[i] not in verticesOnTree:
                    verticesOnTree.append(nextEdge[i])
            tree.append(nextEdge)
        else:
            None
  
    return tree
 
