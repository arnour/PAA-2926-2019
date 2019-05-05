class DijkstraDistance(object):

    def pop(self):
        raise NotImplementedError('pop is not implemented in this class. Use one of its sub classes.')

    def update(self, node, distance):
        raise NotImplementedError('update is not implemented in this class. Use one of its sub classes.')

    def has_nodes_to_visit(self):
        raise NotImplementedError('has_nodes_to_visit is not implemented in this class. Use one of its sub classes.')

    def value(self, node):
        raise NotImplementedError('distance is not implemented in this class. Use one of its sub classes.')

    @property
    def values(self):
        raise NotImplementedError('values is not implemented in this class. Use one of its sub classes.')
