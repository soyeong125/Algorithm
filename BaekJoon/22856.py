import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

if __name__ == "__main__":  
    n = int(input())
    tree = [[] for _ in range(n+1)]

    for i in range(n):
        t,l,r = map(int,input().split())
        tree[t].append(l)
        tree[t].append(r)

    
    def find_last_val(v,depth):
        if tree[v][1] == -1: return depth
        return find_last_val(tree[v][1],depth+1) 
    
    print(2*(n-1) - find_last_val(1,0))