import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque
if __name__ == "__main__":  
    n,k = map(int,input().split())
    q = deque()
    visited = [-1 for _ in range(100001)]  
    visited[n] = 1
    q.append([n,0,str(n)])
    while q:
        cur,cnt,res = q.popleft()
        if cur == k:
            print(cnt)
            print(res)
            break
        for i in [cur-1,cur+1,cur*2]:
            if 0 <= i < 100001 and visited[i] == -1:
                if i == cur * 2:
                    visited[i] = 1
                    q.append([i,cnt+1,res+' '+str(i)])
                        
                else:
                    visited[i] = 1
                    q.append([i,cnt+1,res+' '+str(i)])


                    
    
