def isBalanced(s):
    stack = []
    pairs = {"{":"}", "[":"]", "(":")"}

    for ch in s:
        if ch in pairs:
            stack.append(pairs[ch])
        elif stack and ch == stack[-1]:
            stack.pop()
        else:
            return "NO"
    
    return "YES" if not stack else "NO"

print(isBalanced("{{[[(())]]}}"))