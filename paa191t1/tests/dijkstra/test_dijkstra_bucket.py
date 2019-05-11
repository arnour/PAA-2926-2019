from paa191t1.dijkstra.datastructs.buckets import Buckets
from paa191t1.tests.dijkstra.test_dijkstra import TestDijkstraBase


class TestDijkstraBuckets(TestDijkstraBase):

    _SKIP = False

    def setUp(self):
        self.struct = Buckets()
