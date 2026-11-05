def solution(t, p):
    answer = []
    for i in range(len(t)-len(p)+1):
        answer.append(t[i:i+len(p)])
    count = 0
    for k in answer:
        if int(k) <= int(p):
            count+=1
            
    return count