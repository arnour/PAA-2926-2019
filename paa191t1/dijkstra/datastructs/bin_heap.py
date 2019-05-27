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
	"""Encontra e remove na heap binária o nó com menor distância.
        Percorrer a heap binária para achar o nó com a menor distância.
		No caso da min heap aqui implementada, o nó com a menor distância 
		sempre estará na raiz.
        Returns:
            int, int: nó de menor distância e sua respectiva distância.
    """
        heap_node = heapq.heappop(self.__heap)

        return heap_node.vertex, heap_node.distance

    def _search_node_index(self, node):
	"""Encontra o índice de um dado nó armazenado na heap binária.
       Returns:
            int: índice do nó a ser requisitado.
    """
        for index, heap_node in enumerate(self.__heap):
            if node == heap_node.vertex:
                return index

    def update(self, node, distance):
	"""Atualiza a distância de um dado nó e recalcula a posição correta
	   na heap binária dada a nova distância. 
       Args:
           node (int): O nó a ser atualizado
           distance (int): A nova distância
    """
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
