import sys
#sys.stdin=open("input.txt","rt")

if __name__ =="__main__":
    n,m=map(int,input().split())
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        score,time=map(int,input().split())
        if time > m:
            break
        for k in range(time,m+1):
            dp[i][k]=max(dp[i-1][k-time]+score,dp[i-1][k])
	#for k in range(m+1,time-1,-1)
	#    dp[k]=max(dp[k-time]+score,dp[k])

print(dp[n][m])
#2�������� �ϴ� ��� > �޸� ����
#�ߺ��� ������� �ʴ� ��� DP
#DP Table�� ���� �����ؾ���(���� �Ϳ��� X)

#1���� > �ξ� ȿ����
#�ڿ��� ���� ����ϸ鼭 ������ ���� �ߺ� ����� �ȵ