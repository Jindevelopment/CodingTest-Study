def solution(s, skip, index):
    answer = ''
    
    for i in s:
        count = 0
        temp = i
        while count != index:    
            temp = chr(ord(temp) + 1)
            if ord(temp) == ord("z") + 1:
                temp = 'a'
            if chr(ord(temp)) not in skip:
                count +=1
        
        answer += temp
            
    return answer



# a b c d e f g h i j k l m n o p q r s t u v w x y z


