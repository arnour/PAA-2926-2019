from paa191t1.dijkstra.datastructs.tree.avl import AVL as Tree, AVLNode as Node


class AlfaNode(Node):

    def __init__(self, parent, k):
        super(AlfaNode, self).__init__(parent, k)
        self.size = 1

    @property
    def left_size(self):
        return self.left.size if self.left is not None else 0

    @property
    def right_size(self):
        return self.right.size if self.right is not None else 0

    def insert(self, node):
        super(AlfaNode, self).insert(node)
        self.size += 1

    def is_balanced(self, alfa=0.5):
        alfa_ratio = alfa * self.size
        return (self.left_size <= alfa_ratio) and (self.right_size <= alfa_ratio)

    def __label__(self):
        return f'[{self.key} ({self.size},{self.is_balanced()},{0.5 * self.size})]'


class Alfa(Tree):

    def __init__(self, alfa=0.5):
        super(Alfa, self).__init__()
        self.__alfa = alfa

    @property
    def alfa(self):
        return self.__alfa

    @property
    def is_balanced(self):
        return self.root.is_balanced(self.__alfa)

    def update_size(self, node):
        if node:
            node.size -= 1
            if node.parent:
                self.update_size(node.parent)

    def rebalance_delete(self, node):
        self.update_size(node)
        self.rebalance(node.parent)

    def rebalance_insert(self, node):
        self.rebalance(node)

    def rebalance(self, node):
        if node is None:
            return None

        root_to_rebuild = None
        seek = node

        while seek is not None:
            if not seek.is_balanced(self.__alfa):
                root_to_rebuild = seek
                seek = None
            else:
                seek = seek.parent

        if root_to_rebuild is not None:
            new_root = self.rebuild_subtree(root_to_rebuild)
            if new_root.parent is None:
                self.root = new_root
            else:
                if new_root.parent.left and new_root.parent.left.key == root_to_rebuild.key:
                    new_root.parent.left = new_root
                elif new_root.parent.right and new_root.parent.right.key == root_to_rebuild.key:
                    new_root.parent.right = new_root
            self.rebalance(new_root)

    def rebuild_subtree(self, root):
        values = self.inorder_values(root)
        return self.inorder_values_to_tree(root.parent, values, 0, len(values) - 1)

    def inorder_values(self, node):
        return self.traversal.inorder(node)

    def inorder_values_to_tree(self, parent, values, start, finish):
        if start > finish:
            return None
        median = (start + finish) // 2
        root = AlfaNode(parent, values[median])
        root.size = finish - start + 1
        root.left = self.inorder_values_to_tree(root, values, start, median - 1)
        root.right = self.inorder_values_to_tree(root, values, median + 1, finish)
        return root

    def new(self, parent, k):
        return AlfaNode(parent, k)
