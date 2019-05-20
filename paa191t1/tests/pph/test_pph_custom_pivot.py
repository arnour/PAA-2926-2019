from paa191t1.pph.pph_median import pph_median
from paa191t1.tests.pph import TestPPH
from paa191t1.pph.utils import custom_pivot


class TestPPHCustomPivot(TestPPH):

    _SKIP = True

    def setUp(self):
        self.pph = pph_median
        self.pivot = custom_pivot
