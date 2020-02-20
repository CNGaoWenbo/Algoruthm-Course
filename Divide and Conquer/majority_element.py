# Uses python3
import sys
import collections
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here

    counts = collections.Counter(a)
    ele = max(counts.keys(), key=counts.get)
    count = 0
    for i in range(len(a)):
        if ele == a[i]:
            count=count+1
    if count > n/2:
        return ele
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
