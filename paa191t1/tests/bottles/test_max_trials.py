import unittest
from hamcrest import (
    assert_that,
    equal_to
)
from paa191t1.bottles import max_trials


class TestBottlesMaxTrials(unittest.TestCase):

    assert_experiment_message = (
        'Bottles experiment max_height={}, '
        'test_bottles={} should use at most '
        '[{}] trials but used [{}].'
    )

    def assert_experiment(self, max_height, test_bottles, expected_max_trials):
        found_max_trials = max_trials(max_height, test_bottles)
        assert_that(
            found_max_trials,
            equal_to(expected_max_trials),
            TestBottlesMaxTrials.assert_experiment_message.format(
                max_height,
                test_bottles,
                expected_max_trials,
                found_max_trials
            )
        )

    def test_should_calculate_max_trials_for_each_experiment_rounding_the_result_for_two_bottles(self):
        self.assert_experiment(max_height=10, test_bottles=2, expected_max_trials=6)
        self.assert_experiment(max_height=100, test_bottles=2, expected_max_trials=20)
        self.assert_experiment(max_height=1000, test_bottles=2, expected_max_trials=63)
        self.assert_experiment(max_height=10000, test_bottles=2, expected_max_trials=200)
        self.assert_experiment(max_height=100000, test_bottles=2, expected_max_trials=632)
        self.assert_experiment(max_height=1000000, test_bottles=2, expected_max_trials=2000)

    def test_should_calculate_max_trials_for_each_experiment_rounding_the_result_for_three_bottles(self):
        self.assert_experiment(max_height=10, test_bottles=3, expected_max_trials=6)
        self.assert_experiment(max_height=100, test_bottles=3, expected_max_trials=14)
        self.assert_experiment(max_height=1000, test_bottles=3, expected_max_trials=30)
        self.assert_experiment(max_height=10000, test_bottles=3, expected_max_trials=65)
        self.assert_experiment(max_height=100000, test_bottles=3, expected_max_trials=139)
        self.assert_experiment(max_height=1000000, test_bottles=3, expected_max_trials=300)

    def test_should_calculate_max_trials_for_each_experiment_rounding_the_result_for_four_bottles(self):
        self.assert_experiment(max_height=10, test_bottles=4, expected_max_trials=7)
        self.assert_experiment(max_height=100, test_bottles=4, expected_max_trials=13)
        self.assert_experiment(max_height=1000, test_bottles=4, expected_max_trials=22)
        self.assert_experiment(max_height=10000, test_bottles=4, expected_max_trials=40)
        self.assert_experiment(max_height=100000, test_bottles=4, expected_max_trials=71)
        self.assert_experiment(max_height=1000000, test_bottles=4, expected_max_trials=126)
