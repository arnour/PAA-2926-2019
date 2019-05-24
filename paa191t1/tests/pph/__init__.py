from hamcrest import (
    assert_that,
    equal_to,
    close_to,
    empty
)
from paa191t1.pph import Pair
from paa191t1.tests import TestBase


class TestPPH(TestBase):

    _SKIP = True

    def setUp(self):
        self.pph = lambda n, t, p: None

    def test_should_define_s(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16)
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(6, 6),
                Pair(2, 5),
                Pair(3, 8)
            ])
        )

        assert_that(s.r, close_to(0.36, delta=0.05))

        s = self.pph(n, Pair(4, 8))

        assert_that(
            s.values,
            equal_to([
                Pair(6, 6)
            ])
        )

        assert_that(s.r, close_to(0.71, delta=0.05))

    # def test_should_define_s_empty(self):
    #     n = [
    #         Pair(2, 5),
    #         Pair(1, 3),
    #         Pair(3, 8),
    #         Pair(6, 6),
    #         Pair(5, 16)
    #     ]

    #     s = self.pph(n, Pair(100, 10))

    #     assert_that(s.values, empty())
    #     assert_that(s.r, equal_to(10.0))

    #     n = [
    #         Pair(2, 15),
    #         Pair(3, 10),
    #         Pair(8, 19),
    #         Pair(3, 5),
    #         Pair(2, 9),
    #         Pair(6, 12)
    #     ]

    #     s = self.pph(n, Pair(6, 6))

    #     assert_that(s.values, empty())
    #     assert_that(s.r, equal_to(1.0))

    def test_should_add_all_n_in_s_and_n_is_sorted(self):
        n = [
            Pair(4, 3),
            Pair(7, 5),
            Pair(6, 4),
            Pair(8, 5),
            Pair(5, 3),
            Pair(9, 5)
        ]

        s = self.pph(n, Pair(1, 5))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(9, 5),
                Pair(5, 3),
                Pair(8, 5),
                Pair(6, 4),
                Pair(7, 5)
            ])
        )

        assert_that(s.r, close_to(1.33, delta=0.05))

        n = [Pair(i * i, i) for i in range(1, 150)]

        s = self.pph(n, Pair(15, 3))
        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(22201, 149),
                Pair(21904, 148)
            ])
        )

        assert_that(s.r, close_to(147.06, delta=0.01))

    def test_should_add_all_n_in_s_and_n_is_sorted_reversed(self):
        n = [
            Pair(9, 5),
            Pair(5, 3),
            Pair(8, 5),
            Pair(6, 4),
            Pair(7, 5),
            Pair(4, 3)
        ]

        s = self.pph(n, Pair(1, 5))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(9, 5),
                Pair(5, 3),
                Pair(8, 5),
                Pair(6, 4),
                Pair(7, 5)
            ])
        )

        assert_that(s.r, close_to(1.33, delta=0.05))

    def test_should_add_all_n_in_s_and_n_is_NOT_sorted(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16)
        ]

        s = self.pph(n, Pair(10, 100))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(6, 6),
                Pair(2, 5),
                Pair(3, 8),
                Pair(1, 3),
                Pair(5, 16)
            ])
        )

        assert_that(s.r, close_to(0.19, delta=0.05))

    def test_should_works_removing_all_elements_except_one(self):
        n = [
            Pair(5, 16),
            Pair(2, 5),
            Pair(1, 3),
            Pair(16, 16),
            Pair(3, 9),
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            s.values,
            equal_to([
                Pair(16, 16)
            ])
        )

        assert_that(s.r, close_to(0.54, delta=0.05))

    def test_should_works_removing_all_elements_except_one2(self):
        n = [
            Pair(5, 16),
            Pair(2, 5),
            Pair(1, 2),
            Pair(16, 16),
            Pair(3, 9),
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            s.values,
            equal_to([
                Pair(16, 16)
            ])
        )

        assert_that(s.r, close_to(0.54, delta=0.05))

    def test_should_works_with_poggi_trials(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16),
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            sorted(s.values, key=lambda x: x.r, reverse=True),
            equal_to([
                Pair(6, 6),
                Pair(2, 5),
                Pair(3, 8)
            ])
        )

        assert_that(s.r, close_to(0.36, delta=0.01))
