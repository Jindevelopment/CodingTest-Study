T = int(input())
for ts in range(1,T+1):
    li = input()
    answer = ""
    for k in range(len(li)-1,-1,-1):
        if li[k] == "b":
            answer += "d"
        elif li[k] =="d":
            answer+="b"
        elif li[k] == "p":
            answer += "q"
        elif li[k] == "q":
            answer+="p"
    print(f"#{ts} {answer}")