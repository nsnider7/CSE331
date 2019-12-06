"""
Name:
PID:
"""

import random


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
            return self.start

        def get_destination(self):
            return self.destination.vertex_id

        def get_weight(self):
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
            return len(self.edges)

        def visit(self):
            self.visited = True

        def insert_edge(self, destination, weight):
            """
            Adds an edge representation into the edge map between the vertex and the given
            :param destination:
            :param weight:
            :return:
            """
            # # check to see if current vertex and destination already have edge
            if self.get_edge(destination.vertex_id) is not None:  # includes error checking
                e = self.get_edge(destination.vertex_id)
                e.weight = weight
            self.edges[destination.vertex_id] = Graph.Edge(self.vertex_id, destination, weight)

        def get_edge(self, destination):
            if destination in self.edges:
                return self.edges[destination]
            else:
                return None

        def get_edges(self):
            edge_list = []
            for e in self.edges.values():
                edge_list.append(e)
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
        Inserts a vertex into the graph and will create an edge if a destination and weight
        are provided. If the source or destination vertex does not exist in the graph then one will be created.
        :param source:
        :param dest:
        :param weight:
        :return:
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
        A line in the file could also have just a source or it could have a source and destination,
        but no weight. Make sure that if the sources/destinations are integers that they are converted to integers properly
        :param filename:
        :return:
        """
        file = open(filename, "r+")
        test_lst = []
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
                    if (isinstance(i[0], str) and i[0].isdigit()) and (isinstance(i[1], str) and i[1].isdigit()):
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
        return self.adj_map[vertex_id]

    def get_vertices(self):
        # adj_map is vertex_id:vertex
        vertex_list = []
        for key, val in self.adj_map.items():
            vertex_list.append(val)
        return vertex_list

    def bfs(self, start, target, path=None):
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
        start_vertex = self.get_vertex(start)
        path.append(start)
        if start == target:  # base case
            return path

        if not start_vertex.visited:
            start_vertex.visit()
            for edge in start_vertex.get_edges():
                adjV = self.get_vertex(edge.get_destination())
                if not adjV.visited:
                    new_path = self.dfs(adjV.vertex_id, target, path)
                    if new_path is not None and new_path[-1] == target:
                        return [i for i in new_path]
                    path.pop(-1)


def quickest_route(filename, start, destination):
    """Compute shortest-path distances from src to reachable vertices of g.

    Graph g can be undirected or directed, but must be weighted such that
    e.element() returns a numeric weight for each edge e.

    Return dictionary mapping each reachable vertex to its distance from src.
    """
    g = Graph()
    g.construct_graph_from_file(filename)
    d = {}  # d[v] is upper bound from s to v
    cloud = {}  # map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()  # vertex v will have key d[v]
    pqlocator = {}  # map from vertex to its pq locator

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the source having distance 0 and all others having infinite distance
    for v in g.get_vertices():
        if v.vertex_id is start:
            d[v.vertex_id] = 0
        else:
            d[v.vertex_id] = float('inf')  # syntax for positive infinity
        pqlocator[v.vertex_id] = pq.add(d[v.vertex_id], v.vertex_id)  # save locator for future updates

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key  # its correct d[u] value
        del pqlocator[u]  # u is no longer in pq
        for e in g.get_vertex(u).get_edges():  # outgoing edges (u,v)
            v = e.get_destination()
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                wgt = e.get_weight()
                if d[u] + wgt < d[v]:  # better path to v?
                    d[v] = d[u] + wgt  # update the distance
                    pq.update(pqlocator[v], d[v], v)  # update the pq entry

    return cloud
