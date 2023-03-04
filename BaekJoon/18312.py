import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":
    n,k = map(int,input().split())
    res = 0
    for h in range(n+1):
        if h < 10:
            hh = '0' + str(h)
        else:
            hh = str(h)
        if str(k) in hh:
            res += (60*60)
            continue
        for m in range(60):
            if m < 10:
                mm = '0' + str(m)
            else:
                mm = str(m)
            if str(k) in mm :
                res += 60
                continue
            for s in range(60):
                if s < 10:
                    ss = '0' + str(s)
                else:
                    ss = str(s)
                if str(k) in ss:
                    res +=1
    print(res)
