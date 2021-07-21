from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self,u, v):
        self.graph[u].append(v)
        

    def bfs(self, startNode, debug= True):

        print(self.graph)
        # using list as queue 
        queue = []

        # using set for visited vertices
        visited = set()

        # append start node in the queue
        queue.append(startNode)

        # mark startNode as visited
        visited.add(startNode)

        while(len(queue)):  #while queue is not empty
            # print("---------------------------------------")
            # print("queue:", queue)
            
            # remove node from the queue but as list is implemented as queue
            # so pop first elem from list as queue is FIFO 
            u = queue.pop(0)
            print(u, end = " ")

            # start visiting all neighbors of popped node
            for v in self.graph[u]:
                if v not in visited:
                    # add that neighbor n in queue for further traversal
                    queue.append(v)
                    # mark that neighbor as visited
                    visited.add(v)
                    # print("visited:", visited)

        
        



s = Graph()

s.insertEdge(2,1)
s.insertEdge(2,5)
s.insertEdge(5,6)
s.insertEdge(5,8)
s.insertEdge(6,9)

s.bfs(2)

        

