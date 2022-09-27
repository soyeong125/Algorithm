import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    cardnum = int(input())
    cardarr = list(map(int,input().split()))
    cardarr.sort()
    inputnum = int(input())
    inputarr = list(map(int,input().split()))
    answer = [0] * inputnum

    for i in range(inputnum):
        val = inputarr[i]
        l = 0
        r = cardnum
        while l <= r:
            mid = (l + r) //2
            if mid < 0 or mid >= cardnum:
                break
            if cardarr[mid] < val:
                l = mid +1
            elif cardarr[mid] > val: 
                r = mid -1
            elif cardarr[mid] == val:
                answer[i] = 1
                break
    for i in answer:
        print(i,end=' ')

        
