def solution(num, k):
    answer = -1
    
    temp = list(str(num))
    for i in range(len(temp)):
        if temp[i] == str(k):
            answer = i+1
            return answer
    
    return answer