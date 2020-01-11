def chfdora(A,n,m):
    c=0
    for i in range(0,n):
        for j in range(0,m):
            d=min(i,n-1-i,j,m-j-1)
            pnt=0
            for k in range(0,d+1):
                if A[i-k][j]!=A[i+k][j]:
                    break
                else:
                    pnt+=1
            gnt=0
            for k in range(0,d+1):
                if A[i][j-k]!=A[i][j+k]:
                    break
                else:
                    gnt+=1
            c+=min(pnt,gnt)
    print(c)


T=int(input())
for i in range(0,T):
    N,M=map(int,input().split())
    A=[]
    for i in range(N):
        B=list(map(int,input().split()))
        A.append(B)
    chfdora(A,N,M)
#print (A)
'''
def chfdora(A,N,M):
    count=N*M
    k=min(N,M)
    for r in range(1,N-1):
        for c in range(1,M-1):
            b=min(c,M-c-1,r,N-r-1)
            for j in range(1,b+1):
                #print(r,c)
                if A[r][c+j]!=A[r][c-j] or A[r+j][c]!=A[r-j][c]:
                    break
                else:
                    count+=1
            
    print (count)
chfdora([[1],[1],[1],[1],[1]],5,1)
'''

#chfdora([[1,2,1,1,2,1,2],[1,2,1,2,1,1,2],[2,1,1,1,1,1,2],[2,1,1,2,1,2,1],[1,1,2,1,2,1,2]],5,7)
