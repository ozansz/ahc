from Ahc import ComponentModel, Event, GenericMessage, GenericMessageHeader, EventTypes, ComponentRegistry, Lock, Thread, Topology
from Channels import P2PFIFOPerfectChannel, Channel
import time
import matplotlib.pyplot as plt

import networkx as nx
import numpy as np
from Routing.FredericksonAlgorithmAdvanced.RoutingExample.MachineLearningNodeComponent import MachineLearningNode


edges = [(0, 1, {"weight": 1}), (0, 2, {"weight": 1}), (1, 3, {"weight": 1}), (2, 4, {"weight": 1}), (4, 5, {"weight": 1}),
         (3, 5, {"weight": 1}), (1, 4, {"weight": 1}), (4, 6, {"weight": 1}), (4, 7, {"weight": 1}),
         (6, 8, {"weight": 1}), (8, 9, {"weight": 1}), (7, 10, {"weight": 1}), (7, 11, {"weight": 1}),
         (11, 13, {"weight": 1}), (2, 12, {"weight": 1}),
         (7, 9, {"weight": 1})]

# undirected graph
graph = nx.Graph()
graph.add_edges_from(edges)

topology = Topology()
topology.construct_from_graph(graph, MachineLearningNode, P2PFIFOPerfectChannel)
# process1 = MachineLearningNode("MachineLearningNode", 0)
# ComponentRegistry().init()
# topology.plot()
# plt.show()

topology.start()

while True:pass



