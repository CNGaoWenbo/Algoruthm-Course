# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    if m*n == 0:
        return m+n
    D=[]
    for i in range(m+1):
        D.append([0]*(n+1))
    #print(D)
    for i in range(m+1):
        D[i][0] = i
       # print(D)
    for i in range(n+1):
        D[0][i] = i
      #  print(D)
    for i in range(1,m+1):
        for j in range(1,n+1):
            insertion = D[i][j-1]+1
            deletion = D[i-1][j]+1
            match = D[i-1][j-1]
            dismatch = D[i-1][j-1]+1
            if s[i-1] == t[j-1]:
                D[i][j] = min(insertion,deletion,match)
            else:
                D[i][j] = min(insertion,deletion,dismatch)
    return D[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
