import sys
input = sys.stdin.readline

if __name__ == "__main__":
    l,c = map(int,input().split())
    arr = input().split()
    arr.sort(key = lambda x: ord(x[0]))
    visited = [0] * c
    res = []

    def check():
        tmp = ''
        mo_list = ['a', 'e', 'o', 'i', 'u']
        mo,ja = 0,0
        for i in range(c):
            if visited[i]:
                tmp += arr[i]
                if arr[i] in mo_list:
                    mo += 1
                else:
                    ja += 1
        if mo>=1 and ja>=2:
            res.append(''.join(tmp))
        return


    def dfs(level,start):
        if level >= l:
            check()
            return

        for i in range(start,c):
            if not visited[i]:
                visited[i] = 1
                dfs(level+1,i+1)
                visited[i] = 0

    dfs(0,0)

    for word in res:
        print(word)