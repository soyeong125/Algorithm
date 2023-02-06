import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    number = list(map(int,input().split()))
    opt = list(map(int,input().split()))
    maxnum = -1e9
    minnum = 1e9

    def dfs(l,sum):
        global opt
        global maxnum
        global minnum
        if l == n :
            maxnum = max(sum,maxnum)
            minnum = min(sum,minnum)
            return
        
        if opt[0] > 0 :
            tmp = sum
            tmp += number[l]
            opt[0]-=1
            dfs(l+1,tmp)
            opt[0] +=1
        if opt[1] > 0 :
            tmp = sum
            tmp -= number[l]
            opt[1]-=1
            dfs(l+1,tmp)
            opt[1] +=1
        if opt[2] > 0 :
            tmp = sum
            tmp *= number[l]
            opt[2]-=1
            dfs(l+1,tmp) 
            opt[2] +=1
        if opt[3] > 0 :
            tmp = sum
            tmp = int(tmp/number[l])
            opt[3] -=1
            dfs(l+1,tmp)
            opt[3] +=1
    
    dfs(1,number[0])    
    print(maxnum)                 
    print(minnum)    