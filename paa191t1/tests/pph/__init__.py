from hamcrest import (
    assert_that,
    equal_to,
    close_to
)
from paa191t1.pph import Pair
from paa191t1.tests import TestBase


class TestPPH(TestBase):

    _SKIP = True

    def setUp(self):
        self.pph = lambda n, t: None

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
