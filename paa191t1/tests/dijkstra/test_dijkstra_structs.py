import math
from unittest import skip, TestCase
from hamcrest import (
    assert_that,
    has_length,
    equal_to
)

from paa191t1.dijkstra.datastructs import DijkstraDistance


@skip("Base Class")
class TestStructsBase(TestCase):

    struct = DijkstraDistance()

    def create_struct(self, number_of_nodes=4):
        return self.struct(nodes=range(number_of_nodes))

    def test_should_smallest_distance_init_all_nodes_distance_with_infinity(self):
        struct = self.create_struct(number_of_nodes=4)

        assert_that(struct.values, has_length(4))
        assert_that(struct.values[0], equal_to(math.inf))
        assert_that(struct.values[1], equal_to(math.inf))
        assert_that(struct.values[2], equal_to(math.inf))
        assert_that(struct.values[3], equal_to(math.inf))

    def test_should_distance_struct_remove_node_with_smallest_distance_at_time_equal_distances(self):
        struct = self.create_struct(number_of_nodes=4)

        assert_that(struct.pop(), equal_to((3, math.inf)))
        assert_that(struct.pop(), equal_to((2, math.inf)))
        assert_that(struct.pop(), equal_to((1, math.inf)))
        assert_that(struct.pop(), equal_to((0, math.inf)))

    def test_should_distance_struct_remove_node_with_smallest_distance_at_time_different_distances(self):
        struct = self.create_struct(number_of_nodes=4)

        struct.update(0, 0)
        struct.update(1, 22)
        struct.update(2, 990)
        struct.update(3, 2)

        assert_that(struct.pop(), equal_to((0, 0)))
        assert_that(struct.pop(), equal_to((3, 2)))
        assert_that(struct.pop(), equal_to((1, 22)))
        assert_that(struct.pop(), equal_to((2, 990)))

    def test_should_distance_struct_return_false_when_it_has_popped_all_nodes(self):
        struct = self.create_struct(number_of_nodes=4)

        assert_that(struct.has_nodes_to_visit(), equal_to(True))

        struct.pop()
        assert_that(struct.has_nodes_to_visit(), equal_to(True))

        struct.pop()
        assert_that(struct.has_nodes_to_visit(), equal_to(True))

        struct.pop()
        assert_that(struct.has_nodes_to_visit(), equal_to(True))

        struct.pop()
        assert_that(struct.has_nodes_to_visit(), equal_to(False))

    def test_should_distance_struct_return_node_distance(self):
        struct = self.create_struct(number_of_nodes=2)

        assert_that(struct.value(0), equal_to(math.inf))
        assert_that(struct.value(1), equal_to(math.inf))

        struct.update(0, 4)
        struct.update(1, 7)

        assert_that(struct.value(0), equal_to(4))
        assert_that(struct.value(1), equal_to(7))
