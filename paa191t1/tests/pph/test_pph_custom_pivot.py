from paa191t1.pph.pph_custom_pivot import pph_custom_pivot
from paa191t1.tests.pph import TestPPH


class TestPPHCustomPivot(TestPPH):

    _SKIP = False

    def setUp(self):
        self.pph = pph_custom_pivot
