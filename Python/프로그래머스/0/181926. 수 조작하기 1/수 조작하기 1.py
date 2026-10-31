def solution(n, control):
    answer = n
    temp = {"w":1,"s":-1,"d":10,"a":-10}
    
    for i in control:
        answer += temp[i]
    
    return answer