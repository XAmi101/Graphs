"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if the vertices exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        # Put the starting point in that
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack and push(add) starting vertex
        ss = Stack()
        # Put the starting point in that
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While stack is not empty
        while ss.size() > 0:
            # pop the first index
            path = ss.pop()
            last_vertex = path[-1]
            # if not in visited
            if path[-1] not in visited:
                # DO THE THING!! (search stop when you find something)
                print(last_vertex)
                # mark as visited
                visited.add(last_vertex)
                # For each edge in the item
                for next_vert in self.get_neighbors(last_vertex):
                    #Make a copy the path
                    new_path = list(path)
                    # append/add all neighbors
                    new_path.append(next_vert)
                    # Add that edge to the queue/stack
                    ss.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node has been visited
        # If not...
        # Mark it as visited
        # Call dft_recursive on each neighbor

        # visited.add(starting_vertex)
        # for neighbor in self.get_neighbors(starting_vertex):
        #     if neighbor not in visited:
        #         new_path = self.dft_recursive(neighbor, visited)

        # Starting out with visited defaulting to None
        # it will turn into a recursion error if not done this way
        if visited is None:
            visited = set()

        # Check if vertex (node) is visited, if not ...
        if starting_vertex not in visited:
            # mark as visited
            visited.add(starting_vertex)
            # DO THE THING!! (search stop when you find something)
            print(starting_vertex)
            # recurse all neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
    

# this function will determine the path to oldest ancestor
# Using of DFS

    def earliest(self, starting_vertex):
        # Create a stack and push(add) starting vertex       
        ss = Stack()
        # Put the starting point in that
        ss.push([starting_vertex])
        # Make a set to keep track of where we've been
        visited = set()
        # Track the path
        longest_path = [starting_vertex]
        # While there is stuff in the queue/stack
        while ss.size() > 0:
            #Pop the first item
            path = ss.pop()
            last_vertex = path[-1]
            # If not visited
            if last_vertex not in visited:
                # DO THE THING!! (search stop when you find something)
                print(last_vertex)
                # mark as visited
                visited.add(last_vertex)
                # For each edge in the item
                for next_vert in self.get_neighbors(last_vertex):
                    # Copy the path
                    new_path = list(path)
                    new_path.append(next_vert)
                    # Add that edge to the queue/stack
                    ss.push(new_path)
                    # compare the path lengths and update
                    if len(new_path) > len(longest_path):
                        longest_path = new_path
                    # path may be same size size but path has changed so check last element for change
                    if len(new_path) == len(longest_path) and new_path[-1] != longest_path[-1]:
                        longest_path = new_path
        return longest_path

#     