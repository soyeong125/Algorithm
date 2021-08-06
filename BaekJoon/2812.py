import sys
sys.stdin=open("input.txt","rt")

n,k=map(int,input().split())
num=input()
result=[]
i=0
while len(num)!=i:
	while result and result[-1]<num[i] and k!=0:
		result.pop()
		k-=1
	result.append(num[i])
	i+=1
while k>0:
	result.pop()
	k-=1
print(int("".join(result)))


	
	
