import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


if __name__ == "__main__":  
    cardnum = int(input())
    cardarr = list(map(int,input().split()))
    cardarr.sort()
    inputnum = int(input())
    inputarr = list(map(int,input().split()))

    def search(start,end,target):
        while start <= end:
            mid = (start+end) //2
            if cardarr[mid] < target:
                start = mid +1
            elif cardarr[mid] > target: 
                end = mid -1
            elif cardarr[mid] == target:
                return 1
        return 0

    for i in range(inputnum):
        target = inputarr[i]
        if search(0,cardnum - 1,target):
            print(1,end = ' ')
        else:
            print(0,end = ' ')
        
        
