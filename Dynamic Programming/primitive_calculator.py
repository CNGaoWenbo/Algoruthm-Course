# Uses python3
#STRESS TEST: Max time used: 0.51/7.50, max memory used: 13717504/536870912.
import sys
import math
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)
def my_optimal_sequence(n):
    if n == 1:
        return [1]
       # print(num_op)
    num_op = [0,0]
    for i in range(2,n+1):
       # print(i)
        t1,t2,t3 = [math.inf]*3 
        t1 = num_op[i-1]+1
      #  print('t1:',i-1,t1)
        if i%2 == 0:
            t2 = num_op[i//2]+1
      #      print('t2:',i//2,t2)
        if i%3 == 0:
            t3 = num_op[i//3]+1
      #      print('t3:',i//3,t3)
        num = min(t1,t2,t3)
        num_op.append(num)
       # print(num_op)

    sequence = [n]
    while n > 1:
        if n%3 == 0 and num_op[n//3] == num_op[n]-1:
            n = n//3
            sequence.append(n)
        if n%2 == 0 and num_op[n//2] == num_op[n]-1:
            n = n//2
            sequence.append(n)
        if num_op[n-1] == num_op[n] - 1:
            n = n-1
            sequence.append(n)
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(my_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
