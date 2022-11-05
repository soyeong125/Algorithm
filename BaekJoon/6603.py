import sys
from xxlimited import Str
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

if __name__ == "__main__":

    def combination(array,r):
        for i in range(len(array)):
            if r == 1:
                yield [array[i]]
            else:
                for next in combination(array[i+1:],r-1):
                    yield [array[i]] + next

    while 1:
        arr = list(map(str,input().split()))

        k = arr[0]
        s = arr[1:]

        if k == 0:
            break
        for c in combination(s,6):
            print(' '.join(c))

        print()
    
