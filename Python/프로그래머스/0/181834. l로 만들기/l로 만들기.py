def solution(myString):
    answer = ''
    for k in range(len(myString)):
        if myString[k] < "l":
            answer+="l"
        else:
            answer += myString[k]
    return answer