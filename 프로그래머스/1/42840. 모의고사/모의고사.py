def solution(answers):
    answer = []
    
    people1 = [] 
    people2 = []
    people3 = []
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        people1.append(pattern1[i%5])
        people2.append(pattern2[i%8])
        people3.append(pattern3[i%10])
    
    
    count = [0] * 3
    for k in range(len(answers)):
        if people1[k] == answers[k]:
            count[0] += 1
        if people2[k] == answers[k]:
            count[1] += 1
        if people3[k] == answers[k]:
            count[2] += 1
        
    max_value = max(count)
    res = []
    if count.count(max_value) >= 2:
        for u in range(len(count)):
            if max_value == count[u]:
                res.append(u+1)
        res.sort()
    else:
        res.append(count.index(max_value)+1)
    
    return res