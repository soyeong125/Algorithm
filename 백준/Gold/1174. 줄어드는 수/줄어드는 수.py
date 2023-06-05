if __name__ == "__main__":
    n = int(input())
    result = []
    arr = []

    def dfs():
        if len(arr) > 0 :
            result.append(int(''.join(map(str,arr))))

        for i in range(10):
            if len(arr) == 0 or arr[-1] > i:
                arr.append(i)
                dfs()
                arr.pop()

    dfs()
    result.sort()
    print(-1 if n-1 >= len(result) else result[n-1])