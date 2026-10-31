def solution(myString):
    answer = myString.split("x")
    res = []
    for i in answer:
        res.append(len(i))
    
    
    return res