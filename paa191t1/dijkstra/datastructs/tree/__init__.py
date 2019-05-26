class DistanceNode(object):
    """Estrutura de comparação de um nó de distância"""
    
    def __init__(self, vertex, distance):
        if vertex is None or distance is None:
            raise ValueError('vertex and distance are required to create a Distance node.')
        self.vertex = vertex
        self.distance = distance

    def __eq__(self, other):
        if other is not None:
            return (self.vertex == other.vertex and self.distance == other.distance)
        return False

    def __gt__(self, other):
        if other is not None:
            return (self.distance > other.distance) or (self.distance == other.distance and self.vertex > other.vertex)
        return False

    def __ge__(self, other):
        if other is not None:
            return (self.distance >= other.distance) or (self.distance == other.distance and self.vertex > other.vertex)
        return False

    def __lt__(self, other):
        if other is not None:
            return (self.distance < other.distance) or (self.distance == other.distance and self.vertex < other.vertex)
        return False

    def __le__(self, other):
        if other is not None:
            return (self.distance <= other.distance) or (self.distance == other.distance and self.vertex < other.vertex)
        return False


    def __str__(self):
        return f'(v: {self.vertex}, d: {self.distance})'

    __repr__ = __str__


class TreeTraversal(object):

    def inorder(self, root):
        nodes = []
        if root:
            nodes = nodes + self.inorder(root.left)
            nodes.append(root.key)
            nodes = nodes + self.inorder(root.right)
        return nodes
