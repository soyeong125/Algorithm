import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n+1)]
    node = [[],[0,0]]

    for i in range(2,n+1):
        t,a,p = input().split()
        a = int(a)
        p = int(p)
        tree[p].append(i)
        node.append([t,a])
    
    def dfs(v):
        result = 0
        
        for i in tree[v]:
            result += dfs(i)
        if node[v][0] == 'W':
            result -= node[v][1]
            if result < 0:
                result = 0
        else:
            result += node[v][1]
        return result
    print(tree)
    print(node)


  