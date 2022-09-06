from collections import defaultdict
from random import choice

class Graph(object):
    
    def __init__(self):
        self._connections = defaultdict(set)
    
    @property
    def connections(self):
        return self._connections
        
    @connections.setter
    def connections(self, value):
        self._connections = defaultdict(set)
        self._connections.update(value)
    
    def copy(self, donor):
        graph_copy = type(self)()
        graph_copy.connections = donor.connections
        return graph_copy
    
    def add_arc(self, source, destination):
        self._connections[source].add(destination)
        self._connections[destination].add(source)
                
    def remove_node(self, node):
        for connected_node in self._connections[node]:
            self._connections[connected_node].remove(node)
        del self._connections[node]
    

def choice(nodes, graph):
    """Select the node to walk to."""
    nodes = list(nodes)
    best_choice = None
    best_choice_score = float("inf")
    for node in nodes:
        this_node_score = len(graph._connections[node])
        if this_node_score < best_choice_score:
            best_choice_score = this_node_score
            best_choice = node
    return best_choice

def random_walk(graph):
    current_node = choice(graph._connections.keys(), graph)
    path = []
    while True:
        path.append(current_node)
        choices = graph._connections[current_node]
        if not choices:
            break
        graph.remove_node(current_node)
        next_node = choice(choices, graph)
        current_node = next_node
    return path

def read_inputs():
    return input().strip().split()

number_of_cities, number_of_roads = map(int, read_inputs())

roads = []
for _ in range(number_of_roads):
    roads.append(read_inputs())

graph = Graph()
for source, destination in roads:
    graph.add_arc(source, destination)

path = random_walk(graph)
print(len(path))
print(*path)
