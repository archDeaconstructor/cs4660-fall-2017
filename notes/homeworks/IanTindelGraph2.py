"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    with open(file_path) as f:
        lines = f.readlines()
    lines = [eachline.strip() for eachline in lines]
    for num in range(0,lines[0]):
        graph.add_node(num)
        newEdge = Edge((line[num+1].split(":")[0]),
                       (line[num+1].split(":")[1]),
                       (line[num+1].split(":")[2]))
        graph.add_edge(newEdge)
    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        if self.adjacency_list[node_1] = node_2:
            return true
        elif self.adjacency_list[node_2] = node_1:
            return true
        else:
            return false

    def neighbors(self, node):
        return self.adjacency_list[node]

    def add_node(self, node):
       for num in range(0,len(self.adjacency_list)):
            if self.adjacency_list(num) = node:
                return false
       self.adjacency_list[node] = []
       return true

    def remove_node(self, node):
        for num in range(0,len(self.adjacency_list)):
            if self.adjacency_list(num) = node:
                del self.adjacency_list[node]
                return true
        return false

    def add_edge(self, edge):
        for num in range(0,len(self.adjacency_list)):
            for num2 in range(0,len(self.adjacency_list[num])):
                if self.adjacency_list[num][num2] = ("Edge (" + edge.from_node + "," + edge.to_node + "," + edge.weight +")"):
                    return false
        self.adjacency_list[edge.from_node].append("Edge (" + edge.from_node + "," + edge.to_node + "," + edge.weight +")")
        return true

    def remove_edge(self, edge):
        for num in range(0,len(self.adjacency_list)):
            for num2 in range(0,len(self.adjacency_list[num])):
                if self.adjacency_list[num][num2] = ("Edge (" + edge.from_node + "," + edge.to_node + "," + edge.weight +")"):
                    del self.adjacency_list[num][num2]
                    return true
        return false

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        if self.adjacency_matrix[node_1][node_2] = 1:
            return true
        else:
            return false

    def neighbors(self, node):
        result = []
        for num in range(0,len(self.nodes)):
            if self.adjacency_matrix[node][num] = 1:
                result.append(num)
        if result != []:
            return result
        elif result = []:
            return result

    def add_node(self, node):
        for num in range(0,len(self.nodes)):
            if self.nodes(num) = node:
                return false
        self.nodes.append(node)
        newRow = [node]
        self.adjacency_matrix[0].append(node)
        for num in range(1,len(self.nodes)):
            self.adjacency_matrix[num].append(0)
            newRow.append(0)
        self.adjacency_matrix.append(newRow)
        return true

    def remove_node(self, node):
        for num in range(0,len(self.nodes)):
            if self.nodes(num) = node:
                del self.adjacency_matrix(__get_node_index(node))
                for num in range(0,len(self.nodes)):
                    del self.adjacency_matrix[num][(__get_node_index(node))]
                del self.nodes(__get_node_index(node))
                return true
        return false

    def add_edge(self, edge):
        if (self.adjacency_matrix[edge.from_node][edge.to_node] = 0):
            self.adjacency_matrix[edge.from_node][edge.to_node] = 1
            self.adjacency_matrix[edge.to_node][edge.from_node] = 1
            return true
        return false

    def remove_edge(self, edge):
        if (self.adjacency_matrix[edge.from_node][edge.to_node] = 1):
            self.adjacency_matrix[edge.from_node][edge.to_node] = 0
            self.adjacency_matrix[edge.to_node][edge.from_node] = 0
            return true
        return false

    def __get_node_index(self, node):
        """helper method to find node index"""
        for num in range(0,len(self.nodes)):
            if self.nodes(num) = node:
                return num
        return false

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        pass

    def neighbors(self, node):
        pass

    def add_node(self, node):
        pass

    def remove_node(self, node):
        pass

    def add_edge(self, edge):
        pass

    def remove_edge(self, edge):
        pass

