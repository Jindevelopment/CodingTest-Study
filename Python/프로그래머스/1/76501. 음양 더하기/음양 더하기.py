def solution(absolutes, signs):
    answer = 0
    for n in range(len(absolutes)):
        if signs[n]==True:
            answer += absolutes[n]
        else:
            answer -= absolutes[n]
    
    return answer