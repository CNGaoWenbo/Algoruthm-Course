# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    lis = [0,1]
    lis_r = [0,1]
    for i in range(2,n):
        lis[i] = lis[i-1]+lis[i-2]
        lis_r[i] = lis[i]%m
        if lis_r[i] == 0 & lis_r[i+1] == 1 & lis_r[i+2] == 1:
            flag = i
            period = i
        
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
