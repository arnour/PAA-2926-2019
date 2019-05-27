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
        """Encontra e remove na heap de fibonacci o nó com menor distância.
        Percorrer a heap de fibonacci para achar o nó com a menor distância.
        No caso aqui implementado, o nó com a menor distância sempre estará
        na raiz. A complexidade para esta etapa, no pior caso é O(log(V)), 
        onde V é a quantidade de vértices no grafo armazenado na heap de
        fibonacci.                
        Returns:
            int, int: nó de menor distância e sua respectiva distância.
    """
        heap_node = self.__heap.extract_min().data

        return heap_node.vertex, heap_node.distance

    def _node_to_min(self, node):
        """Verifica se o dado nó está na lista de nós na raiz da heap de fibonacci.
           Caso esteja, atualiza o valor do nó e reajusta a ordem da heap de fibonacci.
           A complexidade desta função, no pior caso, seria O(?) [deveria ser O(1), mas
           tem um loop do lado de fora do decrease key]
        Returns:
            logic: True or False dependendo se o nó está ou não na raiz da Heap.
    """
        for heap_node in self.__heap.iterate(self.__heap.root_list):
            if node == heap_node.data.vertex:
                copy_node = MinHeapNode(node, -1)
                self.__heap.decrease_key(heap_node, copy_node)
                return True
        return False

    def update(self, node, distance):
        """Atualiza a distância de um dado nó e recalcula as posições corretas
           na heap de fibonacci dada a nova distância. O processo toma complexidade,
           no pior caso, O(log(V)).
       Args:
           node (int): O nó a ser atualizado
           distance (int): A nova distância
    """
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
