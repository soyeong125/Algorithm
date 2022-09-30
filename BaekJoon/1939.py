import sys
input = sys.stdin.readline

if __name__ == "__main__": 
    n,m = map(int,input().split())
    world = [[0] * n for _ in range(n)]
    for _ in range(m):
        s,e,v = map(int,input().split())
        if s < e:
            world[s-1][e-1] = v    
        else:
            world[e-1][s-1] = v
    v1,v2 = map(int,input().split())
    result = 0

    def dfs(idx,val):
        global result
        if idx == v2-1:
            result = max(result,val)
            return
        
        for i in range(n):
            if world[idx][i] > 0:
                dfs(i,min(world[idx][i],val))
    dfs(v1-1,10000000000)
    print(result)