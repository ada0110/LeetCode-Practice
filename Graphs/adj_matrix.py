
class Graph:
    def __init__(self, numofNodes):
        self.numofNodes = numofNodes + 1
        self.graph = [[0 for x in range(numofNodes+1)] for y in range(numofNodes+1)]
        print(self.graph)

    # adj matrix implementation is restricted by the size of the matrix
    #  so we need to check whether the node value is within the size of the matrix
    def withInBounds(self, v1, v2):
        return ((v1>=0 and v1<= self.numofNodes) and (v2>=0 and v2<=self.numofNodes))

    def addEdges(self, v1, v2):
        if (self.withInBounds(v1, v2)):
            self.graph[v1][v2] = 1
            print(self.graph)

    def printGraph(self):
        for i in range(self.numofNodes):
            for j in range(len(self.graph[i])):
                if (self.graph[i][j]):
                    print(i, '-->', j)




g = Graph(4)

g.addEdges(1,2)
g.addEdges(1,4)
g.addEdges(2,3)
g.addEdges(3,4)


g.printGraph()


