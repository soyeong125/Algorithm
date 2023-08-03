if __name__ == "__main__":
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))


    sum_val = sum(arr[0:k])
    res = sum_val
    rm = 0
    include = k


    while include < n :
        tmp_val = sum_val - arr[rm] + arr[include]
        res = max(res,tmp_val)
        sum_val = tmp_val
        rm += 1
        include +=1

    print(res)