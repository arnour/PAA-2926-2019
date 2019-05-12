from paa191t1.dijkstra.datastructs.tree.bst import Node


class AVLNode(Node):

    def __init__(self, key, left=None, right=None, **kargs):
        Node.__init__(self, key, left=None, right=None, **kargs)
        self.balance_factor = 0

    def add_child(self, node):
        self.balance_factor += 1
        Node.add_child(self, node)
