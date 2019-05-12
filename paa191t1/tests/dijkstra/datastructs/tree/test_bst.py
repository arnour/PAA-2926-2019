from paa191t1.dijkstra.datastructs.tree import bst
from paa191t1.tests import TestBase
from hamcrest import (
    assert_that,
    equal_to,
)


class TestBST(TestBase):
    _SKIP = False

    def test_should_add_node_with_smaller_key_at_left(self):
        node = bst.Node(5)
        node.add_child(bst.Node(2))

        assert_that(node.right, equal_to(None))
        assert_that(node.left, equal_to(2))
        assert_that(node.left.parent, equal_to(node))

    def test_should_add_node_with_bigger_key_at_right(self):
        node = bst.Node(5)
        node.add_child(bst.Node(8))

        assert_that(node.left, equal_to(None))
        assert_that(node.right, equal_to(8))
        assert_that(node.right.parent, equal_to(node))

    def test_should_add_nodes(self):
        node = bst.Node(7)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(5))
        node.add_child(bst.Node(3))
        node.add_child(bst.Node(10))
        node.add_child(bst.Node(8))
        node.add_child(bst.Node(11))

        assert_that(node.left, equal_to(4))
        assert_that(node.left.left, equal_to(3))
        assert_that(node.left.right, equal_to(5))
        assert_that(node.left.left.left, equal_to(None))
        assert_that(node.left.left.right, equal_to(None))
        assert_that(node.left.right.left, equal_to(None))
        assert_that(node.left.right.right, equal_to(None))

        assert_that(node.left.parent, equal_to(node))
        assert_that(node.right.parent, equal_to(node))
        assert_that(node.left.left.parent, equal_to(4))
        assert_that(node.left.right.parent, equal_to(4))

        assert_that(node.right, equal_to(10))
        assert_that(node.right.left, equal_to(8))
        assert_that(node.right.right, equal_to(11))
        assert_that(node.right.left.left, equal_to(None))
        assert_that(node.right.left.right, equal_to(None))
        assert_that(node.right.right.left, equal_to(None))
        assert_that(node.right.right.right, equal_to(None))

        assert_that(node.left.parent, equal_to(node))
        assert_that(node.right.parent, equal_to(node))
        assert_that(node.left.left.parent, equal_to(4))
        assert_that(node.left.right.parent, equal_to(4))
        assert_that(node.right.left.parent, equal_to(10))
        assert_that(node.right.right.parent, equal_to(10))

    def test_should_NOT_find_node(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(6))

        found = node.find_child(bst.Node(49))

        assert_that(found, equal_to(None))

    def test_should_find_node_in_itself(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(6))

        found = node.find_child(bst.Node(5))

        assert_that(found, equal_to(node))

    def test_should_find_node_at_left(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(6))

        found = node.find_child(bst.Node(4))

        assert_that(found, equal_to(4))
        assert_that(found.right, equal_to(None))
        assert_that(found.left, equal_to(None))
        assert_that(found.parent, equal_to(node))

    def test_should_find_node_at_right(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(6))

        found = node.find_child(bst.Node(6))

        assert_that(found, equal_to(6))
        assert_that(found.right, equal_to(None))
        assert_that(found.left, equal_to(None))
        assert_that(found.parent, equal_to(node))

    def test_should_find_node_deeply(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(60))
        node.add_child(bst.Node(26))
        node.add_child(bst.Node(16))
        node.add_child(bst.Node(6))
        node.add_child(bst.Node(3))
        node.add_child(bst.Node(100))

        found = node.find_child(bst.Node(6))

        assert_that(found, equal_to(6))
        assert_that(found.right, equal_to(None))
        assert_that(found.left, equal_to(None))
        assert_that(found.parent, equal_to(16))
        assert_that(found.parent.parent, equal_to(26))
        assert_that(found.parent.parent.parent, equal_to(60))
        assert_that(found.parent.parent.parent.parent, equal_to(5))

    def test_should_find_smallest(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(60))
        node.add_child(bst.Node(26))
        node.add_child(bst.Node(16))
        node.add_child(bst.Node(6))
        node.add_child(bst.Node(3))
        node.add_child(bst.Node(100))

        assert_that(node.find_smallest(), equal_to(3))
        assert_that(node.right.find_smallest(), equal_to(6))

    def test_node_with_both_child_has_child(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(6))

        node.has_child()

        assert_that(node.has_child(), equal_to(True))
        assert_that(node.has_both_child(), equal_to(True))

    def test_node_with_only_left_child_has_child(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))

        node.has_child()

        assert_that(node.has_child(), equal_to(True))
        assert_that(node.has_both_child(), equal_to(False))
        assert_that(node.get_only_child(), equal_to(4))

    def test_node_with_only_right_child_has_child(self):
        node = bst.Node(5)
        node.add_child(bst.Node(8))

        node.has_child()

        assert_that(node.has_child(), equal_to(True))
        assert_that(node.has_both_child(), equal_to(False))
        assert_that(node.get_only_child(), equal_to(8))

    def test_node_has_no_child(self):
        node = bst.Node(5)

        node.has_child()

        assert_that(node.has_child(), equal_to(False))
        assert_that(node.has_both_child(), equal_to(False))

    def test_left_node_is_left_child(self):
        node = bst.Node(5)
        node2 = bst.Node(4)
        node.add_child(node2)

        assert_that(node2.is_left_child(), equal_to(True))
        assert_that(node.left.is_left_child(), equal_to(True))

    def test_right_node_is_not_left_child(self):
        node = bst.Node(5)
        node2 = bst.Node(6)
        node.add_child(node2)

        assert_that(node2.is_left_child(), equal_to(False))
        assert_that(node.right.is_left_child(), equal_to(False))

    def test_remove_child_with_no_child(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(6))

        node.remove_child(bst.Node(4))

        assert_that(node.left, equal_to(None))
        assert_that(node.right, equal_to(6))
        assert_that(node.right.parent, equal_to(5))

    def test_remove_child_with_only_one_child(self):
        node = bst.Node(5)
        node.add_child(bst.Node(4))
        node.add_child(bst.Node(6))
        node.add_child(bst.Node(3))

        node.remove_child(bst.Node(4))

        assert_that(node.left, equal_to(3))
        assert_that(node.right, equal_to(6))
        assert_that(node.left.parent, equal_to(5))
        assert_that(node.right.parent, equal_to(5))

    def test_remove_child_with_both_child(self):
        node = bst.Node(8)
        node2 = bst.Node(6)
        node3 = bst.Node(7)
        node4 = bst.Node(5)
        node5 = bst.Node(1)
        node6 = bst.Node(9)
        node.add_child(node2)
        node.add_child(node3)
        node.add_child(node4)
        node.add_child(node5)
        node.add_child(node6)

        node.remove_child(bst.Node(6))

        assert_that(node.left, equal_to(7))
        assert_that(node.right, equal_to(9))

        assert_that(node.right.parent, equal_to(8))
        assert_that(node.left.left, equal_to(5))
        assert_that(node.left.left.left, equal_to(1))

        assert_that(node.left.parent, equal_to(8))
        assert_that(node.left.left.parent, equal_to(7))
        assert_that(node.left.left.left.parent, equal_to(5))
