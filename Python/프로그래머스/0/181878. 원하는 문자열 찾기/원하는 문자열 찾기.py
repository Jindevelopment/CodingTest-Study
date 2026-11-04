def solution(myString, pat):
    if myString.lower().find(pat.lower())>=0:
        return 1
    else: 
        return 0