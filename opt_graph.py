import math
import numpy as np
import optalg
M = math.inf
#origin graph
graph = [
    [0,6,M,17,M,M,M,M,7,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [6,0,2,M,M,1,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,2,0,M,M,M,2,8,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [17,M,M,0,7,M,M,M,M,M,M,M,M,M,M,M,M,11,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,7,0,M,M,M,M,M,M,M,6,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,1,M,M,M,0,1,M,M,3,3,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,2,M,M,1,0,6,M,M,M,2,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,8,M,M,M,6,0,M,M,M,M,M,M,M,M,M,M,M,M,M,M,10,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [7,M,M,M,M,M,M,M,0,2,M,M,M,4,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,3,M,M,2,0,2,M,M,M,3,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,3,M,M,M,2,0,4,M,M,M,2,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,2,M,M,M,4,0,M,M,M,M,2,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,6,M,M,M,M,M,M,M,0,2,M,M,M,M,4,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,4,M,M,M,2,0,1,M,M,M,M,M,M,M,M,M,M,7,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,3,M,M,M,1,0,1,M,M,M,M,M,M,M,M,M,M,8,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,2,M,M,M,1,0,3,M,M,3,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,2,M,M,M,3,0,M,M,M,2,4,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,11,M,M,M,M,M,M,M,M,M,M,M,M,M,0,2,M,M,M,M,3,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,4,M,M,M,M,2,0,M,M,M,M,M,2,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,3,M,M,M,0,1,M,M,M,M,M,M,3,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,2,M,M,1,0,2,M,M,M,M,M,M,1,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,4,M,M,M,2,0,3,M,M,M,M,M,M,3,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,10,M,M,M,M,M,M,M,M,M,M,M,M,M,3,0,M,M,M,M,M,M,M,2,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,3,M,M,M,M,M,0,1,M,M,M,M,M,M,M,M,M,M,M,9,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,2,M,M,M,M,1,0,6,M,M,M,M,M,3,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,7,M,M,M,M,M,M,M,M,M,M,6,0,1,M,M,M,M,M,3,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,8,M,M,M,M,M,M,M,M,M,M,1,0,3,M,M,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,3,M,M,M,M,M,M,3,0,2,M,M,M,M,M,4,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,1,M,M,M,M,M,M,2,0,2,M,M,M,M,M,M,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,3,M,M,M,M,M,M,2,0,1,M,M,M,M,1,M,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,2,M,M,M,M,M,M,1,0,M,M,M,M,M,M,M,M,M,6],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,3,M,M,M,M,M,M,0,7,M,M,M,4,M,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,3,M,M,M,M,M,7,0,3,M,M,M,3,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,3,0,3,M,M,M,2,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,4,M,M,M,M,M,3,0,5,M,M,M,1,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,1,M,M,M,M,5,0,M,M,M,M,2],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,9,M,M,M,M,M,M,M,4,M,M,M,M,0,5,M,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,3,M,M,M,5,0,1,M,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,2,M,M,M,1,0,2,M],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,1,M,M,M,2,0,6],
    [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,6,M,M,M,M,2,M,M,M,6,0],
    ]

dist= optalg.floydWarshall(graph)
np.savetxt("opt_graph.txt", dist)
np.savetxt("ori_graph.txt",graph)
