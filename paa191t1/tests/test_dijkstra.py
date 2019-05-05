from hamcrest import (
    assert_that,
    has_entries,
    has_length,
    empty
)
import math
import networkx as nx
from paa191t1.dijkstra.structs import graph, vector
from paa191t1.dijkstra import dijkstra


def test_should_return_shortest_distances_and_predecessors_for_equally_weighted_graph_with_one_path():

    all_structs = [vector.Vector()]

    for strct in all_structs:

        dg = nx.DiGraph()
        dg.add_weighted_edges_from([(0, 1, 1), (1, 2, 1), (2, 3, 1)])

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=0, distance_struct=strct)

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


def test_should_return_shortest_distances_and_predecessors_for_equally_weighted_graph_with_many_paths():

    all_structs = [vector.Vector()]

    for strct in all_structs:

        dg = nx.DiGraph()
        dg.add_weighted_edges_from([(0, 1, 1), (0, 2, 1), (1, 3, 1), (2, 3, 1)])

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=0, distance_struct=strct)

        assert_that(distances, has_length(4))
        assert_that(
            distances,
            has_entries({0: 0, 1: 1, 2: 1, 3: 2})
        )

        assert_that(predecessors, has_length(3))
        assert_that(
            predecessors,
            has_entries({1: 0, 2: 0, 3: 2})
        )


def test_should_return_shortest_distances_and_predecessors_for_differently_weighted_graph_with_many_paths():

    all_structs = [vector.Vector()]

    for strct in all_structs:

        dg = nx.DiGraph()
        dg.add_weighted_edges_from([(0, 1, 4), (1, 3, 1), (3, 5, 1)])
        dg.add_weighted_edges_from([(0, 2, 1), (2, 4, 1), (4, 5, 1)])

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=0, distance_struct=strct)

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


def test_should_return_shortest_distances_and_predecessors_for_graph_with_connected_components():

    all_structs = [vector.Vector()]

    for strct in all_structs:

        dg = nx.DiGraph()
        dg.add_weighted_edges_from([(1, 3, 1), (3, 5, 1), (5, 7, 1)])
        dg.add_weighted_edges_from([(0, 2, 2), (2, 4, 2), (4, 6, 2)])

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=1, distance_struct=strct)

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


def test_should_return_shortest_distances_and_predecessors_for_graph_with_unreachble_nodes():

    all_structs = [vector.Vector()]

    for strct in all_structs:

        dg = nx.DiGraph()
        dg.add_node(1)
        dg.add_node(2)
        dg.add_node(3)

        distances, predecessors = dijkstra(graph=graph.Graph(dg), source_node=1, distance_struct=strct)

        assert_that(distances, has_length(3))
        assert_that(
            distances,
            has_entries({1: 0, 2: math.inf, 3: math.inf})
        )

        assert_that(predecessors, empty())
