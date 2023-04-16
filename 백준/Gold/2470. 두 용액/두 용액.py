import sys
import math


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    l = 0
    r = n - 1
    ans = abs(arr[l] + arr[r])
    res = [arr[l],arr[r]]

    while l < r:
        l_val = arr[l]
        r_val = arr[r]
        sum_val = l_val + r_val

        if abs(sum_val) < ans :
            ans = abs(sum_val)
            res = [l_val,r_val]
            if ans == 0:
                break
        if sum_val < 0 :
            l = l + 1
        else:
            r = r - 1

    print(res[0],res[1])