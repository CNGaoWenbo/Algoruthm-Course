# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    stops.insert(0,0)
    numR = 0
    current = 0
    n=len(stops)-1#终点是n+1
    while 0<= current <= n:
        last = current
        while stops[current+1] - stops[last] <= tank:#能到下一个点
            current = current+1
                
            if current == n:#开到终点了
                return numR
            
        numR = numR+1#没到下一个点，退出循环
        if current == last:
            return -1


    return numR

if __name__ == '__main__':
    #print(compute_min_refills(960,400,[500,475,550,750]))
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
