T = int(input())

for ts in range(1,T+1):
    num = int(input())
    li = []
    while len(li) < num:
        li.extend(input().split())

    st = ''.join(li)
    
    answer = 0

    while str(answer) in st:
        answer += 1

    


    print(f"#{ts} {answer}")

