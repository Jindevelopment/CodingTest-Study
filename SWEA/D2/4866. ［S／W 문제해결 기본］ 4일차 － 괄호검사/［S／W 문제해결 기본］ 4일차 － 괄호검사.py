T = int(input())

for ts in range(1,T+1):
    st = input().strip()
    stack = []
    result = 1
    for i in st:
        if i=="{" or i == "(":
            stack.append(i)
        if i == "}":
            if stack and stack[-1] == "{":
                stack.pop()
            else:
                result = 0
                break
        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                result = 0
                break
    if len(stack)==0 and result == 1:
        print(f"#{ts} 1")
    else:
        print(f"#{ts} 0")
            