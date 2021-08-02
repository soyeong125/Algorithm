import sys
sys.stdin=open("input.txt","rt")

T=int(input())
for _ in range(T):
	N = int(sys.stdin.readline())
	arr=[tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
	new_arr = sorted(arr, key=lambda x:(x[0]))
	
	st = new_arr[0][1]
	cnt= 1
	for i in new_arr:
		if st > i[1]:
			st = i[1]
			cnt+=1
	print(cnt)



