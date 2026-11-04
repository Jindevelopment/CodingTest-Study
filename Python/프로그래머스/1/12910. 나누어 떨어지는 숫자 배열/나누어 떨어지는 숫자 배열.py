def solution(arr, divisor):
    temp = []
    count = 0
    for i in arr:
        if i % divisor == 0:
            count += 1
            temp.append(i)
            
    answer = sorted(temp)        
    if count == 0:
        return [-1]
    else:
        return answer