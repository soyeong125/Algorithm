import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
   

if __name__ == "__main__":  
    n = int(input())
    tree = [[] for _ in range(n+1)]
    last = 0
    for i in range(n):
        t,l,r = map(int,input().split())
        tree[t].append(l)
        tree[t].append(r)

    #마지막 노드 찾기
    def find_last_val(v):
        if tree[v][1] == -1: return v
        return find_last_val(tree[v][1]) 
    
    #트리 순회
    def dfs_tree(v):
        global last
        if tree[v][0] > -1:
            print(tree[v][0])
            dfs_tree(tree[v][0])

        
        if v == last:
            print(v)
            sys.exit(0)
        print(v)

        if tree[v][1] > -1:
            print(tree[v][0])
            dfs_tree(tree[v][1])

    last = find_last_val(1)
    dfs_tree(1)
    