import sys
sys.stdin=open("input.txt","rt")

n=input()
strr=""
arr=[]

for i in n:
    arr.append(int(i))
arr.sort(reverse=True)

for k in arr:
    strr+=str(k)

if(int(strr)%30==0):
    print(int(strr))
else:
    print(-1)