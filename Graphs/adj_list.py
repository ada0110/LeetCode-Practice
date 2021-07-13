
# unweighted graph using adj list
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    
    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)
        # print(self.graph)

    def printGraph(self):
        for node in self.graph:
            values = self.graph[node]
            print(node, "==>" , values)
            # for val in self.graph[node]:
                # print("val:", val)
            #     print(node, "==>", val)


    



g = Graph()

g.addEdge(1, 2)
g.addEdge(1,3)
g.addEdge(3, 4)
g.addEdge(4,2)


g.printGraph()
