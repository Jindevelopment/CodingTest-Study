def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for k in numbers[i+1:]:
            answer.append(numbers[i]+k)
    
    result = sorted(list(set(answer)))
    return result