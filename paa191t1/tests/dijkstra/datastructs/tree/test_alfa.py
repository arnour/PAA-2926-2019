from paa191t1.dijkstra.datastructs.tree.alfa import AlfaNode as Node, Alfa as Tree
from paa191t1.tests import TestBase
from hamcrest import (
    assert_that,
    equal_to
)


class TestAlfaBalancedNode(TestBase):

    def test_balanced_node_should_return_correct_sizes(self):

        root = Node(None, 7)

        root.insert(Node(root, 4))
        root.insert(Node(root, 5))
        root.insert(Node(root, 3))

        root.insert(Node(root, 10))
        root.insert(Node(root, 9))
        root.insert(Node(root, 11))

        assert_that(root.size, equal_to(7))
        assert_that(root.left_size, equal_to(3))
        assert_that(root.right_size, equal_to(3))

    def test_balanced_node_should_have_only_balanced_children(self):
        root = Node(None, 7)

        root.insert(Node(root, 5))
        root.insert(Node(root, 10))

        root.insert(Node(root, 4))
        root.insert(Node(root, 6))

        root.insert(Node(root, 9))
        root.insert(Node(root, 11))

        assert_that(root.is_balanced(), equal_to(True))
        assert_that(root.left.is_balanced(), equal_to(True))
        assert_that(root.left.left.is_balanced(), equal_to(True))
        assert_that(root.left.right.is_balanced(), equal_to(True))

        assert_that(root.right.is_balanced(), equal_to(True))
        assert_that(root.right.left.is_balanced(), equal_to(True))
        assert_that(root.right.right.is_balanced(), equal_to(True))


class TestAlfaUnbalancedNode(TestBase):

    def test_unbalanced_node_should_return_correct_sizes(self):

        root = Node(None, 7)

        root.insert(Node(root, 4))
        root.insert(Node(root, 5))
        root.insert(Node(root, 3))

        assert_that(root.size, equal_to(4))
        assert_that(root.left_size, equal_to(3))
        assert_that(root.right_size, equal_to(0))

    def test_unbalanced_node_could_have_balanced_children(self):
        root = Node(None, 7)

        root.insert(Node(root, 8))
        root.insert(Node(root, 9))
        root.insert(Node(root, 10))

        assert_that(root.is_balanced(), equal_to(False))
        assert_that(root.right.is_balanced(), equal_to(False))
        assert_that(root.right.right.is_balanced(), equal_to(True))


class TestAlfaTreeInsertion(TestBase):

    def test_should_rebuild_tree(self):
        tree = Tree()

        tree.insert(7)
        tree.insert(8)
        tree.insert(9)

        assert_that(tree.root, equal_to(8))
        assert_that(tree.root.left, equal_to(7))
        assert_that(tree.root.right, equal_to(9))

    def test_should_rebuild_subtree(self):
        tree = Tree()

        tree.insert(10)

        tree.insert(6)
        tree.insert(13)

        tree.insert(5)
        tree.insert(11)

        tree.insert(7)
        tree.insert(14)

        assert_that(tree.root, equal_to(10))
        assert_that(tree.is_balanced, equal_to(True))
        assert_that(tree.root.left, equal_to(6))
        assert_that(tree.root.right, equal_to(13))

        tree.insert(15)
        tree.insert(16)
        tree.insert(17)

        assert_that(tree.root, equal_to(11))
        assert_that(tree.is_balanced, equal_to(True))
        assert_that(tree.root.left, equal_to(6))
        assert_that(tree.root.right, equal_to(15))


class TestAlfaTreeDeletion(TestBase):

    def test_should_rebuild_subtree(self):
        tree = Tree()

        tree.insert(10)

        tree.insert(6)
        tree.insert(13)

        tree.insert(5)
        tree.insert(11)

        tree.insert(7)
        tree.insert(14)

        assert_that(tree.root, equal_to(10))
        assert_that(tree.is_balanced, equal_to(True))
        assert_that(tree.root.left, equal_to(6))
        assert_that(tree.root.right, equal_to(13))

        tree.insert(15)
        tree.insert(16)
        tree.insert(18)
        tree.insert(17)
        tree.insert(19)

        assert_that(tree.root, equal_to(13))
        assert_that(tree.is_balanced, equal_to(True))
        assert_that(tree.root.left, equal_to(7))
        assert_that(tree.root.right, equal_to(16))

        tree.delete(16)
        tree.delete(18)
        tree.delete(19)
        tree.delete(17)

        assert_that(tree.root, equal_to(11))
        assert_that(tree.is_balanced, equal_to(True))
        assert_that(tree.root.left, equal_to(6))
        assert_that(tree.root.right, equal_to(14))

    def test_should_rebuild_subtree_removing_roots(self):
        tree = Tree()

        tree.insert(10)

        tree.insert(6)
        tree.insert(13)

        tree.insert(5)
        tree.insert(11)

        tree.insert(7)
        tree.insert(14)

        assert_that(tree.root, equal_to(10))
        assert_that(tree.is_balanced, equal_to(True))
        assert_that(tree.root.left, equal_to(6))
        assert_that(tree.root.right, equal_to(13))

        tree.insert(15)
        tree.insert(16)
        tree.insert(18)
        tree.insert(17)
        tree.insert(19)

        assert_that(tree.root, equal_to(13))
        assert_that(tree.is_balanced, equal_to(True))
        assert_that(tree.root.left, equal_to(7))
        assert_that(tree.root.right, equal_to(16))

        tree.delete(13)
        tree.delete(14)
        tree.delete(15)
        tree.delete(11)
        tree.delete(16)
        tree.delete(10)
        tree.delete(17)
        tree.delete(7)
        tree.delete(18)
        tree.delete(6)
        tree.delete(19)
        tree.delete(5)

        assert_that(tree.root, equal_to(None))
