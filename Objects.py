'''
Objects used in the maze
'''

import pygame

#create a vertex object
class v:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.weight = 0 #Used for path-finding
        
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

def changePos(self,posNew):
    self.pos = posNew
    return self.pos

def changeSprite(self): 
    self.currentSprite = self.spriteDict[self.currentDirection]
    return

#Returns new location, and sets new sprite
def moveOnce(self, maze, dirDict):
    changePos(self,self.pos+dirDict[self.currentDirection])
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
 
