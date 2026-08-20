from collections import deque

class Graph:
    def __init__(self):
        self.graph_dict = {} # empty dictionary

    def add_vertex(self, vertex):
        if vertex in self.graph_dict:
            raise Exception("Vertex already in graph")
        self.graph_dict[vertex] = [] # insert vertex as key and the value be empty list. for example: graph_dict = { "A": [] }
        return self

    def add_edge(self, vertex1, vertex2): # suppose, vertex1 = A, vertex2 = B
        if vertex1 not in self.graph_dict or vertex2 not in self.graph_dict:
            raise Exception("Invalid vertices")
        self.graph_dict[vertex1].append(vertex2) # ADD vertex2 to vertex1's connection list { "A": ["B"] }
        self.graph_dict[vertex2].append(vertex1) # ADD vertex1 to vertex2's connection list { "B": ["A"] }
        return self

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph_dict or vertex2 not in self.graph_dict:
            raise Exception("Invalid vertices")
        self.graph_dict[vertex1].remove(vertex2) # REMOVE vertex2 from vertex1's connection list
        self.graph_dict[vertex2].remove(vertex1) # REMOVE vertex1 from vertex2's connection list
        return self

    def remove_vertex(self, vertex): # Suppose vertex = A
        if vertex not in self.graph_dict:
            raise Exception("Vertex not in graph")
        for neighbor in self.graph_dict[vertex]:
            self.graph_dict[neighbor].remove(vertex)
        self.graph_dict.pop(vertex)
        return self

    def dft_recursive(self, starting_node):
        if starting_node not in self.graph_dict:
            raise Exception("Vertex not in graph")
        explored = set()
        visited = []

        def traverse(current_node):    
            explored.add(current_node)
            visited.append(current_node)
            for member in self.graph_dict[current_node]:
                if member not in explored:
                    traverse(member)

        traverse(starting_node)
        return visited

    def dft_iterative(self, starting_node): # We can start the traversal from any node.
        if starting_node not in self.graph_dict:
            raise Exception("Vertex not in graph")
        stack = [starting_node]
        explored = set()
        visited = []
        while stack:
            current_node = stack.pop()
            explored.add(current_node)
            visited.append(current_node) 
            for member in self.graph_dict[current_node]:
                if member not in explored: 
                    explored.add(member) 
                    stack.append(member)  
        return visited

    # dft and bft is similar, just the stack() vs queue makes it different.
    def bft(self, starting_node): # We can start the traversal from any node.
        if starting_node not in self.graph_dict:
            raise Exception("Vertex not in graph.")
        queue = deque()
        queue.append(starting_node)
        explored = set()
        visited = []
        while queue:
            current_node = queue.popleft()
            explored.add(current_node) 
            visited.append(current_node) 
            for member in self.graph_dict[current_node]:
                if member not in explored: 
                    explored.add(member)
                    queue.append(member) 
        return visited




    