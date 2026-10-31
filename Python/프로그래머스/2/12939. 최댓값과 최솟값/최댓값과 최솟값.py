def solution(s):
    answer = ''
    res = []
    temp = s.split()
    for i in temp:
        res.append(int(i))
        
    mi = min(res)
    ma = max(res)
    answer = str(mi) + " " + str(ma)
    return answer

