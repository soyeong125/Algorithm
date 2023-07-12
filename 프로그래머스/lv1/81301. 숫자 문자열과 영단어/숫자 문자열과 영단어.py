def solution(s):
    answer = ""
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    idx = 0
    while idx < len(s):
        if ord(s[idx]) >= ord('a') and ord(s[idx]) <= ord('z'):
            for j in range(10):
                if s[idx:idx + 2] in number[j]:
                    answer += str(j)
                    idx += len(number[j])
                    break
        else:
            answer += s[idx]
            idx += 1
    return int(answer)