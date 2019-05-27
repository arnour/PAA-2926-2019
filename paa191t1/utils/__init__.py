import os
import networkx as nx
from networkx.readwrite.edgelist import read_edgelist
from paa191t1.dijkstra.datastructs.graph import Graph


def load_graph(file, distance_struct):
    G = read_edgelist(file, nodetype=int, data=(('weight', float),), create_using=nx.DiGraph())
    return {
        'name': file.replace('instance_').replace('.edges'),
        'size': {'v': G.number_of_nodes(), 'e': G.number_of_edges()},
        'value': {
            'graph': Graph(G),
            'source_node': 1,
            'distance_struct': distance_struct
        }
    }


def generate_dijkstra_instances(instance_dir, distance_struct, size=10):
    i = 0
    for file in sorted(os.listdir(instance_dir)):
        i += 1
        yield load_graph(f'{instance_dir}/{file}', distance_struct)
        if i == size:
            break


def v_plus_e(v=1, e=1):
    return v + e
