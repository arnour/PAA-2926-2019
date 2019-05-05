from hamcrest import (
    assert_that,
    has_length,
    equal_to
)
import math
from paa191t1.dijkstra.datastructs.buckets import Buckets


def create_bucket(number_of_nodes=4):
    return Buckets()(nodes=list(range(number_of_nodes)))


def test_should_smallest_distance_init_all_nodes_distance_with_infinity():
    bucket = create_bucket(number_of_nodes=4)

    assert_that(bucket.values, has_length(4))
    assert_that(bucket.values[0], equal_to(math.inf))
    assert_that(bucket.values[1], equal_to(math.inf))
    assert_that(bucket.values[2], equal_to(math.inf))
    assert_that(bucket.values[3], equal_to(math.inf))


def test_should_distance_bucket_remove_node_with_smallest_distance_at_time_equal_distances():
    bucket = create_bucket(number_of_nodes=4)
    assert_that(bucket.pop(), equal_to((3, math.inf)))
    assert_that(bucket.pop(), equal_to((2, math.inf)))
    assert_that(bucket.pop(), equal_to((1, math.inf)))
    assert_that(bucket.pop(), equal_to((0, math.inf)))


def test_should_distance_bucket_remove_node_with_smallest_distance_at_time_different_distances():
    bucket = create_bucket(number_of_nodes=4)

    bucket.update(0, 0)
    bucket.update(1, 22)
    bucket.update(2, 990)
    bucket.update(3, 2)

    assert_that(bucket.pop(), equal_to((0, 0)))
    assert_that(bucket.pop(), equal_to((3, 2)))
    assert_that(bucket.pop(), equal_to((1, 22)))
    assert_that(bucket.pop(), equal_to((2, 990)))


def test_should_distance_bucket_return_false_when_it_has_popped_all_nodes():
    bucket = create_bucket(number_of_nodes=4)
    assert_that(bucket.has_nodes_to_visit(), equal_to(True))

    bucket.pop()
    assert_that(bucket.has_nodes_to_visit(), equal_to(True))

    bucket.pop()
    assert_that(bucket.has_nodes_to_visit(), equal_to(True))

    bucket.pop()
    assert_that(bucket.has_nodes_to_visit(), equal_to(True))

    bucket.pop()
    assert_that(bucket.has_nodes_to_visit(), equal_to(False))


def test_should_distance_bucket_return_node_distance():
    bucket = create_bucket(number_of_nodes=2)

    assert_that(bucket.value(0), equal_to(math.inf))
    assert_that(bucket.value(1), equal_to(math.inf))

    bucket.update(0, 4)
    bucket.update(1, 7)

    assert_that(bucket.value(0), equal_to(4))
    assert_that(bucket.value(1), equal_to(7))
