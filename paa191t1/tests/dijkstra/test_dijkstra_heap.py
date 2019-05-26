from paa191t1.dijkstra.datastructs.heap import Heap
from paa191t1.tests.dijkstra.test_dijkstra import TestDijkstraBase


class TestDijkstraHeap(TestDijkstraBase):

    def setUp(self):
        self.struct = Heap()
