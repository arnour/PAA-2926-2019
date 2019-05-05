from hamcrest import (
    assert_that,
    has_length,
    equal_to
)
import math
from paa191t1.dijkstra.datastructs.vector import Vector


def create_vector(number_of_nodes=4):
    return Vector()(nodes=range(number_of_nodes))


def test_should_smallest_distance_init_all_nodes_distance_with_infinity():
    vector = create_vector(number_of_nodes=4)

    assert_that(vector.values, has_length(4))
    assert_that(vector.values[0], equal_to(math.inf))
    assert_that(vector.values[1], equal_to(math.inf))
    assert_that(vector.values[2], equal_to(math.inf))
    assert_that(vector.values[3], equal_to(math.inf))


def test_should_distance_vector_remove_node_with_smallest_distance_at_time_equal_distances():
    vector = create_vector(number_of_nodes=4)

    assert_that(vector.pop(), equal_to((3, math.inf)))
    assert_that(vector.pop(), equal_to((2, math.inf)))
    assert_that(vector.pop(), equal_to((1, math.inf)))
    assert_that(vector.pop(), equal_to((0, math.inf)))


def test_should_distance_vector_remove_node_with_smallest_distance_at_time_different_distances():
    vector = create_vector(number_of_nodes=4)

    vector.update(0, 0)
    vector.update(1, 22)
    vector.update(2, 990)
    vector.update(3, 2)

    assert_that(vector.pop(), equal_to((0, 0)))
    assert_that(vector.pop(), equal_to((3, 2)))
    assert_that(vector.pop(), equal_to((1, 22)))
    assert_that(vector.pop(), equal_to((2, 990)))


def test_should_distance_vector_return_false_when_it_has_popped_all_nodes():
    vector = create_vector(number_of_nodes=4)

    assert_that(vector.has_nodes_to_visit(), equal_to(True))

    vector.pop()
    assert_that(vector.has_nodes_to_visit(), equal_to(True))

    vector.pop()
    assert_that(vector.has_nodes_to_visit(), equal_to(True))

    vector.pop()
    assert_that(vector.has_nodes_to_visit(), equal_to(True))

    vector.pop()
    assert_that(vector.has_nodes_to_visit(), equal_to(False))


def test_should_distance_vector_return_node_distance():
    vector = create_vector(number_of_nodes=2)

    assert_that(vector.value(0), equal_to(math.inf))
    assert_that(vector.value(1), equal_to(math.inf))

    vector.update(0, 4)
    vector.update(1, 7)

    assert_that(vector.value(0), equal_to(4))
    assert_that(vector.value(1), equal_to(7))
