def solution(s):
    answer = True
    temp = []
    for i in s:
        if i == "(":
            temp.append(i)
        elif i == ")" and len(temp)!=0 and temp[-1]=="(":
            temp.pop()
        else:
            answer = False
            break
    
    if len(temp)!=0:
        answer = False
    return answer