# Uses python3
#STRESS TEST: Max time used: 0.01/5.00, max memory used: 9117696/536870912.
import sys
deno=[1,3,4]#denominations
def get_change(m):
    mincoin = [0]
    for mi in range(1,m+1):
        mincoin.append(mi)
        for i in deno:
            if mi >= i:
                temp = mincoin[mi-i]+1
                if temp < mincoin[mi]:
                    mincoin[mi] = temp
    return mincoin[m]         

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
