import math
import numpy as np
import optalg
M = math.inf
G = np.loadtxt("opt_graph.txt")
OG = np.loadtxt("ori_graph.txt")

#配送中心为 v5
start = 4
capacity = 4
all_lenth=0
all_path = []
count=0
#需求节点为 v3 v5 v9 v12  [index, need]
need = [
    [0,4],
    [2,5],
    [12,8],
    [14,3],
    [20,2],
    [27,6],
    [32,7],
    [36,2]
]
while(need):
    overplus = capacity
    tspnow = [start]
    x_tsp = []
    ####断点检查
    print(f"*************从起点出发****************\n当前需求need([需求点,需求量]):\n{need}")
    while(overplus>0):
        max1 = [0, -1]  # [长度, need_index]
        max2 = [0, -1]
        for i in range(len(need)):
            if overplus >= need[i][1]:
                tsptry = tspnow.copy()
                tsptry.append(need[i][0])
                temp_g = [[0 for _ in range(len(tsptry))] for _ in range(len(tsptry))]
                for k in range(len(tsptry)):
                    for j in range(len(tsptry)):
                        temp_g[k][j] = G[tsptry[k]][tsptry[j]]
                pathlen, meiyy = optalg.tsp(temp_g)
                if max1[0] < pathlen:
                    max1[0] = pathlen
                    max1[1] = i
            else:
                tsptry = tspnow.copy()
                tsptry.append(need[i][0])
                temp_g = [[0 for _ in range(len(tsptry))] for _ in range(len(tsptry))]
                for k in range(len(tsptry)):
                    for j in range(len(tsptry)):
                        temp_g[k][j] = G[tsptry[k]][tsptry[j]]
                pathlen, meiyy = optalg.tsp(temp_g)
                if max2[0] < pathlen:
                    max2[0] = pathlen
                    max2[1] = i
        print(f"##overplus = {overplus},tspnow = {tspnow},need={need}")
        if max1[1]>-1:
            # print(f"max1={max1[1]}")
            tspnow.append(need[max1[1]][0])
            overplus -= need[max1[1]][1]
            need.pop(max1[1])
            pass
        elif max2[1]>-1:
            # print(f"max2={max2[1]}")
            tspnow.append(need[max2[1]][0])
            need[max2[1]][1] -= overplus
            overplus = 0
            pass
        else:
            break
        print(f"##overplus = {overplus},tspnow = {tspnow},x_tsp = {x_tsp},need={need}")
    print(f"overplus = {overplus},tspnow = {tspnow},x_tsp = {x_tsp},need={need}")
    ##得到第一个tsp圈
    temp_g = [[0 for _ in range(len(tspnow))] for _ in range(len(tspnow))]
    for k in range(len(tspnow)):
        for j in range(len(tspnow)):
            temp_g[k][j] = G[tspnow[k]][tspnow[j]]
    length_temp,x_temp = optalg.tsp(temp_g)
    # print(f"x-temp={x_temp}")
    for i in x_temp:
        var_name, indices = i.split('[')
        indices = indices[:-1]  # 去掉最后一个']'字符
        x_tsp.append(tspnow[(int)(indices.split(',')[0])]) # 分割索引为列表
    x_tsp.append(start)
    full_path=[]
    for i in range(len(x_tsp)-1):
        full_path.extend(optalg.dijk(OG,x_tsp[i],x_tsp[i+1]))
    full_path.append(x_tsp[-1])
    all_lenth+=length_temp
    all_path.append(x_tsp)
    print(f"路长{length_temp},路径{x_tsp}\nfullpath:{full_path}")
    count+=1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("**************************")
print(f"总长{all_lenth},圈数：{count},{all_path}")



