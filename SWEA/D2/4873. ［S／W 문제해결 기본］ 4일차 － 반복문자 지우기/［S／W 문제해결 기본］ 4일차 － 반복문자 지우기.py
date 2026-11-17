T = int(input())

for ts in range(1, T+1):
    word = input().strip()
    stack = []

    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print(f"#{ts} {len(stack)}")