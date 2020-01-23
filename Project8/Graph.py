"""
Name:
PID:
"""

import random
from Project8.Heap import AdaptableHeapPriorityQueue
# from Heap import *

def generate_edges(size, connectedness):
    """
    DO NOT EDIT THIS METHOD
    Generates undirected edges between vertices to form a graph
    :return: A generator object that returns a tuple of the form (source ID, destination ID)
    used to construct an edge
    """
    assert connectedness <= 1
    random.seed(10)
    for i in range(size):
        for j in range(i + 1, size):
            if random.randrange(0, 100) <= connectedness * 100:
                w = random.randint(1, 20)
                yield [i, j, w]


class Graph:
    """
    Class representing a Graph
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """

        __slots__ = ['start', 'destination', 'weight']

        def __init__(self, start, destination, weight):
            """
            DO NOT EDIT THIS METHOD
            :param start: represents the starting vertex of the edge
            :param destination: represents the destination vertex of the edge
            :param weight: represents the weight of the edge
            """
            self.start = start
            self.destination = destination
            self.weight = weight

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: edge to compare
            :return: Bool, True if same, otherwise False
            """
            return self.start == other.start and \
                   self.destination.vertex_id == other.destination.vertex_id \
                   and self.weight == other.weight

        def __repr__(self):
            return f"Start: {self.start} Destination: {self.destination} Weight: {self.weight}"

        __str__ = __repr__

        def get_start(self):
            """
            Gets the edges starting vertex id
            :return: vertex_id of any type
            """
            return self.start

        def get_destination(self):
            """
            Gets the edges destination vertex_id
            :return: vertex_id of destination
            """
            return self.destination.vertex_id

        def get_weight(self):
            """
            Get's the weight of the edge
            :return: [int] weight of edge
            """
            return self.weight

    class Vertex:
        """
        Class representing an Edge in the Graph
        """

        __slots__ = ['vertex_id', 'edges', 'visited']

        def __init__(self, vertex_id):
            """
            DO NOT EDIT THIS METHOD
            :param vertex_id: represents the unique identifier of the vertex
            """
            self.vertex_id = vertex_id
            self.edges = {}  # destination ID to edge object
            self.visited = False

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: vertex to compare
            :return: Bool, True if the same, False otherwise
            """
            return self.vertex_id == other.vertex_id and \
                   self.edges == other.edges and self.visited == other.visited

        def __repr__(self):
            return f"Vertex: {self.vertex_id}"

        __str__ = __repr__

        def degree(self):
            """
            Finds the degree of the vertex
            :return: [int] number of edges on current curent
            """
            return len(self.edges)

        def visit(self):
            """
            Sets the vertex's visit value to True
            :return: None
            """
            self.visited = True

        def insert_edge(self, destination, weight):
            """
            Adds an edge representation into the edge map between the vertex and the given
            :param destination: [Vertex] destination vertex
            :param weight: [int] weight of edge between source and destination
            :return: None
            """
            # # check to see if current vertex and destination already have edge
            if self.get_edge(destination.vertex_id) is not None:  # includes error checking
                edge = self.get_edge(destination.vertex_id)
                edge.weight = weight
            self.edges[destination.vertex_id] = Graph.Edge(self.vertex_id, destination, weight)

        def get_edge(self, destination):
            """
            Finds the edge with the given destination
            :param destination: [vertex] destination vertex
            :return:  [Edge] returns edge if found, None if not found
            """
            if destination in self.edges:
                return self.edges[destination]
            else:
                return None

        def get_edges(self):
            """
            Creates a list of all th vertex's edges
            :return: [list] list of edges
            """
            edge_list = []
            for edge in self.edges.values():
                edge_list.append(edge)
            return edge_list

    def __init__(self):
        """
        DO NOT EDIT THIS METHOD
        """
        self.adj_map = {}
        self.size = 0

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are Identical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        return self.adj_map == other.adj_map and self.size == other.size

    def add_to_graph(self, source, dest=None, weight=0):
        """
        Adds the source and destination to the graph with an edge. If parameters
        already in graph, connect them with an edge
        :param source: vertex_id of source already in graph or to create
        :param dest: vertex_id of destination already in graph or to create
        :param weight: [int] weight of edge
        :return: No return
        """
        source_vertex = self.Vertex(source)
        # if there is a element in the dest parameter
        if dest is not None:
            # if they are both already in graph but want new edge
            if source in self.adj_map and dest in self.adj_map:
                source_vertex = self.adj_map[source]
                dest_vertex = self.adj_map[dest]
                source_vertex.insert_edge(dest_vertex, weight)
                dest_vertex.insert_edge(source_vertex, weight)

            # if source and destination are not in map
            elif dest not in self.adj_map and source not in self.adj_map:
                dest_vertex = self.Vertex(dest)
                source_vertex = self.Vertex(source)
                source_vertex.insert_edge(dest_vertex, weight)
                dest_vertex.insert_edge(source_vertex, weight)
                self.adj_map[dest] = dest_vertex
                self.adj_map[source] = source_vertex
                self.size += 2

            # if source is in map and we are mapping to do new destination
            elif source in self.adj_map and dest not in self.adj_map:
                dest_vertex = self.Vertex(dest)
                source_vertex = self.adj_map[source]
                dest_vertex.insert_edge(source_vertex, weight)
                source_vertex.insert_edge(dest_vertex, weight)
                self.adj_map[dest] = dest_vertex
                self.size += 1

            # if source is not in map and we are mapping to existing destination
            else:
                source_vertex = self.Vertex(source)
                dest_vertex = self.adj_map[dest]
                source_vertex.insert_edge(dest_vertex, weight)
                dest_vertex.insert_edge(source_vertex, weight)
                self.adj_map[source] = source_vertex
                self.size += 1

        # if source in map and destination not provided
        else:
            self.adj_map[source] = source_vertex
            self.size += 1

    def construct_graph_from_file(self, filename):
        """
        Adds the information passed in through the file to the graph
        :param filename: [string] file name
        :return: No return
        """
        file = open(filename, "r+")
        test_lst = []
        # Add all potential vertices to list
        for i in file:
            i = i.split()

            test_lst.append(i)

        for i in test_lst:
            if i:
                if len(i) == 1:
                    if isinstance(i[0], str) and i[0].isdigit():
                        self.add_to_graph(int(i[0]))
                    else:
                        self.add_to_graph(i[0])
                elif len(i) == 2:
                    # both are integers
                    if (isinstance(i[0], str) and i[0].isdigit()) and (isinstance(i[1],
                                                                                  str) and i[1].isdigit()):
                        self.add_to_graph(int(i[0]), int(i[1]))
                    # dest is an integer
                    elif isinstance(i[1], str) and i[1].isdigit():
                        self.add_to_graph(i[0], int(i[1]))
                    # src is an integer
                    elif isinstance(i[0], str) and i[0].isdigit():
                        self.add_to_graph(int(i[0]), i[1])
                elif len(i) == 3:
                    self.add_to_graph(i[0], i[1], int(i[2]))
        file.close()

    def get_vertex(self, vertex_id):
        """
        Given vertex_id retrieve the corresponding vertex object
        :param vertex_id: Vertex_id of vertex to grab
        :return: [Vertex] vertex that has the pass in vertex_id
        """
        return self.adj_map[vertex_id]

    def get_vertices(self):
        """
        Creates a lust of all the vertices in the graph
        :return: [list] list containing all the vertices in graph
        """
        # adj_map is vertex_id:vertex
        vertex_list = []
        for value in self.adj_map.values():
            vertex_list.append(value)
        return vertex_list

    def bfs(self, start, target, path=None):
        """
        Does a breadth first search to find the path from start to target
        :param start: [vertex_id] start vertex
        :param target:  [vertex_id] target vertex
        :param path: [list] path from start to target
        :return: [list] list of vertex_ids from start to target
        """
        start_vertex = self.get_vertex(start)
        queue = []
        queue.append([start_vertex])
        while queue:
            currentpath = queue.pop()
            currentV = currentpath[-1]
            currentV.visit()
            if currentV.vertex_id == target:
                return [i.vertex_id for i in currentpath]
            for edge in currentV.get_edges():
                copy_path = currentpath.copy()
                if self.get_vertex(edge.get_destination()).visited is False:
                    copy_path.append(self.get_vertex(edge.get_destination()))
                    queue.append(copy_path)

    def dfs(self, start, target, path=None):
        """
        Does a depth first search to find the path from start to target
        :param start: [vertex_id] start vertex
        :param target:  [vertex_id] target vertex
        :param path: [list] path from start to target
        :return: [list] list of vertex_ids from start to target
        """
        start_vertex = self.get_vertex(start)
        path.append(start)
        if start == target:  # base case
            return path

        if not start_vertex.visited:
            start_vertex.visit()
            # get each edge attached to vertex
            for edge in start_vertex.get_edges():
                adjV = self.get_vertex(edge.get_destination())
                if not adjV.visited:
                    # recursively call dfs downt that path
                    new_path = self.dfs(adjV.vertex_id, target, path)
                    # if last element = target return that list
                    if new_path is not None and new_path[-1] == target:
                        return [i for i in new_path]
                    # if last not equal pop it and continue through vertices
                    path.pop(-1)


