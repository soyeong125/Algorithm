import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    
    def go(i,w):
        if i == n:
            return 0
        n1 = 0
        n2 = 0
        if arr[i][0] + w <= k:
            n1 = go(i+1,w+arr[i][0]) + arr[i][1]
            n2 = go(i+1,w)
        return max(n1,n2)

    print(go(0,0))


    

    