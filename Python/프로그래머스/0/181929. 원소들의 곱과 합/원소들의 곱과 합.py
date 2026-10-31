def solution(num_list):
    answer = 0
    temp1 = 1
    temp2 = 0
    for i in num_list:
        temp1 *= i
        temp2 += i
    
    if temp1 > (temp2**2):
        return 0
    else:
        return 1
    