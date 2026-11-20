T = int(input())

for ts in range(1,T+1):
    li = input()
    current = "0"
    count = 0
    for i in li:
        if i!=current:
            current = i
            count+=1

    print(f"#{ts} {count}")