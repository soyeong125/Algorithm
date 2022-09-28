import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    D,N = map(int,input().split())
    oven = list(map(int,input().split()))
    banjuk = list(map(int,input().split()))

    for i in range(1,D):
        oven[i] = min(oven[i],oven[i-1])
    
    idx = 0
    for i in range(N):
        val = banjuk[i]
        l = 0
        r = D-1
        while l<=r:
            mid =(l+r)//2
            if oven[mid] >= val:
                idx = min(idx,mid)
                oven[mid] = 0
                break
            else:
                r = mid - 1

    print(idx+2)


            

        
        