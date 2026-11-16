for k in range(1, 11):
    ts = int(input())
    find_str = input().strip()
    destination = input().strip()
    count = 0
    for i in range(len(destination)-len(find_str)+1):
        if destination[i:i+len(find_str)]==find_str:
            count+=1
    print(f"#{ts} {count}")
    