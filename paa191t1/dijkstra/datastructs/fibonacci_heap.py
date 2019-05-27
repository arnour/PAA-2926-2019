from paa191t1.dijkstra import datastructs
from paa191t1.dijkstra.datastructs.heap import MinHeapNode
from paa191t1.dijkstra.datastructs.heap.fibonacci import FibonacciHeap
import math


class FibHeap(datastructs.DijkstraDistance):

    def __call__(self, nodes):

        self.__distances = [None] * (max(nodes) + 1)

        self.__heap = FibonacciHeap()

        for node in nodes:
            self.__distances[node] = math.inf
            self.__heap.insert(MinHeapNode(node, math.inf))

        return self

    def pop(self):
        heap_node = self.__heap.extract_min().data

        return heap_node.vertex, heap_node.distance
 
    def _node_to_min(self, node):
        for heap_node in self.__heap.iterate(self.__heap.root_list):
            if node == heap_node.data.vertex:
                copy_node = MinHeapNode(node, -1)
                self.__heap.decrease_key(heap_node, copy_node)
                return True
        return False

    def update(self, node, distance):
        if (self._node_to_min(node)):
            self.__heap.extract_min()
        self.__heap.insert(MinHeapNode(node, distance))
        self.__distances[node] = distance

    def has_nodes_to_visit(self):
        """bool: Retorna verdadeiro se existe algum nó que ainda não foi visitado. Do contrário, falso."""
        return (self.__heap.total_nodes > 0)

    def value(self, node):
        """Retorna a distância de um dado nó.
        Args:
            node (int): O nó
        """
        return self.__distances[node]

    @property
    def values(self):
        return dict([(k, v) for k, v in enumerate(self.__distances) if v is not None])