import math

#(1) brown + yellow = 넓이
#(2) yellow로 나타낼 수 있는 사각형 체크
#(2-1) 가로세로 길이 정하기 > 긴게 가로(약수체크)
#(3) 가로*세로 +4 가 brown의 넓이면 출력   
def solution(brown, yellow):
    answer = []
    xx , yy = 0 , 0
    for i in range(yellow,0,-1):
        if yellow % i == 0:
            if yellow // i >= i:
                xx = yellow//i
                yy = i

            else:
                xx = i
                yy = yellow//i
            if xx*2 + yy*2 + 4 == brown:
                  answer.append(xx+2)
                  answer.append(yy+2)
                  break
    return answer