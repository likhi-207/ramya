
expression = "[{([2+3]{6-1}{5+4})}]"

stack = []
# for i in expression:
# for i in range(0, len(expression)):

for i in expression:
    print("current i : ", i)
    if i == "(" or i=="{" or i=="[":
        stack.append(i)
    elif i == ")" or i=="{" or i=="[":
        stack.pop()
    else:
        continue

if len(stack) == 0:
    print("Valid exp")
else:
    print("Invalid exp")
