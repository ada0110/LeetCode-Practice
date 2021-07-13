
class Graph:
    def __init__(self, numofNodes):
        self.numofNodes = numofNodes + 1
        self.graph = [[0 for x in range(numofNodes+1)] for y in range(numofNodes+1)]


    def addEdges(self, v1, v2):
        self.graph[v1][v2] = 1
    
# adj matrix implementation is restricted by the size of the matrix
#  so we need to check whether the node value is within the size of the matrix
    def withInBounds(self, v1, v2):
        return (v1>=0 and v1<= self.numofNodes)   

    def printGraph(self):
        