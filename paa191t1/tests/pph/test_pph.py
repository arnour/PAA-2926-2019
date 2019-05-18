import unittest
from hamcrest import (
    assert_that,
    equal_to,
    close_to
)
from paa191t1.pph import pph, Pair


class TestPPH(unittest.TestCase):

    def test_should_define_s(self):
        n = [
            Pair.of(2, 5),
            Pair.of(1, 3),
            Pair.of(3, 8),
            Pair.of(6, 6),
            Pair.of(5, 16)
        ]

        s = pph(n, Pair.of(2, 17))

        assert_that(
            s.values,
            equal_to([
                Pair.of(2, 5),
                Pair.of(3, 8),
                Pair.of(6, 6),
            ])
        )

        assert_that(s.r, close_to(0.36, delta=0.05))
