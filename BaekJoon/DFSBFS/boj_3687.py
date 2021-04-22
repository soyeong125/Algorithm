import sys
from collections import deque
sys.stdin = open("input.txt","rt")


def DFS_MAX(k):
    if k==2 or k==3:
        return dic[k][0]
    if dp[k]==0:
        dp[k]=DFS_MAX(k-2)*10+DFS_MAX(2)
    return dp[k]
    
def DFS_MIN(k):
    num=[0,0,1,7,4,2,0,8,10]
    dp=[0]*101
    for i in range(1,9):
        dp[i]=num[i]
    dp[6]=6
    for i in range(9,k+1):
            dp[i]=dp[i-2]*10 + dp[2]
            for j in range(3,8):
                    dp[i]=min(dp[i],dp[i-j]*10+num[j])
    return dp[k]


   
if __name__ =="__main__":
    n=int(input())
    dic={2:[1],3:[7],4:[4],5:[2,3,5],6:[0,6,9],7:[8]}
    dp=[0]*101

    for _ in range(n):
        k = int(input())
        print(DFS_MIN(k),end=' ')
        print(DFS_MAX(k))



    

