import sys
sys.stdin=open("input.txt","rt")

n,m=map(int,input().split())
grap=[[0]*(n+1) for _ in range(n+1)]
dgree=[0]*(n+1)
stack=[i for i in range(1,n+1)]
for i in range(m):
    a,b=map(int,input().split())
    grap[a][b]=1
    dgree[b]+=1

while stack:
    for j in stack:
        if dgree[j]==0:
            print(j,end=' ')
            stack.remove(j)
            for k in range(1,n+1):
                if grap[j][k]==1:
                    dgree[k]-=1


    

