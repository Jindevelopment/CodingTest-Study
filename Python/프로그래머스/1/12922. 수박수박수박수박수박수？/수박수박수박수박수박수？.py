def solution(n):
    temp = ["수","박"]
    answer = ""
    for i in range(n):
        answer += temp[i%2]
    
    return answer