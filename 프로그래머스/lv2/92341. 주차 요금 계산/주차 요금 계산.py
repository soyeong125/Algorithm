import math
def solution(fee, records):
    answer = []
    sort_records = [r.split() for r in records]
    sort_records.sort(key=lambda x: (x[1], x[0]))

    start_time, car = sort_records[0][0], sort_records[0][1]
    end_time = ""
    total_time = 0

    for idx in range(1,len(sort_records)):
        if car == sort_records[idx][1]:
            if sort_records[idx][2] == "OUT":
                end_time = sort_records[idx][0]
                total_time += ((int(end_time[:2]) - int(start_time[:2])) * 60) + (int(end_time[3:]) - int(start_time[3:]))
                # start_time = ""
                # end_time = ""
            else:
                start_time = sort_records[idx][0]
                end_time = ""

        else:
            if end_time == "":
                end_time = "23:59"
                total_time += ((int(end_time[:2]) - int(start_time[:2])) * 60) + (int(end_time[3:]) - int(start_time[3:]))

            # 이전 차 주차 요금 계산
            if total_time <= fee[0]:
                answer.append(fee[1])
            else:
                answer.append(fee[1] + (math.ceil((total_time - fee[0]) / fee[2]) * fee[3]))

            total_time = 0

            if sort_records[idx][2] == "IN":
                start_time = sort_records[idx][0]
                end_time = ""

        car = sort_records[idx][1]
        idx +=1


    if end_time == "":  # end_time이 비었다?
        end_time = "23:59"
        total_time += ((int(end_time[:2]) - int(start_time[:2])) * 60) + int(end_time[3:]) - int(start_time[3:])

    if total_time <= fee[0]:
        answer.append(fee[1])
    else:
        answer.append(fee[1] + (math.ceil((total_time - fee[0]) / fee[2]) * fee[3]))

    return answer