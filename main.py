from IPython.display import SVG

import numpy as np
from scipy import sparse
import pandas as pd
import json as js

import sknetwork
from sknetwork.data import from_edge_list, from_adjacency_list, from_graphml, from_csv, load_netset, load_konect
from sknetwork.data import erdos_renyi, block_model, linear_graph, cyclic_graph, linear_digraph, cyclic_digraph, grid, albert_barabasi, watts_strogatz
from sknetwork.data import painters

from sknetwork.topology import get_connected_components, get_largest_connected_component

from sknetwork.visualization import svg_graph, svg_digraph, svg_bigraph
from sknetwork.utils import directed2undirected

with open("wikivital_mathematics.json", "r") as read_file:
    data = js.load(read_file)

data.keys()

edges = np.array(data['edges'])

weighted_edges = [edge + [weigth] for edge, weigth in zip(data['edges'], data['weights'])]

adjacency = from_edge_list(weighted_edges, directed=True)

image = svg_graph(adjacency)

SVG(image)