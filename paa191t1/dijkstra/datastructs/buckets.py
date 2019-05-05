import math
from paa191t1.dijkstra import datastructs


class Buckets(datastructs.DijkstraDistance):

    def __call__(self, nodes):
        self._buckets = {}
        self._non_visited = nodes.copy()
        
        self._d_vector = [None] * (max(nodes) + 1)
        self._buckets[math.inf] = nodes.copy()
        for node in nodes:
            self._d_vector[node] = math.inf
        return self

    def pop(self):
        """Encontra e remove nos buckets o nó com menor distância.

        Percorre os buckets para encontrar o de menor peso de nós inteiro
        comparando as distâncias até encontrar o nó com menor distância.
        Então remove o nó da do bucket e retorna juntamente com sua distância.

        Returns:
            int, int: nó de menor distância e seu respectiva distância.
        """
        smallest = math.inf
        for b_keys in self._buckets.keys():
            if (b_keys <= smallest) and (len(self._buckets[b_keys]) > 0):
                smallest = b_keys
        node = self._buckets[smallest].pop()
        self._non_visited.remove(node)
        return node, smallest

    def update(self, node, distance):
        last_bucket = self._d_vector[node]
        self._d_vector[node] = distance
        self._buckets[last_bucket].remove(node)
        if self._buckets.get(distance):
            self._buckets[distance].append(node)
        else:
            self._buckets[distance] = [node]

    def has_nodes_to_visit(self):
        return len(self._non_visited) > 0

    def value(self, node):
        return self._d_vector[node]

    @property
    def values(self):
        return dict([(k, v) for k, v in enumerate(self._d_vector) if v is not None])
