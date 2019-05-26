from paa191t1.pph.pph_n_log_n import pph_n_lg_n
from paa191t1.tests.pph import TestPPHBase


class TestPPHNLGN(TestPPHBase):

    def setUp(self):
        self.pph = pph_n_lg_n
