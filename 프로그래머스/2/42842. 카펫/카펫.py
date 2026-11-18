def solution(brown, yellow):
    total = brown + yellow
    
    temp = []
    for i in range(1,total+1):
        if total % i == 0:
            res = total / i
            if res >= i:
                tu = (res,i)
                temp.append(tu)
            else:
                tu = (i,res)
                temp.append(tu)
    
    for x,y in temp:
        if (x-2) * (y-2) == yellow:
            return [x,y]