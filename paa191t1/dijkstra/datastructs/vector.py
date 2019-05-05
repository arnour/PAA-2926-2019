import math
from paa191t1.dijkstra import datastructs


class Vector(datastructs.DijkstraDistance):

    def __call__(self, nodes):
        self.__nodes = []
        self.__distances = [None] * (max(nodes) + 1)
        for node in nodes:
            self.__nodes.append(node)
            self.__distances[node] = math.inf
        return self

    def pop(self):
        """Encontra e remove da lista de nós o nó com menor distância.

        Percorre o array de nós inteiro comparando as distâncias até encontrar o nó com menor distância.
        Então remove o nó da lista e retorna juntamento com sua distância.

        Returns:
            int, int: nó de menor distância e seu respectiva distância.
        """
        smallest = math.inf
        found = None
        for node in self.__nodes:
            if self.__distances[node] <= smallest:
                found = node
                smallest = self.__distances[node]
        self.__nodes.remove(found)
        return found, self.__distances[found]

    def update(self, node, distance):
        """Atualiza a distância de um nó

        Args:
            node (int): O nó a ser atualizado
            distance (int): A nova distância
        """
        self.__distances[node] = distance

    def has_nodes_to_visit(self):
        """bool: Retorna verdadeiro se existe algum nó que ainda não foi visitado. Do contrário, falso."""
        return len(self.__nodes) > 0

    def value(self, node):
        """Retorna a distância de um dado nó.

        Args:
            node (int): O nó
        """
        return self.__distances[node]

    @property
    def values(self):
        return dict([(k, v) for k, v in enumerate(self.__distances) if v is not None])
