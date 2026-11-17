T = int(input())

for ts in range(1,T+1):
    num = int(input())
    li = [0] * (num+1)
    cnt=1
    def tree(k):
        global cnt
        if k<=num:
            tree(2*k)
            li[k]=cnt
            cnt+=1
            tree(2*k+1)
            
    tree(1)
    
    print(f"#{ts} {li[1]} {li[num//2]}")