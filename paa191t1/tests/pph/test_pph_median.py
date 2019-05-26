from paa191t1.pph.pph_median import pph_median
from paa191t1.tests.pph import TestPPH


class TestPPHMedian(TestPPH):

    def setUp(self):
        self.pph = pph_median
