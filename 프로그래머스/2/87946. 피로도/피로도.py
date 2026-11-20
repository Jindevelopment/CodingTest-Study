from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    # 순열 만들기
    li = list(permutations(dungeons,len(dungeons)))
    res = []
    
    for i in range(len(li)):
        count = 0
        temp = k
        for j in range(len(li[i])):
            if temp >= li[i][j][0]:
                temp -= li[i][j][1]
                count+=1
        res.append(count)
        
    return max(res)