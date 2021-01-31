import sys
#sys.stdin=open("input.txt","rt")

if __name__ =="__main__":
    n=int(input())
    dp=[[216000000]*(n+1) for _ in range(n+1)]
    while 1:
        a,b=map(int,input().split())
        if a==-1 and b==-1:
            break
        dp[a][b]=1
        dp[b][a]=1
    for i in range(n):
        dp[i][i]=0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
    score=[0]*(n+1)
    minn=2160000000
    cnt=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            score[i]=max(score[i],dp[i][j])
        if minn>score[i]:
            minn=score[i]
    for i in range(1,n+1):
        if score[i]==minn:
            cnt+=1
    print(minn, cnt)
    for k in range(1,n+1):
        if minn==score[k]:
            print(k,end=' ')
        


    
        


