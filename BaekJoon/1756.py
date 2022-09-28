import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    D,N = map(int,input().split())
    oven = list(map(int,input().split()))
    banjuk = list(map(int,input().split()))

    for i in range(1,D):
        oven[i] = min(oven[i],oven[i-1])
    
    cur = 0
    idx = 0
    for i in range(D-1,0,-1):
        if oven[i] < banjuk[cur]:
            continue
        cur +=1
        if cur >= N:
            idx = (i+1)
            break
    print(idx)
            

        
        