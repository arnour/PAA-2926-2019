class Graph(object):

    def __init__(self, graphx):
        self.__graphx = graphx

    def all_nodes(self):
        return self.__graphx.nodes()

    def successors(self, origin_node):
        return self.__graphx.successors(origin_node)

    def edge_weight(self, origin_node, target_node):
        return self.__graphx.edges[origin_node, target_node]['weight']
