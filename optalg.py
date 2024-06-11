import gurobipy as gp
from gurobipy import GRB
import numpy as np
# tsp模型
def tsp(graph):
    model = gp.Model("tsp")
    model.setParam(GRB.Param.OutputFlag, 0)
    n = len(graph[0])
    # 定义决策变量
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")
    # 目标函数：最小化总距离
    z = gp.quicksum(x[i, j] * graph[i][j] for i in range(n) for j in range(n) if i != j)
    model.setObjective(z, GRB.MINIMIZE)
    # 约束条件
    # 每个节点只能离开一次
    for i in range(n):
        model.addConstr(gp.quicksum(x[i, j] for j in range(n) if i != j) == 1, name="out_{}".format(i))
    # 每个节点只能进入一次
    for j in range(n):
        model.addConstr(gp.quicksum(x[i, j] for i in range(n) if i != j) == 1, name="in_{}".format(j))
    for k in range(n):
        model.addConstr(gp.quicksum(x[i, k] for i in range(n) if i == k) == 0, name="fuck_{}".format(k))
    # 子回路约束
    u = model.addVars(n, lb=-GRB.INFINITY, ub=GRB.INFINITY, name="u")
    for i in range(n):
        for j in range(n):
            if i != j and i > 0 and j > 0:
                # 将辅助变量u与决策变量x连接起来
                model.addConstr(u[i] - u[j] + n * x[i, j] <= n - 1, "break_{}_{}".format(i, j))
    # 配置求解器并求解
    model.optimize()
    # 输出结果
    x_list=[]
    if model.status == GRB.OPTIMAL:
        # print(f"The optimal objective is {model.objVal}")
        for v in model.getVars():
            if v.X >= 0.5 and v.varName.startswith('x'):
                # print(f"{v.varName} : {v.X}")
                x_list.append(f"{v.varName}")
    else:
        print("No optimal solution found.")
        return None
    return model.objVal ,x_list

def floydWarshall(graph):
    # 获取顶点的数量
    n = len(graph)
    # 初始化距离矩阵和路径矩阵
    dist = [row[:] for row in graph]
    # 执行Floyd-Warshall算法
    for k in range(n):  # 对于每一个顶点作为中间顶点
        for i in range(n):  # 遍历每一个起始顶点
            for j in range(n):  # 遍历每一个终点
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def perms(dingdanm):
    result = [[]]
    while (dingdanm):
        danm = dingdanm.pop()
        new_result = []
        for org in result:
            j = len(org)
            while j >= 0:
                i = 0
                while i <= j:
                    add = org.copy()
                    # Execution time: 6.9922730922698975 seconds
                    # add = add[:i]+[danm[0]]+add[i:j]+[danm[1]]+add[j:]
                    # Execution time: 4.674955606460571 seconds
                    add.insert(i, danm[0])
                    add.insert(j + 1, danm[1])
                    new_result.append(add)
                    i += 1
                j -= 1
        # print(new_result)
        result = new_result
    # print(len(result))
    return result

def dpmin(G,start,dingdamn):
    M = np.inf
    all_path = perms(dingdamn)
    minlength = M
    minpath = []

    for path in all_path:
        length = G[start][path[0]]
        for node in range(len(path)-1):
            length += G[path[node]][path[node+1]]
        if length < minlength:
            minlength = length
            minpath = path
    minpath.insert(0,start)
    return minlength,minpath

def dijk(ori_graph,start,end):
    n = len(ori_graph)
    dist=np.full(n, np.inf)
    pred=np.full(n,-1)
    visitd = [False for _ in range(n)]
    dist[start]=0
    for i in range(n-1):
        min = np.inf
        min_index = -1
        for j in range(n):
            if (not visitd[j]) and dist[j] <= min:
                min = dist[j]
                min_index = j
        visitd[min_index]=True
        for j in range(n):
            if ori_graph[min_index][j] !=np.inf and (not visitd[j]) and dist[min_index]!=np.inf and dist[min_index] + ori_graph[min_index][j] < dist[j]:
                dist[j]=dist[min_index] + ori_graph[min_index][j]
                pred[j]=min_index
    current = end
    path =[]
    while(current!=start):
        current = pred[current]
        path.insert(0,current)
    return path