import math
from pyllist import dllist
from paa191t1.dijkstra import datastructs


class Buckets(datastructs.DijkstraDistance):

    def __call__(self, nodes):
        """Cria um Bucket de distância infinita inicialmente em O(1) e um vetor d (dict) que
        guarda as distâncias de todos os nós em O(v) porque precisa percorrer todos os vértices.

        Para criar um dict acessório de não visitados também leva o tempo O(v).

        Args:
            nodes (list): lista de nós do grafo

        Returns:
            self Buckets
        """
        self._buckets = {}
        self._non_visited = dict.fromkeys(nodes.copy())

        self._d_vector = [None] * (max(nodes) + 1)
        self._buckets[math.inf] = dllist(nodes.copy())
        for node in nodes:
            self._d_vector[node] = math.inf
        return self

    def pop(self):
        """Encontra e remove nos buckets o nó com menor distância.

        Percorre os buckets em O(b), sendo b a quantidade de buckets,
        para encontrar o de menor peso de nós inteiro
        comparando as distâncias até encontrar o nó com menor distância.
        Então remove o nó da do bucket e retorna juntamente com sua distância.

        Returns:
            int, int: nó de menor distância e sua respectiva distância.
        """
        smallest = math.inf
        for b_keys in self._buckets.keys():  # O(b) sendo b a quantidade de buckets
            if (b_keys <= smallest) and (self._buckets[b_keys].size > 0):
                smallest = b_keys
        node = self._buckets[smallest].pop()
        del self._non_visited[node]  # Remove elemento em O(1)
        return node, smallest

    def __pop_node(self, _dllist, value):
        """Acha e remove objeto do nó em O(v) na lista duplamente encadeada.

        Args:
            _dllist (dllist): lista duplamente encadeada a ser buscada
            value (int): valor a buscar na lista

        Returns:
            dllistnode: nó buscado.
        """
        node = _dllist.first
        while node.next is not None:  # O(v)
            if node.value == value:
                break
            node = node.next
        return _dllist.remove(node)

    def update(self, node, distance):
        """Atualiza a distância de um nó no seu bucket correto em O(v).

        Atualiza o vetor de mapeamento de nó para o bucket e coloca o
        nó dentro do bucket correto.

        Args:
            node (int): O nó a ser atualizado
            distance (int): A nova distância
        """
        last_bucket = self._d_vector[node]
        self._d_vector[node] = distance
        self.__pop_node(self._buckets[last_bucket], node)  # O(v)
        if self._buckets.get(distance):
            self._buckets[distance].append(node)
        else:
            self._buckets[distance] = dllist([node])

    def has_nodes_to_visit(self):
        """Valida nós visitados em O(1)

        Returns:
            bool: Retorna verdadeiro se existe algum nó que ainda não foi visitado. Do contrário, falso.
        """
        return len(self._non_visited) > 0

    def value(self, node):
        """Retorna a distância de um dado nó em O(1).

        Args:
            node (int): O nó

       Returns:
            int: distancia
        """
        return self._d_vector[node]

    @property
    def values(self):
        """Cria e retorna um dict com todos os nós e suas distâncias atualizadas em O(v).

        Returns:
            dict(no: distancia)
        """
        return dict([(k, v) for k, v in enumerate(self._d_vector) if v is not None])
