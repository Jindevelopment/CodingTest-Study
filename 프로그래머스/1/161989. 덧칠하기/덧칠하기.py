def solution(n, m, section):
    answer = 0
    li = []
    #벽에 페인트 초기화
    for i in range(n):
        li.append(1)
    
    #색칠 안 된 벽
    for k in section:
        li[k-1] = 0
    
    start = 0
    while start < n:
        if li[start] == 0:
            answer += 1
            for j in range(start,min(start+m,n)):
                li[j]=1
        start += 1
                
    
    
    return answer