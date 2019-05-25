from libs.CPUtimer import CPUTimer
import subprocess
import sys

result_folder = "./data/results/"
inputs_folder = "./data/inputs/"

timer = CPUTimer()

def test_and_save(filename, instance_name, n, times, function, *args, **kwargs):
    subprocess.call(f"rm {result_folder}/{filename}", shell=True)
    for i in range(times):
        print(f"executing to {filename} and instance {instance_name} {i+1}/{times} for n={n}")
        sys.stdout.flush()
        timer.reset()
        timer.start()
        function(*args, **kwargs)
        timer.stop()
        time_lapse = timer.get_time("total", "milliseconds")
        subprocess.call(f"echo '{instance_name},{n},{time_lapse}\n' >> {result_folder}/{filename}", shell=True)


## Dijkstra

QUESTION = "dijkstra"

import networkx as nx
from networkx.readwrite.edgelist import read_edgelist
from paa191t1.dijkstra import dijkstra
from paa191t1.dijkstra.datastructs import graph, vector, fibonacci_heap, heap, buckets

states = ["NY", "USA", "CTR", "W", "E", "LKS", "CAL", "NE", "NW", "FLA", "COL", "BAY"]

structures = [
    vector.Vector(), fibonacci_heap.FibHeap(), heap.Heap(), buckets.Buckets()
]

for state in states:
    G = read_edgelist(f"{inputs_folder}/{QUESTION}/{state}.edges", nodetype = int, data=(('weight',float),), create_using=nx.DiGraph())
    data = list(G.nodes())
    size = len(data)
    source = data[0]
    for structure in structures:
        test_and_save(f"{QUESTION}/{structure}_{state}.csv", state, size, 5, dijkstra, graph.Graph(G), source, structure)

## PPH

QUESTION = "pph"

from paa191t1.pph.pph_median import pph_median
from paa191t1.pph.pph_n_2 import pph_n_2
from paa191t1.pph.pph_n_log_n import pph_n_lg_n
from paa191t1.pph.pph_custom_pivot import pph_custom_pivot
from paa191t1.pph import Pair

pph_files = ['pph_19_01.dat','pph_29_01.dat' ,'pph_39_01.dat','pph_49_01.dat','pph_59_01.dat','pph_69_01.dat','pph_79_01.dat','pph_89_01.dat','pph_99_01.dat']

pph_instances = []

def read_pph_instances(file_path):
  
    with open(file_path) as pph:
        num_instances = pph.readline()
        a_instances = []
        b_instances = []
        pairs = []
        is_a = True
        for instance in pph.readlines():
            i = instance.replace("\n", "").strip()
            if not i:
                is_a = False
                continue
            if is_a:
                a_instances += i.split(" ")
            else:
                b_instances += i.split(" ")
          
        t = Pair(int(a_instances[0]), int(b_instances[0]))
      
        for i in range(1, len(a_instances)):
            pairs.append(Pair(int(a_instances[i]),int(b_instances[i])))
      
        return (t, pairs)

for pph_file in pph_files:
    t0,n = read_pph_instances(f"{inputs_folder}/{QUESTION}/{pph_file}")
    pph_instances.append((pph_file, t0, n))

pph_functions = [pph_median, pph_custom_pivot, pph_n_lg_n, pph_n_2]

for pph_function in pph_functions:
    for instance in pph_instances:
        pph_file, t0, n = instance
        test_and_save(f"{QUESTION}/{pph_function.__name__}_{pph_file}.csv", pph_file, len(n), 100000, pph_function, n, t0)


## Bottles

QUESTION = "bottles"
