from unittest import TestCase
from paa191t1.pph import Pair
from paa191t1.pph.utils import median_of_medians, custom_pivot
from hamcrest import (
    assert_that,
    equal_to
)


class TestMedianOfMedians(TestCase):

    def test_should_find_median_number(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 5
        assert_that(
            median_of_medians(test_list),
            equal_to(expected)
        )

    def test_should_find_median_number_pair(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        expected = 5
        assert_that(
            median_of_medians(test_list),
            equal_to(expected)
        )

    def test_should_find_median_number_pair_without_order(self):
        test_list = [10, 2, 6, 8, 3, 5, 7, 4, 1]
        expected = 5
        assert_that(
            median_of_medians(test_list),
            equal_to(expected)
        )

    def test_should_find_median_number_with_more_than_10_numbers(self):
        test_list = [9, 11, 2, 6, 8, 3, 5, 7, 4, 1, 30, 28, 16, 40, 1000, 18, 74, 80]
        expected = 11
        assert_that(
            median_of_medians(test_list),
            equal_to(expected)
        )

    def test_should_find_median_with_repeated_numbers(self):
        test_list = [9, 9, 2, 6, 8, 3, 5, 7, 4, 1, 30, 28, 16, 40, 1000, 18, 74, 80]
        expected = 9
        assert_that(
            median_of_medians(test_list),
            equal_to(expected)
        )

    def test_should_find_custom_pivot_with_pairs_without_order(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16)
        ]
        expected = Pair(19, 55)
        a0 = 2
        b0 = 17
        assert_that(
            custom_pivot(n, 0, a0, b0),
            equal_to(expected)
        )
