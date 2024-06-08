import time
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
    print(len(result))
    return result
# 效率测试
start_time = time.time()
dingdanm =[
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10],
    [11,12], #高压
    # [13.14],  #烤鸡
]
perms(dingdanm)
end_time = time.time()
# 计算并打印执行时间
print(f"Execution time: {end_time - start_time} seconds")



