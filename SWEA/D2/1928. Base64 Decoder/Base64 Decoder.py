T = int(input())

encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
#3개의 문자를 인코딩 할 경우 4개의 문자로 됨.
for ts in range(1,T+1):
    li = input().strip()
    temp =""
    for i in li:
        temp += format(encoding.index(i),"06b")
        
    res = []
    for k in range(0,len(temp),8):
        res.append(chr(int(temp[k:k+8],2)))
        
    print(f"#{ts} {''.join(res)}")