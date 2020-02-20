# Uses python3
import sys

def binary_search(a, x):

    right = len(a)
    start = 0
    end = right- 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
#        flag=0
        print(binary_search(a,x), end = ' ')
