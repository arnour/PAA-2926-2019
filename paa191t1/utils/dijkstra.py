import os
import math
import networkx as nx
from networkx.readwrite.edgelist import read_edgelist
from paa191t1.dijkstra import dijkstra
from paa191t1.dijkstra.datastructs.graph import Graph
import almetro
from almetro.instance import generator
from almetro.complexity import Complexity


def load_graph(_file, distance_struct):
    G = read_edgelist(_file, nodetype=int, data=(('weight', float),), create_using=nx.DiGraph())
    instance_name = _file.split('/')[-1].replace('instance_', '').replace('.edges', '')
    instance_size = G.number_of_nodes() + G.number_of_edges()
    return {
        'name': f'{instance_name} ({instance_size})',
        'size': {'v': G.number_of_nodes(), 'e': G.number_of_edges()},
        'value': {
            'graph': Graph(G),
            'source_node': 1,
            'distance_struct': distance_struct
        }
    }


def generate_dijkstra_instances(instance_dir, distance_struct, size=10):
    i = 0
    for _file in sorted(os.listdir(instance_dir)):
        i += 1
        yield load_graph(f'{instance_dir}/{_file}', distance_struct)
        if i == size:
            break


def almetro_dijkstra(trials=5, instances=10, complexity=None, struct=None, instance_path=None):
    instance_generator = generate_dijkstra_instances(instance_path, struct, instances)
    return almetro\
        .new()\
        .with_execution(trials=trials, runs=1)\
        .with_instances(instances=instances, provider=generator(instance_generator))\
        .metro(algorithm=dijkstra, complexity=complexity)


def v_plus_e(v=1, e=1):
    return v + e


def c_v_plus_e(c=1, v=1, e=1):

    return v + e


dijkstra_v_quadratic = Complexity(
    theoretical=lambda v=1, e=1: v * v,
    experimental=v_plus_e,
    text='O(v^2)',
    latex=r'$\mathcal{O}(v^2)$'
)

dijkstra_v_plus_e_log_v = Complexity(
    theoretical=lambda v=1, e=1: (v + e) * math.log2(v),
    experimental=v_plus_e,
    text='O((v + e) * log v)',
    latex=r'$\mathcal{O}((v+e) * \log_2{v})$'
)

dijkstra_v_log_v_plus_e = Complexity(
    theoretical=lambda v=1, e=1: (v * math.log2(v)) + e,
    experimental=v_plus_e,
    text='O((v * log v) + e)',
    latex=r'$\mathcal{O}((v * \log_2{v}) + e)$'
)

dijkstra_v_c_plus_e = Complexity(
    theoretical=lambda v=1, e=1, c=1: (v * c) + e,
    experimental=c_v_plus_e,
    text='O((v*c) + e)',
    latex=r'$\mathcal{O}((v*c) + e)$'
)
