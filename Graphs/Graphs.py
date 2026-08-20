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
        '''
        for example: 
        {
            "A": ["B", "C", "D", "E"],
            "B": ["A", "C"],
            "C": ["A", "B", "E"],
            "D": ["A", "E", "F"],
            "E": ["A", "C", "D", "F"],
            "F": ["D", "E"]
        }
        self.graph_dict[vertex] = self.graph_dict["A"] = ["B", "C", "D", "E"]
        for neighbor in ["B", "C", "D", "E"]
            self.graph_dict[neighbor] = self.graph_dict["B"] = ["A", "C"]
            ["A", "C"].remove("A") = ["C"]
        self.graph_dict.pop(vertex) = self.graph_dict.pop("A") = remove ("A": ["B", "C", "D", "E"]) from graph_dict
        return
        '''
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

    '''
    DFT RECURSIVE
    1. Check that starting_node exists.
    2. Create an empty explored set.
    3. Create an empty visited list.
    4. Define a recursive traversal function:
        traverse(current_node):
            Add current_node to explored set.
            Append current_node to visited list.
            FOR each neighbor of current_node:
                IF neighbor is not in explored:
                    Recursively traverse that neighbor.
    5. Start traversal from starting_node.
    6. Return visited.
    '''

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

    '''
    We can start the traversal from any node.
    BFT(starting_node) 

    1. Check that starting_node exists.
    2. Create an empty queue.
    3. Append starting_node into the queue.
    4. Create an empty explored list.
    5. Create an empty visited list.
    6. WHILE the queue is not empty:
        Popleft() the vertex(first/left most) from the queue.
        Append it to explored.
        Append it to visited.
        Look at all its neighbors.
        For every neighbor:
            Check if the neighbour is in explored list.
            If no:
                Mark it as explored.
                Add it to the queue.
    7. Return visited.
    '''