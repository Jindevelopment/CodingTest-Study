def solution(x):
    result=0
    y = x
    while(y!=0):
        result += y%10
        y//=10
    
    if x % result== 0:
        return True
    else:
        return False
    
