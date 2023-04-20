def solution(brown, yellow):
    for i in range(1,yellow+1):
        a,b = 0,0
        if yellow % i == 0:
            a = i
            b = yellow // i
        if a > b:
            break
        if 2*(a+b) + 4 == brown:
            return [b+2,a+2]