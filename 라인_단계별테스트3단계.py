import sys
from collections import deque
import heapq
import re
sys.stdin = open("input.txt","rt")
 

from collections import deque

def solution(program, flag_rules, commands):
    answer = []

    #프로그램 이름을 저장 변수
    program_name = program 

    #입력받은 flag_rules 저장 변수
    rule_check = {} 
    #별칭을 저장하는 tuple
    alias={}
    #입력받은 flag_rules 저장
    for i in flag_rules:
        rule = i.split()
        flag=rule[0]
        flag_arg=rule[1]
        #별칭있는 경우 기존에 존재하는 key값의 value를 동일하게 저장
        if flag_arg == 'ALIAS':
            if rule[2] in rule_check:
                rule_check[flag]=rule_check[rule[2]]
            else:
                alias[flag] = rule[2]
        if flag not in rule_check:
            rule_check[flag]=flag_arg
    #별칭이 먼저 나오는 경우를 대비하여 별칭이 존재하는 경우 가장 마지막에 해준다.
    if len(alias)>0:
        for k,v in alias.items():
            rule_check[k]=rule_check[v]


   


    #입력받은 commands가 입력 받은 flag_rules에 적합한지 확인
    for i in commands:

        comm=deque(i.split())

        #1. 프로그램 이름이 일치하는지 확인
        if comm.popleft() != program_name:
            answer.append(False)
            continue

        #2. 명령어가 규칙에 맞는지 확인
        while comm:
            #시작 명령어 값을 저장하는 변수
            start_comm=''
            ch_comm = comm.popleft()
            
            #명령어의 맨 앞의 값이 flag로 시작되는지 확인한다
            if ch_comm in rule_check.keys():
                #명령어로 시작하는 경우 명령어를 저장
                start_comm=ch_comm
                #flag가 -e 인 경우 명령어가 종료되어야함
                if rule_check[ch_comm] == 'NULL':
                    if (len(comm)==0):
                        result=True
                    else:
                        result=False
                        break
                        
                else:
                    ch_comm_arg=comm.popleft()
                    if rule_check[ch_comm] in 'STRING':
                         if ch_comm_arg.isalpha():
                               result=True
                         else:
                               result=False

                    elif rule_check[ch_comm] in 'NUMBER':
                           if ch_comm_arg.isdigit():
                               result=True
                           else:
                               result=False
            else:
                #명령어로 시작하는 경우가 아닌 경우 복수의 argument인지 잘못된 경우인지 확인 해주어야함
                #명령어가 오지 않았는데 argument가 오는 경우 -> 실패
                if start_comm =='' :
                        result=False
                #명령어가 왔고 복수의 argument인 경우 string인 경우 number인 경우 체크해준다.
                elif ch_comm.isalpha() and rule_check[start_comm] in 'STRING':
                        result = True
                elif ch_comm.isdigit() and rule_check[start_comm] in 'NUMBER':
                        result = True

        answer.append(result)
    return answer


  

if __name__ == "__main__":
    print(solution("bank",["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"],["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))
    
    #print(solution("line",["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
    

    
