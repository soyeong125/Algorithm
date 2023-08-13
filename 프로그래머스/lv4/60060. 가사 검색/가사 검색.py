def count_by_range(arr, left_val, right_val):
    # 왼쪽 경계 찾기
    left_idx = 0
    right_idx = len(arr)
    while left_idx < right_idx:
        mid = (left_idx + right_idx) // 2
        if arr[mid] < left_val:
            left_idx = mid + 1
        else:
            right_idx = mid

    left_bound = left_idx

    # 오른쪽 경계 찾기
    right_idx = len(arr)
    while left_idx < right_idx:
        mid = (left_idx + right_idx) // 2
        if arr[mid] <= right_val:
            left_idx = mid + 1
        else:
            right_idx = mid

    right_bound = left_idx

    return right_bound - left_bound

def solution(words, queries):
    word_list = [[] for _ in range(10001)]
    reversed_word_list = [[] for _ in range(10001)]
    
    for word in words:
        word_list[len(word)].append(word)
        reversed_word_list[len(word)].append(word[::-1])
    
    for i in range(10001):
        word_list[i].sort()
        reversed_word_list[i].sort()
    
    answer = []
    for query in queries:
        if query[0] != '?':  # 접미사에 '?'가 있는 경우
            cnt = count_by_range(word_list[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:  # 접두사에 '?'가 있는 경우
            cnt = count_by_range(reversed_word_list[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
        answer.append(cnt)
    
    return answer

    