# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    lis = [1,1]
    for i in range(2,n):
        new = lis[i-1]+lis[i-2]
        lis.append(new)
    return lis[n-1]

n = int(input())
print(calc_fib(n))
