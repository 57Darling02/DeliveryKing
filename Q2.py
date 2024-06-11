import math
import numpy as np
import optalg
import time
M = math.inf
start_time = time.time()
G = np.loadtxt("opt_graph.txt")
OG = np.loadtxt("ori_graph.txt")
# 等待顾客取餐的时间 min
def throw_wait(x=1):
    # 定义正态分布的参数：均值（mean），标准差（stddev）
    mean = 3  # 均值
    stddev = 0.6  # 标准差
    if x==0:
        return mean
    else:
        return max(0.1 ,np.random.normal(mean, stddev))
# 骑手进店取餐耗时
waittime2 = 1
def pick_wait(x=1):
    # 定义正态分布的参数：均值（mean），标准差（stddev）
    mean = 1  # 均值
    stddev = 0.2  # 标准差
    if x==0:
        return mean
    else:
        return max(0.1 ,np.random.normal(mean, stddev))
#平均每分钟移动的距离 60km/h = 1km/min  40km/h = 0.667km/h
averspeed = 1
# 最后一单送达时间限制
limit_time = 60




def printresult(stage,opt_status,OG):
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
    print_opt(opt_status,OG)
def print_opt(opt_status,OG):
    print("***************opt*******************")
    print(opt_status)
    full_path=[]
    path0=[]
    path0.extend(opt_status.get("path"))
    for i in range(len(path0) - 1):
        full_path.extend(optalg.dijk(OG, path0[i], path0[i + 1]))
    full_path.append(path0[-1])
    print(f"fullpath:{full_path}")

def GetTime(start_time,opt_status,OG,itercount):
    T = time.time()
    if  T- start_time >= 5:
        if not hasattr(GetTime, 'last_run_time'):
            GetTime.last_run_time = T
            print("运行超过5s,输出当前最优结果:")
            print(f"当前迭代次数{itercount}")
            print_opt(opt_status,OG)
            print("程序继续运行,将每隔5s输出一次最优目前最优解")
        elif T - GetTime.last_run_time >= 5:
            print("当前最优结果:")
            print(f"当前迭代次数{itercount}")
            print_opt(opt_status, OG)
            print("程序继续运行...")
            GetTime.last_run_time = T


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
    [6,8], #0.06
    [6,8], # 1.4
    [5,8], # 1.726180076599121 seconds
    [6,9], # 9.149291515350342 seconds
    [7,8], # 10.777399063110352 seconds
    [8,40], #  13.456018447875977 seconds
    [9,8], # 15.147678852081299 seconds
    [10,22], # 16.096506595611572 seconds
    [11,22], # 29.35
    [12,36],
    [13,36],
    [14,36],
    [29,36],
    [35,36],
]
take_out_index = list(range(len(take_out)))
##init
n=0
stage ={} # 放所有阶段 stage[0]就算n=0
allstatus =[] # 放本阶段包含的所有
opt_status={"time":0,"stage":0,"ReceviedOrder": set(),"active":True,"path":[]}
allstatus.append(opt_status)
stage[0] = allstatus
itercount = 0
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
            newtime = (n-1)*throw_wait(0)+ newlenth/averspeed +n*pick_wait(0)
            estimatedtime = (n-1)*throw_wait()+ newlenth/averspeed +n*pick_wait()
            if newtime < limit_time:
                newstatus = {"time": newtime,"estimatedtime":estimatedtime, "stage": n, "ReceviedOrder": new_get_index, "active": True,"path":newpath}
            else:
                newstatus = {"time": newtime,"estimatedtime":estimatedtime,  "stage": n, "ReceviedOrder": new_get_index, "active": False,"path":newpath}
            # 找最优
            if newstatus.get("time")<=limit_time and newstatus.get("stage")>=opt_status.get("stage"):
                if newstatus.get("stage")>opt_status.get("stage"):
                    opt_status = newstatus
                elif newstatus.get("time")<opt_status.get("time"):
                    opt_status = newstatus
            allstatus.append(newstatus)
            itercount+=1
            GetTime(start_time, opt_status, OG,itercount)
    # print(allstatus)
    if not allstatus:
        break
    stage[n]=allstatus

printresult(stage,opt_status,OG)
print(f"exc:{time.time()-start_time}")