from paa191t1.dijkstra.datastructs.tree import DistanceNode, TreeTraversal
from paa191t1.dijkstra.datastructs.tree.avl import AVLNode as Node
from paa191t1.tests import TestBase
from hamcrest import (
    assert_that,
    equal_to,
    greater_than,
    less_than
)


class TestDistanceNode(TestBase):

    _SKIP = False

    def test_node_should_be_equal(self):
        node1 = DistanceNode(vertex=3, distance=4)
        node2 = DistanceNode(vertex=3, distance=4)

        assert_that(node1, equal_to(node2))

    def test_node_should_be_gt_using_vertex_as_lexical_diference(self):
        node1 = DistanceNode(vertex=4, distance=4)
        node2 = DistanceNode(vertex=3, distance=4)

        assert_that(node1, greater_than(node2))

    def test_node_should_be_gt_if_it_has_greater_distance(self):
        node1 = DistanceNode(vertex=4, distance=4)
        node2 = DistanceNode(vertex=3, distance=8)

        assert_that(node2, greater_than(node1))

    def test_node_should_be_lt_using_vertex_as_lexical_diference(self):
        node1 = DistanceNode(vertex=4, distance=4)
        node2 = DistanceNode(vertex=3, distance=4)

        assert_that(node2, less_than(node1))

    def test_node_should_be_lt_if_it_has_lesser_distance(self):
        node1 = DistanceNode(vertex=4, distance=4)
        node2 = DistanceNode(vertex=3, distance=8)

        assert_that(node1, less_than(node2))


class TestTreeTraversal(TestBase):

    _SKIP = False

    def test_should_walk_through_tree_in_order(self):
        root = Node(None, DistanceNode(8, 1))
        root.left = Node(root, DistanceNode(6, 2))
        root.right = Node(root, DistanceNode(10, 3))

        nodes = TreeTraversal().inorder(root)

        assert_that(
            nodes,
            equal_to([(6, 2), (8, 1), (10, 3)])
        )
