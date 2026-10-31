def solution(num_list):
    answer = 0
    
    temp1 = ''
    temp2 = ''
    for i in num_list:
        if i%2 == 0:
            temp1 += str(i)
        else:
            temp2 += str(i)
            
    answer = int(temp1) + int(temp2)
    
    return answer