"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # This is our adjacency list
​
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
​
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
​
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            
​
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:  # size is in util.py
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!! (search and stop when you find something)
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

​
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack and push(add) starting vertex
        ss = Stack()
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
                # append/add all neighbors
                for next_vert in self.get_neighbors(last_vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)

    def dft_recursive(self, starting_vertex, visited=set(), path=[]):
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

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a Queue
        qq = Queue()
        #Create a set to store the visited verticies
        visited = set()
        # Enqueue a PATH to the starting vertex
        qq.enqueue([starting_vertex])
        # while the queue is not empty..
        while qq.size() > 0:
            # Dequeue the first PATH
            path = qq.dequeue()
            # Grab the vertex from the end of the path
            last_vertex = path[-1]
            # Check if vertex (node) is visited, if not
            if last_vertex not in visited:
                # DO THE THING!! (search stop when you find something)
                print(last_vertex)
                # mark as visited
                visited.add(last_vertex)
                # enqueue a path to all it's neighbors
                if last_vertex == destination_vertex:
                    return path
                # recurse all neighbors
                for next_vert in self.get_neighbors(last_vertex):
                    # Make a copy of the path
                    # new_path = path.copy()
                    new_path = list(path)
                    new_path.append(next_vert)
                    # enqueue the copy
                    qq.enqueue(new_path)            

        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """        

        # Create a Stack
        ss = Stack()
        # Create a set of traversed/visited vertices
        visited = set()
        # Push a PATH to the starting vertex
        ss.push([starting_vertex])
        # while the stack is not empty..
        while ss.size() > 0:
            # Dequeue/pop the the first index/vertex
            path = ss.pop()
            # Grab the vertex from the end of the path
            last_vertex = path[-1]
            # Check if vertex (node) is visited, if not
            if last_vertex not in visited:
                # DO THE THING!! (search stop when you find something)
                print(last_vertex)
                # mark as visited
                visited.add(last_vertex)
                # enqueue/add a path to all it's neighbors
                if last_vertex == destination_vertex:
                    return path
                for next_vert in self.get_neighbors(last_vertex):
                    # Make a copy of the path
                    # new_path = path.copy()
                    new_path = list(path)
                    # append/add all neighbors
                    new_path.append(next_vert)
                    # push the copy
                    ss.push(new_path)   
        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

