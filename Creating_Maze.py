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


#make a function that returns a  random minimum spanning tree of an l*w lattice
def makeTree(l, w, s):
    
    tree = undirectedGraph(l, w) # breadth is l, height is w
    start = v(s/2,s/2)
    verticesOnTree = [start]
    #Use Prim's Algorithm 
    for _ in range( (l*w) - 1 ): # Number of repetitions of algorithm we need
        
        # Getting candidate edges to add
        candidates = []
        for edg in graph:
            if bool(edg[0] in verticesOnTree) != bool(edg[1] in verticesOnTree):
                candidates.append(edg)
               
        # Adding a random edge if we can
        if candidates != []:
            nextEdge = candidates[randint(0, len(candidates)-1)]
            for i in range(2):
                if nextEdge[i] not in verticesOnTree:
                    verticesOnTree.append(nextEdge[i])
                    
            addEdge(tree, nextEdge)
  
    return tree
 
