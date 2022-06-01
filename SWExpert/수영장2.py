import sys
sys.stdin=open("input.txt","rt")
#DFS 
def DFS(month, tmpResult):
    global result
    if month >= 12:
        if tmpResult < result:
            result = tmpResult
        return #Return�� ��ġ
    DFS(month+1,tmpResult+fee_list[0]*month_list[month])
    DFS(month+1,tmpResult+fee_list[1])
    DFS(month+3,tmpResult+fee_list[2])

T = int(input())
for t in range(T):
    fee_list = list(map(int,input().split()))
    month_list = list(map(int,input().split()))
    result = fee_list[3]
    DFS(0,0)
    print('#{} {}'.format(t,result))
