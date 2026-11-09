def solution(num_list):
    answer = 0
    for i in num_list:
        temp = i
        while temp!=1:
            if temp%2==0:
                temp//=2
            else:
                temp = (temp-1)//2
            answer+=1
        
    return answer
    