def quickest_route(filename, start, destination):
    """Compute shortest-path from start to destination
    :param filename: filename that contains elements to add to the graph
    :param start: [vertex_id] vertex to start on
    :param destination: [vertex_id] destination to find path to
    :return: [list] first element is total weight followed by the path taken
    """
    g = Graph()
    g.construct_graph_from_file(filename)
    d = {}  # d[v] is upper bound from s to v
    cloud = {}  # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()  # vertex v will have key d[v]
    pqlocator = {}  # map from vertex to its pq locator
    bool_dest = False
    bool_start = False
    for v in g.get_vertices():
        if v.vertex_id == destination:
            bool_dest = True
        if v.vertex_id == start:
            bool_start = True
    if bool_dest is False or bool_start is False:
        return []
    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.get_vertices():
        if v.vertex_id == start:
            d[v.vertex_id] = 0
        else:
            d[v.vertex_id] = float('inf')  # syntax for positive infinity
        # save locator for future updates
        pqlocator[v.vertex_id] = pq.add(d[v.vertex_id], v.vertex_id)

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key  # its correct d[u] value
        for e in g.get_vertex(u).get_edges():  # outgoing edges (u,v)
            v = e.get_destination()
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.get_weight()
                if d[u] + wgt < d[v]:  # better path to v?
                    d[v] = d[u] + wgt  # update the distance
                    pq.update(pqlocator[v], d[v], v, u)  # update the pq entry
                        #update(self,loc, newkey, newval, newprevious):

    # locate destination node in the priority queue
    dest_node = pqlocator[destination]
    shortest_path = [destination]
    # get previous of
    parent_str = pq.get_previous(dest_node)
    # backtrack through the queue and using get_previous find shortest path
    while True:
        if parent_str == "":  # root node will not have a previous
            break
        else:
            # add previous to shortest path and find next parent
            shortest_path = [parent_str] + shortest_path
            dest_node = pqlocator[parent_str]
            parent_str = pq.get_previous(dest_node)
    # using cloud dictionary pull on totaly weight length
    shortest_path = [cloud[destination]] + shortest_path
    # if there is not a path or vertices aren't connect return empty list
    if shortest_path[0] == float('inf'):
        return []
    else:
        return shortest_path

