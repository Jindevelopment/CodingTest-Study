def solution(array, height):
    answer = 0
    
    array.sort()
    for i in array:
        if height<i:
            answer+=1
    
    return answer