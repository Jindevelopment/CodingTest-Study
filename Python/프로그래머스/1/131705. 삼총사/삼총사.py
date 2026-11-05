def solution(number):
    count = 0
    for i in range(len(number)):
        for k in range(i+1,len(number)):
            for j in range(k+1,len(number)):
                if number[i]+number[j]+number[k]==0:
                    count+=1
    
    return count