import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":  
    n,k = map(int,input().split())
    v = [0] * 101
    w = [0] * 101

    for i in range(1,n+1):
        w[i],v[i] = map(int,input().split())
    dp = [0] * 100001

    for i in range(1,n+1):
        for j in range(k,0,-1):
            if w[i] <= j :
                dp[j] = max(dp[j],dp[j-w[i]]+v[i])
    print(dp[k])




  



        





    