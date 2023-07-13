import sys
input = sys.stdin.readline
if __name__ == "__main__":
    a,b = [input().rstrip() for _ in range(2)]
    stack = []

    for i in a:
        stack.append(i)
        while True:
            if len(stack) >= len(b):
                tmp = ''.join(stack[-len(b):])
                if tmp == b:
                    for _ in range(len(b)):
                        stack.pop()
                else:
                    break
            else:
                break
    print('FRULA' if len(stack) == 0 else ''.join(stack))