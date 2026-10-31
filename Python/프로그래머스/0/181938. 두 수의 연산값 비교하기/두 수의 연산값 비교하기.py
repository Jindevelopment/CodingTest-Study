def solution(a, b):
    answer = 0
    temp1 = str(a) + str(b)
    
    if int(temp1) > 2*a*b:
        answer = int(temp1)    
    else:
        answer = 2*a*b
    return answer