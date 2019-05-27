from paa191t1.dijkstra import datastructs
from paa191t1.dijkstra.datastructs.heap import MinHeapNode
from paa191t1.dijkstra.datastructs.heap.fibonacci import FibonacciHeap
import math


class FibHeap(datastructs.DijkstraDistance):

    def __call__(self, nodes):

        self.__distances = [None] * (max(nodes) + 1)
        self.__heap = FibonacciHeap()

        for node in nodes:
            heap_node = self.__heap.Node(MinHeapNode(node, math.inf))
            self.__distances[node] = heap_node
            self.__heap.insert(heap_node)

        return self

    def pop(self):
        """Remove o nó com menor distância da heap e aplica as operações para garantir as invariantes em O(lg v)
        Returns:
            int, int: nó de menor distância e sua respectiva distância.
        """
        heap_node = self.__heap.extract_min().data
        return heap_node.vertex, heap_node.distance

    def update(self, node, distance):
        """Atualiza a distância de um dado aplicando a operação decrease_key da fib em O(1).
       Args:
           node (int): O nó a ser atualizado
           distance (int): A nova distância
        """
        heap_node = self.__distances[node]  # O(1) para pegar a referência do nó a atualizar
        new_distance = MinHeapNode(node, distance)
        self.__heap.decrease_key(heap_node, new_distance)  # O(1) para fazer o decrease + consolidate, o heap_node é atualizado por referência.

    def has_nodes_to_visit(self):
        """bool: Retorna verdadeiro se existe algum nó que ainda não foi visitado. Do contrário, falso."""
        return (self.__heap.total_nodes > 0)

    def value(self, node):
        """Retorna a distância de um dado nó.
        Args:
            node (int): O nó
        """
        return self.__distances[node].data.distance

    @property
    def values(self):
        return dict([(k, v.data.distance) for k, v in enumerate(self.__distances) if v is not None])
