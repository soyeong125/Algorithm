#�ð��ʰ� �ذ�:sys.setrecursionlimit(10000)  
#Top-Down ��� (x,y)�� ���� �� (x,y)���� (0,0)���� ���� ����� ��
#�����ϸ� 1�� ����
#-1�� üũ����Ʈ ����: ���� ���� ���� ���
#0 �ѹ��̶� �湮�� ���
#������ ������ DFS�� �̿��Ͽ� ��θ� �����ش�.
#return visited[x][y]�� visited[0][0] �ؼ� ���� ����� ���


import sys
sys.stdin = open("input.txt","rt")
from collections import deque
sys.setrecursionlimit(10000)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def DFS(x,y):
    if x==(m-1) and y==(n-1):
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y]=0
    for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<m and 0<=yy<n and mapp[x][y]>mapp[xx][yy]:
                        visited[x][y]+=DFS(xx,yy)
    return visited[x][y]


if __name__ == "__main__":
    m, n = map(int,input().split())
    mapp = [list(map(int,input().split())) for _ in range(m)]
    visited = [[-1]*n for _ in range(m)]
    print(DFS(0,0))

    

