def solution(bandage, health, attacks):
    answer = 0
    
    start = health
    continue_time = 0
    
    max_time = 0 #마지막 공격 시간
    
    for i in range(len(attacks)):
        max_time = max(attacks[i][0],max_time)
        
    current_time = 0
    while current_time <= max_time:
        attack = False
        for k in range(len(attacks)):
            if attacks[k][0] == current_time:
                start -= attacks[k][1]
                continue_time = 0
                attack = True
                if start <= 0:
                    start = 0
                break
                
        if not attack:
            start += bandage[1]
            continue_time += 1
            if bandage[0] == continue_time:
                start += bandage[2]
                continue_time = 0
            if start >= health:
                start = health
        current_time += 1
        if start <= 0:
            return -1


    if start == 0:
        answer = -1
    else:
        answer = start
    
    return answer