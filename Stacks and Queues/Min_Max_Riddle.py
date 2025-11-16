def riddle(arr):
    n = len(arr)
    left = [-1] * n
    right = [n] * n
    stack = []

    # Step 1: Find Nearest Smaller to Left (NSL)
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    # clear stack for next pass
    stack = []

    # Step 2: Find Nearest Smaller to Right (NSR)
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    # Step 3: result[k] = best minimum for windows of size k
    res = [0] * (n + 1)

    for i in range(n):
        length = right[i] - left[i] - 1
        res[length] = max(res[length], arr[i])

    # Step 4: fill from right → left
    for i in range(n-1, 0, -1):
        res[i] = max(res[i], res[i+1])

    return res[1:]       # ignore index 0 
print(riddle([3, 5, 4, 7, 6]))