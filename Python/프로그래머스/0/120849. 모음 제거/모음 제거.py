def solution(my_string):
    answer = ''
    
    rev = ['a','e','i','o','u']
    
    for i in my_string:
        count = 0
        for k in rev:
            if i == k:
                count+=1
        if count != 1:
            answer += i
            
        
    return answer