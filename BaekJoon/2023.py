import sys
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

if __name__ == "__main__":  
    def check(sosu):
        v = int(sosu)
        for i in range(2,int(v**0.5)+1):
            if v % i == 0:
                return False
        return True
    def dfs(val,cnt):
        if cnt == n:
            print(val)
            return
        for i in range(10):
            tmp = str(val) + str(i)
            if check(tmp): #소수면
                dfs(tmp,cnt+1)
            
    n = int(input())
    res = []
    for i in [2,3,5,7]:
        dfs(i,1)

if __name__ == "__main__":  
    def check(sosu):
        for i in range(2,int(sosu**0.5)+1):
            if sosu % i == 0:
                return False
        return True
    def dfs(val,cnt):
        if cnt == n:
            print(val)
            return
        for i in range(10):
            tmp = val*10 + i
            if check(tmp): #소수면
                dfs(tmp,cnt+1)
            
    n = int(input())
    res = []
    for i in [2,3,5,7]:
        dfs(i,1)

