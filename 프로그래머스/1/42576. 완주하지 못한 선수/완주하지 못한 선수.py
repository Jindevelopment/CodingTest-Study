def solution(participant, completion):
    answer = ''
    
    my_dict = {}
    
    for i in participant:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    
    for j in completion:
        if my_dict[j] >= 1:
            my_dict[j] -= 1
    
    for k,v in my_dict.items():
        if v >= 1:
            answer += k * v
    
    return answer