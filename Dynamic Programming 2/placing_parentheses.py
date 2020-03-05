# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
def minandmax(i,j):
    mini = float('inf') #m[i][j]
    maxi = float('-inf') #M[i][j]
    for k in range(i,j):
        a = evalt(M[i][k],M[k+1][j],op[k])
        b = evalt(M[i][k],m[k+1][j],op[k])
        c = evalt(m[i][k],m[k+1][j],op[k])
        d = evalt(m[i][k],M[k+1][j],op[k])
        if mini > min(a,b,c,d):
            mini = min(a,b,c,d)
        if maxi< max(a,b,c,d):
            maxi = max(a,b,c,d)
    return mini, maxi

def get_maximum_value(dataset):
    #write your code here   
    dig = [] #digit
    global op #operation
    op = []
    for i in range(len(dataset)):
        if (i+2) % 2 == 0:
            dig.append(int(dataset[i]))
        else :
            op.append(dataset[i])
    n = len(dig)
    global m, M
    m = []
    M = []
    for i in range(n):
        m.append([0]*len(dig))
        M.append([0]*len(dig))
    for i in range(n):
        m[i][i] = dig[i]
        M[i][i] = dig[i]
    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            m[i][j], M[i][j] = minandmax(i,j)

    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
