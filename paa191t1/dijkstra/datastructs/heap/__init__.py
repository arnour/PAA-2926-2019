from paa191t1.dijkstra.datastructs.tree import DistanceNode


class MinHeapNode(DistanceNode):
    """Estrutura de comparação de um nó da heap de mínimo."""

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
