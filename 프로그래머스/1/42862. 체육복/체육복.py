def solution(n, lost, reserve):
    temp = []
    for i in range(n):
        temp.append(1)    
    for k in lost:
        temp[k-1] -= 1   #체육복이 없는 학생: 0
    for j in reserve:
        temp[j-1] += 1   #체육복 여분이 있는 학생: 2
    
    for x in sorted(lost):
        if x==1:
            if temp[x] == 2:
                temp[x] = 1
                temp[x-1] = 1
        elif x == n:
            if temp[x-2] == 2:
                temp[x-2] = 1
                temp[x-1] = 1
        else:
            if temp[x-2] == 2:
                temp[x-2] = 1
                temp[x-1] = 1
                continue
            if temp[x] == 2:
                temp[x] = 1
                temp[x-1] = 1
                continue
    
           
    
    # 1 2 3 4 5
    # 2 0 2 0 2
    
    return temp.count(1) + temp.count(2)