'''
Objects used in the maze
'''

import pygame

#create a vertex object
class v:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.weight = 0 #used in Dijkstra's algorithm
        # Store the vertex reference coordinates
        # i.e. vertex points to maze square in ith row and jth column
        self.i = (x - s/2) / s
        self.j = (y - s/2) / s
        
        
    def __getitem__(self,index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError
        
    def __add__(self, other):
        return v(self[0]+other[0],self[1]+other[1])

    def __sub__(self, other):
        return v(self[0]-other[0],self[1]-other[1])
    
    def __eq__(self, other):
        if all(self[i] == other[i] for i in range(2)): 
            return True
        else:
            return False

    def __lt__(self, other):
        if self[0] < other[0] and self[1] < other[1]:
            return True
        else:
            return False
        
    def __gt__(self, other):
        if self[0] > other[0] and self[1] > other[1]:
            return True
        else:
            return False
        
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

#gives rectangles around a given rectangle
def rectAroundList(self, s):
    tlVertex = self+v(5-(s/2),5-(s/2))
    rectList = [((int(tlVertex[0]),int(tlVertex[1])),(int(s-8),int(s-8)))]
    for i in {-1,1}:
        tlVertexNew1 = tlVertex+v(s*i,0)
        tlVertexNew2 = tlVertex+v(0,s*i)

        rectList.append(((int(tlVertexNew1[0]),int(tlVertexNew1[1])),(int(s-8),int(s-8))))
        rectList.append(((int(tlVertexNew2[0]),int(tlVertexNew2[1])),(int(s-8),int(s-8))))

    return rectList

#draws black around the position
def blackAround(self, surface, s):
    for rect in rectAroundList(self, s):
        pygame.draw.rect(surface,(0,0,0,1),rect)
        
def setWeight(self, value):
    self.weight = value

#------------------------------------------------------------#
        
#create a character object
class char:
    def __init__(self,spriteDict,pos):
        self.spriteDict = spriteDict
        self.pos = pos
        self.currentSprite = spriteDict["down"]
        self.currentDirection = None

def changePos(self, posNew):
    self.pos = posNew
    return self.pos

def changeSprite(self): 
    self.currentSprite = self.spriteDict[self.currentDirection]
    return

#Returns new location, and sets new sprite
def moveOnce(self, dirDict):
    changePos(self, self.pos+dirDict[self.currentDirection])
    return

def drawChar(self, gameDisplay, s): 
    gameDisplay.blit(self.currentSprite, (int(self.pos[0]-(s/2)+5), int(self.pos[1]-(s/2)+5)))
    return

#------------------------------------------------------------#

#create an edge object
class edge:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
        
    def __getitem__(self,index):
        if index == 0:
            return self.v1
        elif index == 1:
            return self.v2
        else:
            raise IndexError

    def __eq__(self, other):
        if vertexEq(self, other):
            return True
        else:
            return False        
    def __str__(self):
        return "("+str(self[0])+","+str(self[1])+")"

def centre(self):
    return v(0.5*(self.v1[0]+self.v2[0]),0.5*(self.v1[1]+self.v2[1]))
   
def vertexEq(self,other):
    if all(self[i] == other[i] for i in range(2)):
        return True
    else:
        return False
    
###-------------------------------------------------###
# Create an undirected graph object 
# Undirection makes it easier to keep track of edges 
class undirectedGraph: 
    
    def __init__(self, breath, height): 
        # We input breadth and height of the square grid 
        self.breadth = breadth
        self.height = height
        self.size = self.breadth*self.height
        # Note: for an n*m grid, we need (n+1)(m+1) vertices
        self.adjacencyMatrix = [][]
        for i in range( self.size ):
            for j in range( self.size ): 
                adjacencyMatrix[i][j] = 0 # adjacencyMatrix is a size*size matrix of zeroes 
                
        self.vertexWeights = [] # ith entry is weight of vertex with grid reference i
        for i in range(self.size): 
            self.vertexWeights[i] = 0
                
        return
                
# add an edge to the graph
def addEdge(self, edge):
    # vertex reference data will be of integer form
    # for an n*m grid of squares, the vertices will be indexed:
    """
    1   | n+1   | 2n+1  | 3n+1  | ... | (m-1)n + 1
    2   | n+2   | 2n+2  | .........   | (m-1)n + 2
           ...................
    n   | 2n    | .............       | mn
    """
    
    vertex1 = edge.v1
    vertex2 = edge.v2
    
    # Get vertex references from vertex{k}.i and vertex{k}.j
    vertex1Ref = (vertex1.j - 1)*self.height + vertex1.i
    vertex2Ref = (vertex2.j - 1)*self.height + vertex2.i
    
    # Appropriately change self.adjacencyMatrix
    self.adjacencyMatrix[vertex1Ref][vertex2Ref] = 1
    self.adjacencyMatrix[vertex2Ref][vertex1Ref] = 1
    
    return

# convert between vertex position in adjacency matrix and on-screen coordinates
# 's' will be a global variable (see MazeIncludes.py)
def convertRefToCoords(self, vertexRef, s): 
    # Get 'i' and 'j' from ref 
    # Note: i and j start counting at 1, NOT 0
    i = vertexRef % self.height  #row number
    if i == 0: 
        i = n
        
    j = ( (vertexRef - i) / self.breadth ) + 1  #column number
    
    # Get coordinates on-screen from i and j
    # +s/2 is needed to land us in the middle of a square
    x = s*i + s/2
    y = s*j + s/2
    
    return [x, y]

# returns the complement of a graph
def getComplement(self): 
    complement = undirectedGraph(self.breadth, self.height)
    for i in range(self.size):
        for j in range(self.size): 
            complement.adjacencyMatrix[i][j] = 1 - self.adjacencyMatrix[i][j]
            
    return complement
            
###-----------------------------------------------------------------###
 
