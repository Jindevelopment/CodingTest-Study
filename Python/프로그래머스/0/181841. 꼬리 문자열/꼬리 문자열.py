def solution(str_list, ex):
    answer = ''
    
    for temp in str_list:
        if temp.find(ex) >= 0:
            continue
        else:
            answer += temp
    
    return answer