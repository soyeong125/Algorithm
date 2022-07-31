def solution(word):
    answer = 0
    words = 'AEIOU'
    word_list = []
    def dfs(cnt,w):
        if cnt == 5:
            return
        for i in range(len(words)):
            word_list.append(w+words[i])
            dfs(cnt+1,w+words[i])
    dfs(0,"")
    # for i in range(len(word_list)):
    #     if word_list[i] == word:
    #         return i+1
    return word_list.index(word) + 1

if __name__ == "__main__" :
         print(solution("AAAAE"))