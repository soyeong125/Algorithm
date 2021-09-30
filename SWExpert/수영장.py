# DP
T = int(input())
for t in range(T):
    fee = list(map(int,input().split()))
    plan = list(map(int,input().split()))
    result = [0]*13  #결과를 누적 
    for i in range(1,13):
        a = [0,0,987654321,987654321] #이번달 요금 결과 저장 , 이 값중에서 가장 최소 값이 그달의 최소값
        a[0] = result[i-1] + fee[0]*plan[i-1] #1일권 사용하는 경우: 지난달 요금 + 일일권
        a[1] = result[i-1] + fee[1] # 1달 사용하는 경우 : 지난달 요금 + 한달권
        if i >= 3: #3월 이상인 경우, ex) 0월 + (1,2,3월) 3개월치 요금 
            a[2] = result[i-3] + fee[2]
        if i == 12: # 12월인 경우 1년치 요금 계산해서 마지막에 누적금액들과 최소금액 비교
            a[3] = fee[3]
        result[i] = min(a) #1일, 1달, 3달 , 1년치 중 최소값 선택
    print('#{} {}'.format(t,result[12]))
    