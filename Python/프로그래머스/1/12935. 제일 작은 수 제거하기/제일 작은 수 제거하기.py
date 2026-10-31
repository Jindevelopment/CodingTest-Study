def solution(arr):
    answer = []
    for i in arr:
        answer.append(i)
        
    answer.remove(min(arr))
    
    if answer == []:
        return [-1]
    return answer