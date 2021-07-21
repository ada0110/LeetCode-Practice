from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)
        

    def DFS(self, startNode, debug = False):
        print(self.graph)
        # using  list as stack
        st = []
        visited = set()
        st.append(startNode)
        if debug: print("st before while loop:", st)

        while(len(st)): 
            cur_elem = st[-1]
            # print("curr_elem:", cur_elem)
        
            if debug: print("st before pop:", st)

            # pop a vertex from st and visit its neighbors
            st.pop()
            if debug: print("st after pop :", st)

            if(cur_elem not in visited):
                if debug: print("curr_elem:", cur_elem, end ="\n")
                print(cur_elem, end = " ")
                visited.add(cur_elem)
                if debug: print("visited:", visited)
                if debug: print("---------------------------------")

            # push unvisited neighbors of a node in stack
            for vertex in self.graph[cur_elem]:
                if vertex not in visited:
                    st.append(vertex)
            if debug: print("st after adding neighbors of visited node:", st)

        
    # def printGraph(self):
    #     for node in self.graph:
    #         value = self.graph[node]
    #         print(node, "==>",  value)



s = Graph()
s.insertEdge(2,1)
s.insertEdge(2,5)
s.insertEdge(5,6)
s.insertEdge(5,8)
s.insertEdge(6,9)

s.DFS(2)
# s.printGraph()
