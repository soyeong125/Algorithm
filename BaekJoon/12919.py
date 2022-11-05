import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    s = list(input().rstrip())
    t = list(input().rstrip())
    flag = False

    def dfs(arr,l):
        global flag
        if l > 0 and arr[:l+1] != t[:l+1]:
            return
        if len(arr) == len(t):
            if arr == t:
                flag = True
            return
        
        arr.append("A")
        dfs(arr,l+1)
        arr.pop()

        arr.append("B")
        arr.reverse()
        dfs(arr,l+1)
        arr.reverse()
        arr.pop()

    dfs(s,0)
    print(1 if flag else 0)