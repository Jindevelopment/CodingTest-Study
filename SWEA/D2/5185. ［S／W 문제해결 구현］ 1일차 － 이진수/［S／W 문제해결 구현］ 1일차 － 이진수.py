T = int(input())
te = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
for ts in range(1,T+1):
    a,li = input().split()
    a = int(a)
    res = []
    print(f"#{ts} ",end="")
    for i in range(a):
        for j in li[i]:
            temp = te[j]
            if temp//8>=1:
                res.append(1)
                temp%=8
            else:
                res.append(0)
            if temp//4>=1:
                res.append(1)
                temp%=4
            else:
                res.append(0)
            if temp//2>=1:
                res.append(1)
                temp%=2
            else:
                res.append(0)
            if temp//1>=1:
                res.append(1)
                temp%=1
            else:
                res.append(0)
    for z in res:
        print(z,end="")
    print()
                