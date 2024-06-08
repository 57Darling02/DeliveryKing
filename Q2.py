import math
import numpy as np
import optalg
M = math.inf
G = np.loadtxt("opt_graph.txt")
OG = np.loadtxt("ori_graph.txt")
# 等待顾客取餐的时间 min
waittime1 = 3
def throw_wait():
    # 定义正态分布的参数：均值（mean），标准差（stddev）
    mean = 3  # 均值
    stddev = 0.6  # 标准差
    # return 3
    return max(0.1 ,np.random.normal(mean, stddev))
# 骑手进店取餐耗时
waittime2 = 1
def pick_wait():
    # 定义正态分布的参数：均值（mean），标准差（stddev）
    mean = 1  # 均值
    stddev = 0.2  # 标准差
    # return 1
    return max(0.1 ,np.random.normal(mean, stddev))
#平均每分钟移动的距离 60km/h = 1km/min  40km/h = 0.667km/h
averspeed = 0.667
# 最后一单送达时间限制
limit_time = 60

########################################Q1
# 骑手当前位置为 v1 index=0
start = 4
# 可接订单列表[pick, throw]
# pick为取餐点，throw为送餐点
take_out = [
    [4,0],
    [5,14],
    [18,32],
    [25,36],
    [40,27],
    [11,14],
]
take_out_index = list(range(len(take_out)))
##init
n=0
stage ={} # 放所有阶段 stage[0]就算n=0
allstatus =[] # 放本阶段包含的所有
status={"time":0,"stage":0,"ReceviedOrder": set(),"active":True,"path":[]}
allstatus.append(status)
stage[0] = allstatus
##动态规划
while True:
    n+=1 #阶段数/单量
    allstatus =[] #放本阶段包含的所有
    for prestage_statu in stage[n-1]:
        if not prestage_statu["active"]:
            continue
        # trystatus = prestage_statu
        canadd = list(set(take_out_index) - prestage_statu["ReceviedOrder"])
        for add_index in canadd:
            flag = False
            # new_get_index = prestage_statu.get("ReceviedOrder").copy().add(add_index)
            new_get_index = prestage_statu["ReceviedOrder"].copy()
            new_get_index.add(add_index)
            # print(new_get_index)
            for check in allstatus:
                if check.get("ReceviedOrder") == new_get_index:
                    flag = True
                    break
            if flag: #新的订单集合已经存在
                continue
            #新的订单集合不存在
            # print(new_get_index)
            dingdamn = [take_out[i] for i in new_get_index]
            newlenth,newpath = optalg.dpmin(G,start,dingdamn)
            newtime = (n-1)*throw_wait()+ newlenth/averspeed +n*pick_wait()
            if newtime < limit_time:
                newstatus = {"time": newtime, "stage": n, "ReceviedOrder": new_get_index, "active": True,"path":newpath}
            else:
                newstatus = {"time": newtime, "stage": n, "ReceviedOrder": new_get_index, "active": False,"path":newpath}
            allstatus.append(newstatus)
    # print(allstatus)
    if not allstatus:
        break
    stage[n]=allstatus
# print(stage)
opt_status=stage[0][0]
for n,stagelist in stage.items():
    print(f"**************第{n}阶段:***************")
    count=1
    for status0 in stagelist:
        print(f"*****第{n}阶段状态{count}:")
        count+=1
        time0=status0.get("time")
        # list(status0.get("ReceviedOrder"))
        ifew = status0.get("active")
        bh = status0.get("ReceviedOrder")
        print(f"外卖接单编号:{bh}\n完成订单最短耗时:{time0}\n能否额外接单{ifew}")
        if status0.get("time")<=limit_time and status0.get("stage")>=opt_status.get("stage"):
            if status0.get("stage")>opt_status.get("stage"):
                opt_status = status0
            elif status0.get("time")<opt_status.get("time"):
                opt_status = status0
print("***************opt*******************")
print(opt_status)
full_path=[]
path0=[]
path0.extend(opt_status.get("path"))
for i in range(len(path0) - 1):
    full_path.extend(optalg.dijk(OG, path0[i], path0[i + 1]))
full_path.append(path0[-1])
print(f"fullpath:{full_path}")
