from itertools import permutations

def solution(numbers):
    answer = 0
    li = []
    
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            li.append(int(''.join(p)))
            
    li = list(set(li))
    for k in li:
        count = 0
        for j in range(2,k+1):
            if k%j==0:
                count+=1
        if count == 1:
            answer+=1
    
    return answer