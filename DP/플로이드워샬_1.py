import sys
#sys.stdin=open("input.txt","rt")

if __name__ =="__main__":
    n,m=map(int,input().split())
    dp=[[216000000]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][i]=0
    for i in range(m):
        a,b,c=map(int,input().split())
        dp[a][b]=c
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dp[i][j]==216000000:
                print("M",end=' ')
            else:   
                print(dp[i][j],end=' ')
        print('')


#플로이드 와샬 알고리즘:
#1.모든 정점에서 모든 정점으로 최단 경로를 구하고 싶은 경우
#i와 j 사이의 속하는 모든 정점을 넣어보고 경로가 가장 작은 값을 채택
#정점을 기준으로 갱신이 이루어져야한다.
#하나의 정점에서 다른 모든 정점 -> 다익스트라

#틀린이유 i>j>k 순으로 3중 for문 구현함 
#k>i>j 순으로 구현해야 전체적인 최소값으로 갱신이 가능
#dynamic table로 인해서 전체 최소인 값으로 갱신이 가능하다.
#i>1>2>..>j 인 경우도 i>k>j 만을 계산하여 dynamic table에 넣으면 
#갱신 할 때 포함되서 계산이 된다.