import sys
sys.stdin = open("input.txt", 'r')


def dfs(level):
    global n
    global arr

    for i in range(1,(level//2)+1):
        if arr[-i:] == arr[-i*2:-i]:return -1

    if level == n:
        for i in arr:print(i,end='')
        return 0
    
    for i in range(1,4):
        arr.append(i)
        if dfs(level+1) == 0:
            return 0
        arr.pop()
    


if __name__ == "__main__":
    n = int(sys.stdin.readline())  
    arr = []
    dfs(0)
