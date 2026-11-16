T = int(input())
#50,000원, 10,000원, 5,000원, 1,000원, 500원, 100원, 50원, 10원
for ts in range(1,T+1):
    print(f"#{ts}")
    temp = [0,0,0,0,0,0,0,0]
    money = int(input())
    temp[0] += money//50000
    money%=50000
    temp[1] += money//10000
    money%=10000
    temp[2] += money//5000
    money%=5000
    temp[3] += money//1000
    money%=1000
    temp[4]+=money//500
    money%=500
    temp[5] += money//100
    money%=100
    temp[6] += money//50
    money%=50
    temp[7]+=money//10
    money%=10
    for k in temp:
        print(k,end=" ")
    print("")