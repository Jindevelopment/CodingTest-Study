T = int(input())

for ts in range(1,T+1):
    word = input()
    stack = []

    for i in word:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    print(f"#{ts} {len(stack)}")