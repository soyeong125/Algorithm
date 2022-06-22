def solution(number, k):
    stack = []
    for i in number:
        cur = int(i)
        if not stack:
            stack.append(cur)
        else:
            if cur > stack[-1] and k:
                while stack:
                    if cur <= stack[-1] or not k :
                        break
                    stack.pop()
                    k-=1
            stack.append(cur)

    while k and stack:
        stack.pop()
        k-=1
                       
    return ''.join(str(i) for i in stack)

if __name__ =='__main__':
    print(solution("01010", 3), "11") #���� ������ stack[-1]������ pop���� �ʰ� ���α