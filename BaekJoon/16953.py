import sys
sys.stdin=open("input.txt","rt")

def DFS(L,val,goal):
    if val == goal:
        print(L+1)
        sys.exit()
    if val > goal:
        return
    DFS(L+1,val*2,goal)
    DFS(L+1,val*10+1,goal)


if __name__ == "__main__":
    a,b = map(int,input().split())
    DFS(0,a,b)
    print(-1)
    

