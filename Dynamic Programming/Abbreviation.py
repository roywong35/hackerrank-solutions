def abbreviation(a, b):
    n, m = len(a), len(b)

    # dp[i][j] = can a[:i] be converted to match b[:j]
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    # Initialize first column: matching empty b
    # a[:i] can match empty string ONLY if all are lowercase (can delete them)
    for i in range(1, n + 1):
        if a[i-1].islower():
            dp[i][0] = dp[i-1][0]  # delete lowercase
        else:
            dp[i][0] = False       # cannot delete uppercase

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            charA = a[i-1]
            charB = b[j-1]

            # Option 1: match charA to charB
            if charA.upper() == charB:
                # match (capitalize if needed)
                dp[i][j] = dp[i-1][j-1]

            # Option 2: delete charA if it's lowercase
            if charA.islower():
                dp[i][j] = dp[i][j] or dp[i-1][j]       #(match possible?) OR (delete possible?)

            # IMPORTANT:
            # uppercase mismatch → dp stays False automatically

    return "YES" if dp[n][m] else "NO"

print(abbreviation("daBcd", "ABC"))

def abbreviation(a, b):
    n, m = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0]= True

    for i in range(1, n + 1):
        if a[i-1].lower():
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = False

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            charA = a[i-1]
            charB = b[j-1]

            if charA.upper() == charB:
                dp[i][j] = dp[i-1][j-1]

            if charA.islower():
                dp[i][j] = dp[i][j] or dp[i-1][j]
    
    return "YES" if dp[n][m] else "NO"

print(abbreviation("daBcd", "ABC"))