# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    c = capacity
    w = weights
    v = values
    if type(w) == type(1):#仅一件物品
        if w>c:#装一部分
            value = v/w*c
        else:#全装
            value = v
    else:
        #初始化
        vpw=[]
        vn=[]
        wn=[]
        for i in range(len(w)):
            vpw.append(v[i]/w[i])#单位价值
        index = sorted(range(len(vpw)), key=lambda k: vpw[k])
        index.reverse()#大到小的序号
        for i in index:
            vn.append(v[i]) #单位价值从大到小的价值
        for i in index:
            wn.append(w[i]) #单位价值从大到小的重量值    
        while c:
            for i in range(len(wn)):  #装东西
                if wn[i] <= c: #还能装
                    c = c-wn[i]                   
                    value = value+vn[i]
                    wn[i] = 0
                else:#装不了
                    value = value+vn[i]/wn[i]*c
                    c=0
            return value #背包没装满，东西不够多

    return value                               


if __name__ == "__main__":
    #print(get_optimal_value(50,[10,10,10,10,10,10,10],[10,30,20,40,50,60,70]))

    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


'''
test case
一件物品 略
包太大 1000,[30,10,10],[500,50,10] =560
包太小 50,[20,50,30],[60,100,120] =180
   
    if type(weights)==type(1):
        w = [weights,0.00000001]
        v = [values,0]  
    value = 0
    func = lambda x,y:x/y
    vpw = list(map(func,v,w))
    index = sorted(range(len(vpw)), key=lambda k: vpw[k])
    index.reverse()
    w.reverse()
    v.reverse()
    vpw.reverse()
'''