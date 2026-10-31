def solution(n):
    answer = []
    
    for k in range(1,n+1):
        if n%k==0:
            answer.append(k)
    return answer