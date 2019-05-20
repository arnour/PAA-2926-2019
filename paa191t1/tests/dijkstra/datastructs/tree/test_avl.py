from paa191t1.dijkstra.datastructs.tree.avl import AVL as Tree
from paa191t1.tests import TestBase
from hamcrest import (
    assert_that,
    equal_to
)


class TestAVL(TestBase):

    _SKIP = False

    def test_should_build_avl_tree(self):

        tree = Tree()

        for i in range(5):
            tree.insert(i)

        assert_that(tree.root.height, equal_to(2))
        assert_that(tree.root, equal_to(1))
        assert_that(tree.root.left, equal_to(0))
        assert_that(tree.root.right, equal_to(3))
        assert_that(tree.root.right.left, equal_to(2))
        assert_that(tree.root.right.right, equal_to(4))

    def test_should_build_avl_tree_with_height_five(self):

        tree = Tree()

        for i in range(32):
            tree.insert(i)

        assert_that(tree.root.height, equal_to(5))
        assert_that(tree.root, equal_to(15))

    def test_should_remove_left_leaf_in_avl_tree(self):

        tree = Tree()

        for i in range(5):
            tree.insert(i)

        tree.delete(2)

        assert_that(tree.root.height, equal_to(2))
        assert_that(tree.root, equal_to(1))
        assert_that(tree.root.left, equal_to(0))
        assert_that(tree.root.right, equal_to(3))
        assert_that(tree.root.right.left, equal_to(None))
        assert_that(tree.root.right.right, equal_to(4))

    def test_should_remove_right_leaf_in_avl_tree(self):

        tree = Tree()

        for i in range(5):
            tree.insert(i)

        tree.delete(4)

        assert_that(tree.root.height, equal_to(2))
        assert_that(tree.root, equal_to(1))
        assert_that(tree.root.left, equal_to(0))
        assert_that(tree.root.right, equal_to(3))
        assert_that(tree.root.right.left, equal_to(2))
        assert_that(tree.root.right.right, equal_to(None))

    def test_should_remove_right_node_with_only_right_child_in_avl_tree(self):

        tree = Tree()

        for i in range(6):
            tree.insert(i)

        tree.delete(4)

        assert_that(tree.root.height, equal_to(2))
        assert_that(tree.root, equal_to(3))
        assert_that(tree.root.left, equal_to(1))
        assert_that(tree.root.left.left, equal_to(0))
        assert_that(tree.root.left.right, equal_to(2))
        assert_that(tree.root.right, equal_to(5))

    def test_should_remove_right_node_with_only_left_child_in_avl_tree(self):

        tree = Tree()

        for i in range(7, 3, -1):
            tree.insert(i)

        tree.delete(5)

        assert_that(tree.root.height, equal_to(1))
        assert_that(tree.root, equal_to(6))
        assert_that(tree.root.left, equal_to(4))
        assert_that(tree.root.right, equal_to(7))

    def test_should_remove_node_with_both_children_in_avl_tree(self):

        tree = Tree()

        for i in range(1, 8):
            tree.insert(i)

        tree.delete(6)

        assert_that(tree.root.height, equal_to(2))
        assert_that(tree.root, equal_to(4))
        assert_that(tree.root.left, equal_to(2))
        assert_that(tree.root.left.left, equal_to(1))
        assert_that(tree.root.left.right, equal_to(3))
        assert_that(tree.root.right, equal_to(7))
        assert_that(tree.root.right.left, equal_to(5))
        assert_that(tree.root.right.right, equal_to(None))
