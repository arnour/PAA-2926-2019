import math
from paa191t1.dijkstra.datastructs.tree import DistanceNode
from paa191t1.dijkstra.datastructs.tree.alfa import Alfa as Tree
from paa191t1.dijkstra import datastructs


class AlfaTree(datastructs.DijkstraDistance):

    def __call__(self, nodes):
        self.__tree = Tree()
        self.__nodes = len(nodes)
        self.__distances = [None] * (max(nodes) + 1)
        for node in nodes:
            self.__distances[node] = math.inf
            self.__tree.insert(DistanceNode(node, math.inf))
        return self

    def pop(self):
        self.__nodes -= 1
        popped = self.__tree.delete_min()
        return popped.key.vertex, popped.key.distance

    def update(self, node, distance):
        self.__tree.delete(DistanceNode(node, self.__distances[node]))
        self.__tree.insert(DistanceNode(node, distance))
        self.__distances[node] = distance

    def has_nodes_to_visit(self):
        return self.__nodes > 0

    def value(self, node):
        return self.__distances[node]

    @property
    def values(self):
        return dict([(k, v) for k, v in enumerate(self.__distances) if v is not None])
