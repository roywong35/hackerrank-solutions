def substrCount(n, s):
    group = []
    i = 0
    while i < n:
        length = 1
        while i + length < n and s[i] == s[i+length]:
            length += 1
        group.append((s[i], length))
        i += length
        
    count = sum(val * (val + 1) // 2 for _, val in group)
    
    for j in range(1, len(group) - 1):
        if group[j][1] == 1 and group[j-1][0]== group[j+1][0]:
            count += min(group[j-1][1], group[j+1][1])
    return count