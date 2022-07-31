import math

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