def solution(a, b, g, s, w, t):
        answer = -1
        L = 0
        R = 1 * 10**9 * 10**5 * 2 * 2 # 최소의 무게 1을 10**9번 옮기는 경우 이때 1번 옮기는데 시간이 10**5 시간 걸리고 왕복이고 금/은 둘다 해야한다.
        town = len(g)
        while L <= R:
            T = (L+R)//2
            TOTAL = 0
            G = 0
            S = 0
            for i in range(town):
                cnt = T // (t[i]*2)
                if T % (t[i]*2) >= t[i]:
                    cnt +=1
                
                weight = w[i] * cnt
                G += min(weight,g[i])
                S += min(weight,s[i])
                TOTAL += min(weight,g[i]+s[i])
            if G >= a and S >= b and TOTAL >= a+b:
                R = T -1
            else:
                L = T + 1

        return L