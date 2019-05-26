from hamcrest import (
    assert_that,
    has_entries,
    has_length,
    any_of,
    empty
)
import math
import networkx as nx
from paa191t1.tests import TestBase
from paa191t1.dijkstra.datastructs import graph, DijkstraDistance
from paa191t1.dijkstra import dijkstra


class TestDijkstraBase(TestBase):

    def setUp(self):
        self.struct = DijkstraDistance()

    def test_should_return_shortest_distances_and_predecessors_for_equally_weighted_graph_with_one_path(self):

        dg = nx.DiGraph()
        dg.add_weighted_edges_from([(0, 1, 1), (1, 2, 1), (2, 3, 1)])

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=0, distance_struct=self.struct)

        assert_that(distances, has_length(4))
        assert_that(
            distances,
            has_entries({0: 0, 1: 1, 2: 2, 3: 3})
        )

        assert_that(predecessors, has_length(3))
        assert_that(
            predecessors,
            has_entries({1: 0, 2: 1, 3: 2})
        )

    def test_should_return_shortest_distances_and_predecessors_for_equally_weighted_graph_with_many_paths(self):

        dg = nx.DiGraph()
        dg.add_weighted_edges_from([(0, 1, 1), (0, 2, 1), (1, 3, 1), (2, 3, 1)])

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=0, distance_struct=self.struct)

        assert_that(distances, has_length(4))
        assert_that(
            distances,
            has_entries({0: 0, 1: 1, 2: 1, 3: 2})
        )

        assert_that(predecessors, has_length(3))
        assert_that(
            predecessors,
            any_of(has_entries({1: 0, 2: 0, 3: 2}), has_entries({1: 0, 2: 0, 3: 1}))
        )

    def test_should_return_shortest_distances_and_predecessors_for_differently_weighted_graph_with_many_paths(self):

        dg = nx.DiGraph()
        dg.add_weighted_edges_from([(0, 1, 4), (1, 3, 1), (3, 5, 1)])
        dg.add_weighted_edges_from([(0, 2, 1), (2, 4, 1), (4, 5, 1)])

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=0, distance_struct=self.struct)

        assert_that(distances, has_length(6))
        assert_that(
            distances,
            has_entries({0: 0, 1: 4, 2: 1, 3: 5, 4: 2, 5: 3})
        )

        assert_that(predecessors, has_length(5))
        assert_that(
            predecessors,
            has_entries({1: 0, 2: 0, 3: 1, 4: 2, 5: 4})
        )

    def test_should_return_shortest_distances_and_predecessors_for_graph_with_connected_components(self):

        dg = nx.DiGraph()
        dg.add_weighted_edges_from([(1, 3, 1), (3, 5, 1), (5, 7, 1)])
        dg.add_weighted_edges_from([(0, 2, 2), (2, 4, 2), (4, 6, 2)])

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=1, distance_struct=self.struct)

        assert_that(distances, has_length(8))
        assert_that(
            distances,
            has_entries({0: math.inf, 1: 0, 2: math.inf, 3: 1, 4: math.inf, 5: 2, 6: math.inf, 7: 3})
        )

        assert_that(predecessors, has_length(3))
        assert_that(
            predecessors,
            has_entries({3: 1, 5: 3, 7: 5})
        )

    def test_should_return_shortest_distances_and_predecessors_for_graph_with_unreachble_nodes(self):

        dg = nx.DiGraph()
        dg.add_node(0)
        dg.add_node(1)
        dg.add_node(2)

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=0, distance_struct=self.struct)

        assert_that(distances, has_length(3))
        assert_that(
            distances,
            has_entries({0: 0, 1: math.inf, 2: math.inf})
        )

        assert_that(predecessors, empty())
