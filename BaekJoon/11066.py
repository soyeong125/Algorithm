import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline



if __name__ == "__main__": 
    while 1:
        try:
            print(input())
        except EOFError:
            break




