import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n,k = map(int,input().split())
    if k < 5:
        print(0)
        exit()
    elif k == 26:
        print(n)
        exit()

    answer = 0
    chk = [set(input().rstrip()) for _ in range(n)]
    alpha = [0] * 26
    for a in ['a','n','t','i','c']:
        alpha[ord(a)-ord('a')] = 1

    def dfs(l,idx):
        global answer
        if l == (k-5):
            cnt = 0
            for chk_str in chk:
                tmp_chk = True
                for c in chk_str:
                    if not alpha[ord(c)-ord('a')]:
                        tmp_chk = False
                        break
                if tmp_chk:
                    cnt+=1
            answer = max(answer,cnt)
            return
        for i in range(idx,len(alpha)):
            if not alpha[i]:
                alpha[i] = 1
                dfs(l+1,i)
                alpha[i] = 0
    dfs(0,0)
    print(answer)