import optalg
import numpy as np
G = np.loadtxt("ori_graph.txt")
result = optalg.dijk(G,0,4)
print(result)
