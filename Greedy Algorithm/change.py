# Uses python3
import sys

def get_change(m):
    #write your code here
    count10 = 0
    count5 = 0
    count1 = 0
    if m >= 10:
        count10 = m//10
        m = m -count10*10
    if m >= 5:
        count5 = m//5
        m = m-count5*5
    if m >= 1:
        count1 = m
    return count1+count5+count10

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))