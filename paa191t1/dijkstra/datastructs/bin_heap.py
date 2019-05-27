from paa191t1.dijkstra import datastructs
from paa191t1.dijkstra.datastructs.heap import MinHeapNode
import math
import heapq


class Heap(datastructs.DijkstraDistance):

    def __call__(self, nodes):
        """Cria a Min-Heap com base nos nós em O(v) e um dict que guarda as distâncias de
        todos os nós em O(v) porque precisa percorrer todos os vértices.

        Para criar um dict acessório de não visitados também leva o tempo O(v).

        Args:
            nodes (list): lista de nós do grafo

        Returns:
            self Buckets
        """
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
                sempre estará na raiz. O custo para a busca e remoção da min heap
                é O(log(V)), onde V é o número de vértices do grafo armazenado na
                heap.
        Returns:
            int, int: nó de menor distância e sua respectiva distância.
    """
        heap_node = heapq.heappop(self.__heap)

        return heap_node.vertex, heap_node.distance

    def _search_node_index(self, node, i=0):
        """Encontra o índice de um dado nó armazenado na heap binária.
        A complexidade desta etapa, considerando o pior caso onde o nó
        está na raiz da árvore, é O(log(V)).
        Returns:
            int: índice do nó a ser requisitado.
        """

        if i >= len(self.__heap):
            return False

        heap_node = self.__heap[i]

        if node == heap_node:
            return i
        elif node < heap_node:
            return False
        elif node > heap_node:
            left_child = self._search_node_index(node, 2 * i + 1)
            right_child = self._search_node_index(node, 2 * i + 2)
            return left_child or right_child

    def update(self, node, distance):
        """Atualiza a distância de um dado nó e recalcula a posição correta
           na heap binária dada a nova distância. A complexidade desta etapa,
           considerando o pior caso onde toda a lista será atualizada, é O(log(V)).
       Args:
           node (int): O nó a ser atualizado
           distance (int): A nova distância
    """
        index = self._search_node_index(MinHeapNode(node, self.__distances[node]))  # O(log(V))
        heap_node = self.__heap.pop(index)  # O(1)
        heap_node.distance = distance
        self.__distances[heap_node.vertex] = heap_node.distance
        heapq.heappush(self.__heap, heap_node)  # O(log(V))

    def has_nodes_to_visit(self):
        """Valida nós visitados em O(1)

        Returns:
            bool: Retorna verdadeiro se existe algum nó que ainda não foi visitado. Do contrário, falso.
        """
        return (len(self.__heap) > 0)

    def value(self, node):
        """Retorna a distância de um dado nó em O(1).

        Args:
            node (int): O nó

        Returns:
            int: distancia
        """
        return self.__distances[node]

    @property
    def values(self):
        """Cria e retorna um dict com todos os nós e suas distâncias atualizadas em O(v).

        Returns:
            dict(no: distancia)
        """
        return dict([(k, v) for k, v in enumerate(self.__distances) if v is not None])
