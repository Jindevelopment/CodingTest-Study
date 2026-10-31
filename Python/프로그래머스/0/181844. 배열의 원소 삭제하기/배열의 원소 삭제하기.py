def solution(arr, delete_list):
    answer = arr.copy()
    
    for i in arr:
        for k in delete_list:
            if i==k:
                answer.remove(i)
    
    return answer