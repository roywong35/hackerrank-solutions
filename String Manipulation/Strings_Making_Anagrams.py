from collections import Counter

class Solution:
    def makeAnagram(self, a, b):
        count_a = Counter(a)
        count_b = Counter(b)
        count_diff = (count_a-count_b) + (count_b-count_a)
        return sum(count_diff.values())

solution = Solution()
answer = solution.makeAnagram("cde", "abc")
print(answer)