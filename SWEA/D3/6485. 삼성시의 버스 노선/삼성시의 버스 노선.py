T = int(input())

for ts in range(1,T+1):
    num = int(input()) #버스 노선 개수
    li = [] #각 버스 노선
    for i in range(num):
        num1, num2 = map(int,input().split())
        li.append([num1,num2])
    
    many = int(input()) # 출력하고자 하는 정류장 개수 
    where = [] # 각 버스 정류장
    
    for k in range(many):
        temp = int(input())
        where.append(temp)
    
    
    bus = []
    for z in range(5001):
        bus.append(0)
    
    for x in range(len(li)):
        for y in range(li[x][0],li[x][1]+1):
            bus[y]+=1
    
    print(f"#{ts} ",end="")
    for u in where:
        print(bus[u],end= " ")
    print()