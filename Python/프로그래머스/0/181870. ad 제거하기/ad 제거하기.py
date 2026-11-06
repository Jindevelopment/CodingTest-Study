def solution(strArr):
    answer = []
    for k in strArr:
        if "ad" not in k:
            answer.append(k)
    return answer