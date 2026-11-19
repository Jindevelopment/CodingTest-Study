def solution(today, terms, privacies):
    answer = []
    
    year = int(today[0:4])
    month = int(today[5:7])
    day = int(today[8:])
    
    for i in range(len(privacies)):
        y = int(privacies[i][0:4])
        m = int(privacies[i][5:7])
        d = int(privacies[i][8:10])
        option = privacies[i][-1]
        
        terms_month = 0
        for k in terms:
            if k[0] == option:
                t,p = k.split()
                terms_month = int(p)
        
        m += int(terms_month)
        
        if m>=13:
            y+=(m//12)
            m%=12
        d -= 1
        if d == 0:
            m-=1
            d=28
        if m == 0:
            y-=1
            m=12
        
        if year>y:
            answer.append(i+1)
        elif year==y:
            if month>m:
                answer.append(i+1)
            elif month == m:
                if day>d:
                    answer.append(i+1)
            
    return answer