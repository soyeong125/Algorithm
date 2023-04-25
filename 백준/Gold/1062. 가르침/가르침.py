import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n,k = map(int,input().split())
    chk = []
    answer = 0
    ask_a = ord('a')
    for i in range(n): #입력받은 문자열 앞/뒤 중복 제거 & 남은 문자열 중복 제거 & 알파벳 순으로 정렬해서 리스트 추가
        str = input().rstrip()
        str = str[4:-4]
        tmp = set()
        for s in str:
            tmp.add(ord(s)-ask_a)
        chk.append(sorted(list(tmp)))
    #알고있는 알파벳 초기화
    alpha = [0] * 26
    know = ['a','n','t','i','c']
    for i in range(5):
        alpha[ord(know[i])-ask_a] = 1

    def dfs(l,idx):
        global answer
        if l == (k-5):
            cnt = 0
            for chk_str in chk:
                tmp_chk = True
                for c in chk_str:
                    if not alpha[c]:
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
    if k < 5:
        print(0)
    elif k == 26:
        print(n)
    else:
        dfs(0,0)
        print(answer)