import sys
sys.stdin=open("input.txt","rt")

n=int(sys.stdin.readline())
arr=sorted(list(map(int,sys.stdin.readline().split())))

if len(arr)%2 == 0:
    result=0
    for i in range(len(arr)//2):
        result = max(arr[i]+arr[len(arr)-1-i],result)
else:
    result = arr.pop()
    for i in range(len(arr)//2):
        result = max(arr[i]+arr[len(arr)-1-i],result)
print(result)


#최대의 최소를 구해야한다.
#어떤 것을 더해서 최소가 되려면 오름차순 정렬 후 가장 작은 것 + 가장 큰 것을 더하면 된다.
#이 값들이 최소인데 이 값들중에서 최대를 찾으면 답이된다.