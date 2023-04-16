if __name__ == "__main__":
    d,n = map(int,input().split())
    oven = list(map(int,input().split()))
    banjuck = list(map(int,input().split()))

    for i in range(1,d):
        oven[i] = min(oven[i-1],oven[i])
    
    cur = 0
    idx = 0
    for i in range(d-1,0,-1):
        if oven[i] < banjuck[cur]:
            continue
        cur +=1
        if cur >= n :
            idx = i+1
            break
    print(idx)