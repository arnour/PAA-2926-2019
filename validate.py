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
        returned = function(*args, **kwargs)
        timer.stop()
        time_lapse = timer.get_time("total", "milliseconds")
        extra_args = ",".join([str(r) for r in returned])
        subprocess.call(f"echo '{instance_name},{n},{time_lapse},{extra_args}' >> {result_folder}/{filename}", shell=True)


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

pph_files = ['pph_4_01.dat','pph_8_01.dat' ,'pph_16_01.dat','pph_32_01.dat','pph_64_01.dat','pph_128_01.dat','pph_256_01.dat'
            ,'pph_512_01.dat','pph_1000_01.dat', 'pph_2000_01.dat', 'pph_4000_01.dat', 'pph_10000_01.dat'
            ]

pph_instances = []

def read_pph_instances(file_path):
  
    with open(file_path) as pph:
        num_instances = pph.readline()
        pairs = []
        all_elements = []

        for line in pph.readlines():
            l = line.strip().split(" ")
            all_elements += l
        
        n = int(num_instances)
        a0 = int(all_elements[0])
        b0 = int(all_elements[n+1])
        t = Pair(a0, b0)
        
        for i in range(1, n+1):
            a = int(all_elements[i])
            b = int(all_elements[(n+1)+i])
            if b == 0:
                b = np.random.randint(10,400,size=1)[0]
            pairs.append(Pair(a,b))
      
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

from paa191t1.bottles.bottles_binary import bottles as bottles_binary
from paa191t1.bottles.bottles import bottles
from paa191t1.bottles.binary_search import bottles as binary_search

test_bottles = 8

with open(f"{inputs_folder}/{QUESTION}/bignum_256_01.dat") as bignum:
    num_bits, num_instances = bignum.readline().replace("\n", "").split(" ")
    for instance in bignum.readlines():
        number = instance.replace("\n", "")
        test_and_save(f"{QUESTION}/binary_search_{test_bottles}.csv", num_bits, num_instances, 1, binary_search, int(num_bits), number)