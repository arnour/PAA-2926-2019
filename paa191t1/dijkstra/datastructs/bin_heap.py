from paa191t1.dijkstra import datastructs
from paa191t1.dijkstra.datastructs.heap import MinHeapNode
import math
import heapq


class Heap(datastructs.DijkstraDistance):

    def __call__(self, nodes):

        self.__distances = [None] * (max(nodes) + 1)

        self.__heap = []

        for node in nodes:
            self.__distances[node] = math.inf
            self.__heap.append(MinHeapNode(node, math.inf))

        heapq.heapify(self.__heap)
        return self

    def pop(self):
        heap_node = heapq.heappop(self.__heap)
        self.__distances[heap_node.vertex] = heap_node.distance

        return heap_node.vertex, heap_node.distance

    def _search_node_index(self, node):
        for index, heap_node in enumerate(self.__heap):
            if node == heap_node.vertex:
                return index

    def update(self, node, distance):

        index = self._search_node_index(node)
        
        heap_node = self.__heap[index]
        heap_node.distance = distance
        self.__distances[heap_node.vertex] = heap_node.distance
        heapq.heapify(self.__heap)

    def has_nodes_to_visit(self):
        """bool: Retorna verdadeiro se existe algum nó que ainda não foi visitado. Do contrário, falso."""
        return (len(self.__heap) > 0)

    def value(self, node):
        """Retorna a distância de um dado nó.
        Args:
            node (int): O nó
        """
        return self.__distances[node]

    @property
    def values(self):
        return dict([(k, v) for k, v in enumerate(self.__distances) if v is not None])
