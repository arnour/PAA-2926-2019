class Graph(object):
    """Graph é um wrapper para simplificar e abstrair detalhes de implementação de qualquer biblioteca
     de grafos que seja utilizada neste projeto.

     Examples:
        >>> import networkx as nx

        >>> dg = nx.DiGraph()
        >>> dg.add_weighted_edges_from([(0, 1, 1), (1, 2, 1), (2, 3, 1)])

        >>> graph = graph.Graph(dg)

        >>> graph.all_nodes()
        [0, 1, 2, 3]

        >>> graph.successors(0)
        [1]

        >>> graph.edge_weight(0, 1)
        1
    """

    def __init__(self, graphx):
        self.__graphx = graphx

    def all_nodes(self):
        """list(int): Retorna uma lista com todos os nós do grafo"""
        return self.__graphx.nodes()

    def successors(self, origin_node):
        """Retorna uma lista com todos os nós adjascentes ao nó origem informado.
        Args:
            origin_node (int): O nó origem da aresta

        Returns:
            list(int): a lista de nós adjascentes
        """
        return self.__graphx.successors(origin_node)

    def edge_weight(self, origin_node, target_node):
        """Retorna o peso da aresta (origin_node, target_node)

        Args:
            origin_node (int): O nó origem da aresta
            target_node (int): O nó destino da aresta

        Returns:
            float: o peso da aresta
        """
        return self.__graphx.edges[origin_node, target_node]['weight']
