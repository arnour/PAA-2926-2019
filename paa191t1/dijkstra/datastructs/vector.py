import math
from paa191t1.dijkstra import datastructs


class Vector(datastructs.DijkstraDistance):

    def __call__(self, nodes):
        """Cria um vetor com todos os nós e suas distâncias iniciais em O(v)

        Percorre o array de nós inteiro comparando criando um novo vetor com as distâncias iniciais de cada nó.

        Returns:
            self Vector
        """
        self.__nodes = []
        self.__distances = [None] * (max(nodes) + 1)
        for node in nodes:
            self.__nodes.append(node)
            self.__distances[node] = math.inf
        return self

    def pop(self):
        """Encontra e remove da lista de nós o nó com menor distância em O(v).

        Percorre a lista de nós não visitados comparando as distâncias até encontrar o nó com menor distância.
        Então remove o nó da lista e retorna juntamento com sua distância.

        Returns:
            int, int: nó de menor distância e sua respectiva distância.
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
        """Retorna a distância de um dado nó em O(1).

        Args:
            node (int): O nó
        """
        return self.__distances[node]

    @property
    def values(self):
        """Cria e retorna um dict com todos os nós e suas distâncias atualizadas em O(v).

        Args:
            dict(no: distancia)
        """
        return dict([(k, v) for k, v in enumerate(self.__distances) if v is not None])
