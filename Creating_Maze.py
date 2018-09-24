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
    start = v(s/2,s/2,s)
    verticesOnTree = [start]
    #Use Prim's Algorithm 
    for _ in range( (l*w) - 1 ): # Number of repetitions of algorithm we need
        
        # Getting candidate edges to add
        candidates = []
        for v1 in verticesOnTree:
            # Test if adjacent vertices are in verticesOnTree
            for v2 in [v1 + v(s,0,s), v1 - v(s,0,s), v1 + v(0,s,s), v1 - v(0,s,s)]:
                # Test if v2 is on screen
                if (v2 not in verticesOnTree) and ( min(v2.x, v2.y) > 0 ) and (v2.x < l*s) and (v2.y < w*s):
                    if edge(v1, v2) not in candidates: # Don't add edges more than once
                        candidates.append( edge(v1, v2) )
               
        # Adding a random edge if we can
        if candidates != []:
            nextEdge = candidates[randint(0, len(candidates)-1)]
            for i in range(2):
                if nextEdge[i] not in verticesOnTree:
                    verticesOnTree.append(nextEdge[i])
                    
            addEdge(tree, nextEdge)
  
    return tree
 
