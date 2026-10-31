
def solution(n):
    answer = 0
    
    temp = int(n**0.5)
    
    if n == temp**2:
        answer=1
    else:
        answer = 2
    
    return answer