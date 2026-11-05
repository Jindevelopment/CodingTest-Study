def solution(n, m):
    answer = []
    if n<m:
        temp = 0
        for i in range(1,n+1):
            if n % i == 0 and m % i == 0:
                temp = i
    else:
        temp = 0
        for i in range(1,m+1):
            if n % i == 0 and m % i == 0:
                temp = i
                
    answer.append(temp)
    answer.append(n*m//temp)
    
    return answer