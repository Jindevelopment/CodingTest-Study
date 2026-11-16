a = int(input())
res=[]
for i in range(1,a+1):
    if a%i==0:
        res.append(i)
res.sort()
for k in res:
    print(k,end =" ")