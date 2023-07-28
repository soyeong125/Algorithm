from collections import defaultdict
def solution(record):
    answer = []
    #id 에 맞는 최종 닉네임 저장
    name_dic = defaultdict()
    for r in record:
        r_list = r.split()
        if r_list[0] == "Enter" or r_list[0] == "Change":
            name_dic[r_list[1]] = r_list[2]
    for r in record:
        r_list = r.split()
        tmp = ""
        if r_list[0] == "Enter":
            tmp = name_dic[r_list[1]] + "님이 들어왔습니다."
            
        elif r_list[0] == "Leave":
            tmp = name_dic[r_list[1]] + "님이 나갔습니다."
        else:
            continue
        answer.append(tmp)     
            
    return answer
