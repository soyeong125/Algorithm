if __name__ == "__main__":
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    res = [sum(arr[:k])]

    for i in range(n-k):
        res.append(res[i] - arr[i] + arr[k+i])
    print(max(res))