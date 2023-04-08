import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    k,n = list(map(int,input().split()))
    arr = []
    res = 0 
    for _ in range(k):
        t = int(input())
        arr.append(t)
    
    r = 1
    l = max(arr)
    
    while r <= l :
        target = 0
        mid = (r+l) // 2

        for i in arr:
            target += i//mid
        
        if target >= n:
            r = mid  + 1
            res = max(res,mid)
        else:
            l = mid - 1
    print(res) 
            

