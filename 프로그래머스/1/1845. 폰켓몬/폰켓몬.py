def solution(nums):
    answer = 0
    my_dict = {}
    for i in nums:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    
    total = len(nums)/2
    for k in my_dict.keys():
        if total == answer:
            break
        if my_dict[k] >= 1:
            answer += 1
    
    return answer