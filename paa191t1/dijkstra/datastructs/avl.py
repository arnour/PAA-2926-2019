import math
from paa191t1.dijkstra import datastructs

class AVLNode(object):

    def __init__(self, dist, id):
        self.dist = dist 
        self.id = id
        self.left = None
        self.right = None
        self.height = 1

class AVL(object):

    def insert(self, dist, id):
        new_node = AVLNode(dist, id)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while True:
                if dist < node.dist or (dist == node.dist and id < node.id):
                    if node.left is None:
                        node.left = new_node
                        new_node.parent = node
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        new.parent = node
                        break
                    node = node.right
        # TODO chamar o rebalance
        return new_node
