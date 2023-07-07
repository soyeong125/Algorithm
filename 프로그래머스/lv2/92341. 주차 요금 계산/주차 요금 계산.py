import math

def solution(fee, records):
    answer = []

    sort_records = [r.split() for r in records]
    sort_records.sort(key=lambda x: (x[1], x[0])) # 차랑변호, 날짜순으로 정렬


    start_time, car = sort_records[0][0], sort_records[0][1] # 탐색할 첫번째 차의 입차 시간과, 차량 번호
    end_time = "23:59"
    total_time = 0

    def cost(st,et,tt): # 비용 계산
        if et == "23:59":
            tt += ((int(et[:2]) - int(st[:2])) * 60) + (int(et[3:]) - int(st[3:]))
        # 이전 차 최종 주차 요금 계산
        if tt <= fee[0]:  # 기본 시간 이하로 있는 경우
            answer.append(fee[1])
        else:  # 기본 시간 초과한 경우
            answer.append(fee[1] + (math.ceil((tt - fee[0]) / fee[2]) * fee[3]))

    #1번부터 탐색 시작
    for idx in range(1,len(sort_records)):
        if car == sort_records[idx][1]: # 이전 차와 차량 번호가 같으면 주차 총 시간 계산해주기
            if sort_records[idx][2] == "OUT": # 출차한 경우, 종료 시간 체크하고 총 소요시간 계산
                end_time = sort_records[idx][0]
                total_time += ((int(end_time[:2]) - int(start_time[:2])) * 60) + (int(end_time[3:]) - int(start_time[3:]))

        else: #차량 번호가 다르면 == 다음차 탐색이 시작되면
            cost(start_time, end_time, total_time)
            total_time = 0 #주차 요금 계산했기 때문에 총 주차 시간 초기화

        # 입차 인 경우 입차 시간 초기화, 출차 시간 초기화
        if sort_records[idx][2] == "IN":
            start_time = sort_records[idx][0]
            end_time = "23:59"

        car = sort_records[idx][1] #현재 기준이 되는 차 변경

    cost(start_time, end_time, total_time) # 가장 마지막 차의 최종 출차 시간 체크 및 주차 비용 체크

    return answer