import sys

def solution(N, number):
    answer = -1
    if N == number:
        return 1
    s = [ set() for x in range(8) ] 
    for i,x in enumerate(s, start=1):
            x.add( int( str(N) * i ) )
    for i in range(1, 8):
        for j in range(i):
            for s1 in s[j]:
                for s2 in s[i-j-1]:
                    s[i].add(s1+s2)
                    s[i].add(s1-s2)
                    s[i].add(s1*s2)
                    if s2 != 0:
                        s[i].add(s1//s2)
        if number in s[i]:
            answer=i+1
            break
    return answer

    















    
            







    

