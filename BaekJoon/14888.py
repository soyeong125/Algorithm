import sys
import math
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    number = list(map(int,input().split()))
    opt = list(map(int,input().split()))
    max_num = -1e9
    min_num = 1e9

    def dfs(l,res,plus,min,mul,div):
        global max_num
        global min_num
        
        if l == n:
            max_num = max(res, max_num)
            min_num = min(res, min_num)
            return

        if plus:
            dfs(l+1,res+number[l],plus-1,min,mul,div)
        if min:
            dfs(l+1,res-number[l],plus,min-1,mul,div)
        if mul:
            dfs(l+1,res*number[l],plus,min,mul-1,div)
        if div:
            dfs(l+1,int(res/number[l]),plus,min,mul,div-1)
    dfs(1,number[0],opt[0],opt[1],opt[2],opt[3])
    print(max_num)
    print(min_num)


# if __name__ == "__main__":
#     n = int(input())
#     number = list(map(int,input().split()))
#     opt = list(map(int,input().split()))
#     maxnum = -1e9
#     minnum = 1e9

#     def dfs(l,sum):
#         global opt
#         global maxnum
#         global minnum
#         if l == n :
#             maxnum = max(sum,maxnum)
#             minnum = min(sum,minnum)
#             return
        
#         if opt[0] > 0 :
#             tmp = sum
#             tmp += number[l]
#             opt[0]-=1
#             dfs(l+1,tmp)
#             opt[0] +=1
#         if opt[1] > 0 :
#             tmp = sum
#             tmp -= number[l]
#             opt[1]-=1
#             dfs(l+1,tmp)
#             opt[1] +=1
#         if opt[2] > 0 :
#             tmp = sum
#             tmp *= number[l]
#             opt[2]-=1
#             dfs(l+1,tmp) 
#             opt[2] +=1
#         if opt[3] > 0 :
#             tmp = sum
#             tmp = int(tmp/number[l])
#             opt[3] -=1
#             dfs(l+1,tmp)
#             opt[3] +=1
    
#     dfs(1,number[0])    
#     print(maxnum)                 
#     print(minnum)    