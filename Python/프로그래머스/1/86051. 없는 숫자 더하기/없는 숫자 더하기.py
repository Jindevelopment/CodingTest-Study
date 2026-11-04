def solution(numbers):
    temp = [0,1,2,3,4,5,6,7,8,9]
    result = []
    for i in temp:
        if i not in numbers:
            result.append(i)
            
    return sum(result)