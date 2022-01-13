class Graph:
    def __init__(self): 
        self.adj_list = {}
    
    def add_vertex(self, vertex): 
        if self not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True 
        return False 

    def remove_vertex(self, vertex): 
        if vertex in self.adj_list.keys(): 
            for other_vertex in self.adj_list[vertex]: 
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True 
        return False 
    
    def add_edge(self, v1, v2): 
        adj_list_keys = self.adj_list.keys()
        if v1 in adj_list_keys and v2 in adj_list_keys:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2): 
        adj_list_keys = self.adj_list.keys()
        if v1 in adj_list_keys and v2 in adj_list_keys:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            #Remove a edge from vertex but no edges
            except ValueError: 
                pass
            return True
        return False

    def print_graph(self): 
        for vertex in self.adj_list: 
            print(vertex, ":", self.adj_list[vertex])
        return 
    
my_g = Graph()
my_g.add_vertex("A")
my_g.add_vertex("B")
my_g.add_vertex("C")
my_g.add_vertex("D")
my_g.add_edge("A", "C")
my_g.add_edge("A", "B")
my_g.add_edge("A", "D")
my_g.add_edge("B", "D")
my_g.add_edge("C", "D")
my_g.print_graph()
print("----")
my_g.remove_vertex("D")
my_g.print_graph()