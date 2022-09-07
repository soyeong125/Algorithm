import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n+1)]
    node = [0,0]

    for i in range(2,n+1):
        t,a,p = input().split()
        a = int(a)
        p = int(p)
        tree[p].append(i)
        if t=="W":
            node.append(-a)
        else:
            node.append(a)

    def dfs(v):
        result = 0       
        for i in tree[v]:
            result += dfs(i)
        result += node[v]
        if result < 0:
            result = 0
        return result
    print(dfs(1))
   