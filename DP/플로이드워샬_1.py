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


#�÷��̵� �ͼ� �˰���:
#1.��� �������� ��� �������� �ִ� ��θ� ���ϰ� ���� ���
#i�� j ������ ���ϴ� ��� ������ �־�� ��ΰ� ���� ���� ���� ä��
#������ �������� ������ �̷�������Ѵ�.
#�ϳ��� �������� �ٸ� ��� ���� -> ���ͽ�Ʈ��

#Ʋ������ i>j>k ������ 3�� for�� ������ 
#k>i>j ������ �����ؾ� ��ü���� �ּҰ����� ������ ����
#dynamic table�� ���ؼ� ��ü �ּ��� ������ ������ �����ϴ�.
#i>1>2>..>j �� ��쵵 i>k>j ���� ����Ͽ� dynamic table�� ������ 
#���� �� �� ���ԵǼ� ����� �ȴ�.