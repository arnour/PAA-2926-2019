from paa191t1.bottles.bottles_binary import bottles
from paa191t1.tests.bottles.test_bottles_base import *
from hamcrest import (
    assert_that,
    equal_to
)


class TestBottlesBinaryK2(TestBottlesBaseK2):

    def setUp(self):
        self.bottles = bottles

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="000001")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 2, 2))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="111111")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 27, 2))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="100000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 22, 2))
        )

    def test_should_find_break_point_at_median_position2(self):
        found, used_trials, used_bottles = self.bottles(max_height=20, test_bottles=self.K, break_point="10000000000000000000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 262164, 2))
        )


class TestBottlesBinaryK3(TestBottlesBaseK3):

    def setUp(self):
        self.bottles = bottles

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="000001")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 3, 3))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="111111")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 24, 3))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="100000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 12, 3))
        )

    def test_should_find_break_point_at_median_position2(self):
        found, used_trials, used_bottles = self.bottles(max_height=20, test_bottles=self.K, break_point="10000000000000000000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 40, 3))
        )


class TestBottlesBinaryK4(TestBottlesBaseK4):

    def setUp(self):
        self.bottles = bottles

    def test_should_find_break_point_at_first_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="000001")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 4, 4))
        )

    def test_should_find_break_point_at_last_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="111111")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 24, 4))
        )

    def test_should_find_break_point_at_median_position(self):
        found, used_trials, used_bottles = self.bottles(max_height=6, test_bottles=self.K, break_point="100000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 13, 4))
        )

    def test_should_find_break_point_at_median_position2(self):
        found, used_trials, used_bottles = self.bottles(max_height=20, test_bottles=self.K, break_point="10000000000000000000")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 41, 4))
        )

    def test_should_find_break_point_at_median_position3_worse_case(self):
        found, used_trials, used_bottles = self.bottles(max_height=20, test_bottles=self.K, break_point="10100100100101001010")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 398, 4))
        )

class TestBottlesBinaryK16(TestBottlesBaseK16):

    def setUp(self):
        self.bottles = bottles

    def test_should_find_break_point_at_median_position3_worse_case(self):
        found, used_trials, used_bottles = self.bottles(max_height=32, test_bottles=self.K, break_point="00111101001110011100000000100110")
        assert_that(
            (found, used_trials, used_bottles),
            equal_to((True, 305, 16))
        )
