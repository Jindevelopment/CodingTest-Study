def solution(phone_book):
    answer = True
    li = []
    for j in phone_book:
        li.append(j)
    li.sort()
    for i in range(len(phone_book)-1):
        if li[i+1].startswith(li[i]):
            return False
        
    
    
    
    
            
    
    return answer