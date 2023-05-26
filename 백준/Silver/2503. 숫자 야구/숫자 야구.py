import sys
from itertools import permutations
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    permulist = list(permutations([i for i in range(1,10)],3))
    reslist = [1] * len(permulist)

    for i in range(n):
        num,strike,ball = map(int,input().split())
        for p in range(len(permulist)):
            s,b = 0,0
            for i in range(3):
                if str(num)[i] == str(permulist[p][i]):
                    s+=1
                elif str(num)[i] in str(permulist[p]):
                    b+=1
            if s != strike or b != ball:
                reslist[p] = 0

    print(reslist.count(1))