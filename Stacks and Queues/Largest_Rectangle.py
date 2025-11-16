def largestRectangle(h):
    stack = []
    n = len(h)
    max_area = 0

    for i in range(n):
        while stack and h[stack[-1]] > h[i]:
            height = h[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            max_area = max(max_area, height * width)

        stack.append(i)
    
    while stack:
        height = h[stack.pop()]
        left = stack[-1] if stack else -1
        width = n - left - 1
        max_area = max(max_area, height * width)
    
    return max_area
print(largestRectangle([1, 2, 3, 4, 5]))