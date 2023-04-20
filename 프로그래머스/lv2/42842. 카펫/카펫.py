def solution(brown, yellow):
    for i in range(1,yellow+1):
        a,b = 0,0 # 가로, 세로
        if yellow % i == 0: # yello 의 약수 구하기
            a = i 
            b = yellow // i
        if 2 * (a+b) + 4 == brown: # yellow의 둘레에 4를 더하면 brown 이 된다.
            return [b+2,a+2] # brown의 가로값, 세로값