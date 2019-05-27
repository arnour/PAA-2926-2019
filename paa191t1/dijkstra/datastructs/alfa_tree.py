import math
from paa191t1.dijkstra.datastructs.tree import DistanceNode
from paa191t1.dijkstra.datastructs.tree.alfa import Alfa as Tree
from paa191t1.dijkstra import datastructs


class AlfaTree(datastructs.DijkstraDistance):

    def __call__(self, nodes):
        """Cria uma árvore alfa-balanceada com todos os nós e suas distâncias iniciais em O(v log v)

        Percorre a lista de nós em O(v) e insere cada nó com sua distância inicial na árvore em O(log v).

        Returns:
            self AlfaTree
        """
        self.__tree = Tree()
        self.__nodes = len(nodes)
        self.__distances = [None] * (max(nodes) + 1)
        for node in nodes:
            self.__distances[node] = math.inf
            self.__tree.insert(DistanceNode(node, math.inf))
        return self

    def pop(self):
        """Encontra e remove da arvore o nó com menor distância. O(lg v)

        Percorre a árvore, comparando lg v nós até encontrar o nó mais a esquerda, que por definição é o menor.
        Então remove o nó da árvore e retorna juntamento com sua distância.

        Returns:
            int, int: nó de menor distância e sua respectiva distância.
        """
        self.__nodes -= 1
        popped = self.__tree.delete_min()
        return popped.key.vertex, popped.key.distance

    def update(self, node, distance):
        """Atualiza a distância de um nó.

        Encontra o nó em O(lg v), remove o nó em O(lg v) e reinsere o nó atualizado em O(lg v)

        Args:
            node (int): O nó a ser atualizado
            distance (int): A nova distância
        """
        self.__tree.delete(DistanceNode(node, self.__distances[node]))
        self.__tree.insert(DistanceNode(node, distance))
        self.__distances[node] = distance

    def has_nodes_to_visit(self):
        """bool: Retorna verdadeiro se existe algum nó que ainda não foi visitado. Do contrário, falso."""
        return self.__nodes > 0

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
