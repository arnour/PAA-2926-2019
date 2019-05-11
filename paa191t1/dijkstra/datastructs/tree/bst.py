class Node(object):

    def __init__(self, key, left=None, right=None, **kargs):
        self.key = key
        self.left = left
        self.right = right
        self.props = kargs
        self.parent = None

    def prop(self, name):
        return self.props[name]

    def find_smallest(self):
        if bool(self.left):
            return self.left.find_smallest()
        else:
            return self

    def remove(self):
        if self.is_left_child():
            self.parent.left = None
        else:
            self.parent.right = None
        self.left = None
        self.right = None
        self.props = None

    def has_child(self):
        return bool(self.left) or bool(self.right)

    def has_both_child(self):
        return bool(self.left) and bool(self.right)

    def is_left_child(self):
        return bool(self.parent) and self.parent.left == self

    def get_only_child(self):
        return self.left if bool(self.left) else self.right

    def add_child(self, node):
        if node > self:
            if self.right is None:
                self.right = node
                node.parent = self
            self.right.add_child(node)
        if node < self:
            if self.left is None:
                self.left = node
                node.parent = self
            self.left.add_child(node)

    def find_child(self, node):
        if self == node:
            return self
        if node > self:
            if self.right is None:
                return None
            return self.right.find_child(node)
        if node < self:
            if self.left is None:
                return None
            return self.left.find_child(node)

    def remove_child(self, node):
        if self == node:
            if not self.has_child():
                self.remove()
            elif not self.has_both_child():
                new_child = self.get_only_child()
                self.key = new_child.key
                self.props = new_child.props.copy()
                new_child.remove()
            else:
                new_child = self.right.find_smallest()
                self.key = new_child.key
                self.props = new_child.props.copy()
                new_child.remove()

        if node > self and bool(self.right):
            self.right.remove_child(node)
        if node < self and bool(self.left):
            self.left.remove_child(node)

    def __eq__(self, other):
        if other is not None:
            if isinstance(other, Node):
                return self.key == other.key
            else:
                return self.key == other
        return False

    def __lt__(self, other):
        if other is not None:
            if isinstance(other, Node):
                return self.key < other.key
            else:
                return self.key < other
        return False

    def __gt__(self, other):
        if other is not None:
            if isinstance(other, Node):
                return self.key > other.key
            else:
                return self.key > other
        return False

    def __str__(self):
        return f'[{self.key} -> L({self.left}) R({self.right})]'
