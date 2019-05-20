from paa191t1.pph.pph_median import pph_median
from paa191t1.tests.pph import TestPPH
from paa191t1.pph.utils import median_of_medians


class TestPPHMedian(TestPPH):

    _SKIP = False

    def setUp(self):
        self.pph = pph_median
        self.pivot = median_of_medians
