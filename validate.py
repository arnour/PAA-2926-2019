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


## Bottles

QUESTION = "bottles"
