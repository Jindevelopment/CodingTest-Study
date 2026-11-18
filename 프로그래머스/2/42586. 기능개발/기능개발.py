def solution(progresses, speeds):
    answer = []
    
    for i in range(len(progresses)):
        if (100 - progresses[i])%speeds[i] ==0:
            count = (100-progresses[i])//speeds[i]
        else:
            count = (100-progresses[i])//speeds[i] + 1
        answer.append(count)
        
    # answer: 각 기능이 작업하는데 걸리는 시간 완료
    
    count = []
    #뒷 값이 더 작으면 1 추가 하다가 기다리기, 커지면 거기서 확정
    i = 0
    while i < len(answer):
        temp = answer[i]
        j = i + 1
        res = 1
        
        while j < len(answer):
            if temp < answer[j]:
                break
            else:
                j += 1
                res += 1
                
        count.append(res)
        i = j
    return count