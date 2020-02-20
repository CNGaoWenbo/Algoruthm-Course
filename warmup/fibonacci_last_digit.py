# Uses python3
'''import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)

    return current
'''
def fibo_last_digi_num(n):
    if n <=1:
        return n
    num = [1,1]
    for i in range(2,n):
        new = (num[i-1] + num[i-2]) % 10
        num.append(new)
    return num[n-1]
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibo_last_digi_num(n))

