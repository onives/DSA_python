# graph representation

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
    pass


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
    pass
