"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # this is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('Error getting neighbors')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # create a queue and enqueue starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # create a set of traversed vertices
        visited = set()

        # while queue is not empty:
        while queue.size() > 0:
            # dequeue/pop the first vertex
            path = queue.dequeue()
            # if not visited
            if path[-1] not in visited:
                # print it
                print(path[-1])
                # mark as visted
                visited.add(path[-1])
                # enqueue all neighbors
                for vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(vertex)
                    queue.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack and push starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # create a set of traversed vertices
        visited = set()

        # while stack is not empty:
        while stack.size() > 0:
            # pop the first vertex
            path = stack.pop()
            # if not visited
            if path[-1] not in visited:
                # print it
                print(path[-1])
                # mark as visted
                visited.add(path[-1])
                # push all neighbors
                for vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(vertex)
                    stack.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base case
        if visited is None:
            # create a set of traversed vertices
            visited = set()
        # mark the starting vertex as visited
        visited.add(starting_vertex)
        # print the starting vertex
        print(starting_vertex)
        # traverse all the neighbors and call the recursive function with index of adjacent vertex
        for vertex in self.get_neighbors(starting_vertex):
            if vertex not in visited:
                self.dft_recursive(vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue and enqueue starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # create a set of traversed vertices
        visited = set()

        # while queue is not empty:
        while queue.size() > 0:
            # dequeue/pop the first vertex
            path = queue.dequeue()
            # if not visited
            if path[-1] not in visited:
                # check to see if vertex is the same as destination vertex
                if path[-1] == destination_vertex:
                    # if it is, return the entire path
                    return path
                # mark as visted
                visited.add(path[-1])
                # enqueue all neighbors
                for vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(vertex)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack and push starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # create a set of traversed vertices
        visited = set()

        # while stack is not empty:
        while stack.size() > 0:
            # pop the first vertex
            path = stack.pop()
            # if not visited
            if path[-1] not in visited:
                # check to see if vertex is the same as destination vertex
                if path[-1] == destination_vertex:
                    # if it is, return the entire path
                    return path
                # mark as visted
                visited.add(path[-1])
                # push all neighbors
                for vertex in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(vertex)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # base case
        if visited is None:
            # create a set of traversed vertices
            visited = set()

        if path is None:
            path = []
        # mark the starting vertex as visited
        visited.add(starting_vertex)
        # set path to path plus the starting vertex
        path = path + [starting_vertex]
        # check to see if starting vertex is the same as destination vertex
        if starting_vertex == destination_vertex:
            # if it is return the path
            return path
        # traverse all the neighbors and call the recursive function with index of adjacent vertex
        for vertex in self.get_neighbors(starting_vertex):
            if vertex not in visited:
                new_path = self.dfs_recursive(
                    vertex, destination_vertex, visited, path)
                if new_path:
                    return new_path


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
