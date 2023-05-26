import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    paramlist = [list(map(int,input().split())) for _ in range(n)]
    arrlist = ['1','2','3','4','5','6','7','8','9']
    answer = []
    res = 0

    def check():
        global res
        for i in range(len(paramlist)):
            num,strike,ball = paramlist[i]
            s,b = 0,0
            for i in range(3):
                if int(str(num)[i]) == answer[i]:
                    s += 1
                elif int(str(num)[i]) in answer:
                    b += 1
            if strike != s or ball != b:
                return
        res += 1
        return

    def dfs(l):
        if l == 3:
            check()
            return
        for i in range(1,10):
            if i not in answer:
                answer.append(i)
                dfs(l+1)
                answer.pop()
    dfs(0)
    print(res)