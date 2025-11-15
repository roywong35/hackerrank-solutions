from collections import Counter

class Solution:
    def isValid(self, s):
        freq = Counter(s)
        freq_count = Counter(freq.values())

        # Case 1: all characters have the same frequency
        if len(freq_count) == 1:
            return "YES"

        # Case 2: two different frequencies
        elif len(freq_count) == 2:
            f1, f2 = freq_count.keys()
            # identify which is higher / lower
            high = max(f1, f2)
            low = min(f1, f2)

            # Case 2a: one char occurs once (freq=1) — remove it → valid
            if freq_count[1] == 1 and low == 1:
                return "YES"

            # Case 2b: one char has higher frequency by exactly 1, and only one such char
            elif freq_count[high] == 1 and high - low == 1:
                return "YES"

        # Otherwise invalid
        return "NO"

solution = Solution()
answer = solution.isValid("aabbccc")
print(answer)