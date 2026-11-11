T = int(input())

score = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]

for ts in range(1,T+1):
    num, idx = map(int,input().split())
    li = []
    for i in range(num):
        mid, final,assign = map(int,input().split())
        li.append(mid*0.35+final*0.45+assign*0.2)
    
    target = li[idx-1]
    li = sorted(li,reverse=True)
    grade = []
    wh = 0
    # 20 19 18 17 16 15 14 ~~
    for x in range(num):
        if li[x] == target:
            wh=x
        grade.append(score[x//(num//10)])

    
        
    print(f"#{ts} {grade[wh]}")
    