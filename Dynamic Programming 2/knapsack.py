# Uses python3
import sys
'''
def greedy_optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
'''
def optimal_weight(W, w):
    value = []
    n = len(w)
    for i in range(n+1):
        value.append([0]*(W+1))
    for i in range(1,n+1):
        for j in range(1,W+1):
            value[i][j] = value[i-1][j]
            if w[i-1] <= j:
                val = value[i-1][j-w[i-1]]+w[i-1]        #value = weight        
                if value[i][j] < val:
                    value[i][j] = val
    return value[i][j]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
