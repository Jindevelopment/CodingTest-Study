def solution(N, stages):
    answer = []
    remaining = len(stages)
    for i in range(1,N+1):
        temp = stages.count(i)
        if i <= N:
            if remaining==0:
                answer.append((i,0))
            else:
                answer.append((i,temp/remaining))
                remaining-=temp
    
    answer.sort(key=lambda x:x[1],reverse=True)
    res = []
    for k in answer:
        res.append(k[0])
        
    return res