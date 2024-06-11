import math
import numpy as np
import optalg
M = math.inf
import pandas as pd
# 读取Excel文件

df = pd.read_excel('data.xlsx', sheet_name=0,header=None)

# 将DataFrame中的所有'M'替换为numpy.inf

df.replace('M', M, inplace=True)

# 如果需要将数据转换为二维数组（numpy数组）
graph = df.values

print(df)
dist= optalg.floydWarshall(graph)
np.savetxt("opt_graph.txt", dist)
np.savetxt("ori_graph.txt",graph)
