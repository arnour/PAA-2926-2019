from paa191t1.pph import pph_median, Pair
from paa191t1.tests.pph import TestPPH
from hamcrest import (
    assert_that,
    equal_to,
    close_to
)


class TestPPHMedian(TestPPH):

    _SKIP = False

    def setUp(self):
        self.pph = pph_median

    def test_hell(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 9),
            Pair(5, 16),
            Pair(16, 16),
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            s.values,
            equal_to([
                Pair(16, 16)
            ])
        )

        assert_that(s.r, close_to(0.54, delta=0.05))

    def test_hell2(self):
        n = [
            Pair(2, 5),
            Pair(1, 3),
            Pair(3, 8),
            Pair(6, 6),
            Pair(5, 16),
        ]

        s = self.pph(n, Pair(2, 17))

        assert_that(
            s.values,
            equal_to([
                Pair(2, 5),
                Pair(6, 6),
                Pair(3, 8)
            ])
        )

        assert_that(s.r, close_to(0.36, delta=0.01))
