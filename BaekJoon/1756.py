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
    l,r = 0 , D-1
    
    for b in banjuk:  
        ch = False     
        while l <= r:
            mid = (l+r)//2
            if oven[mid] >= b:
                l = mid + 1
                idx = mid
                ch = True
            else:
                r = mid - 1
        if not ch:
            idx = -1
            break
        l = 0
        r = idx -1
    if idx == -1:
        print(0)
    else:
        print( idx + 1 )

    



            

        
        