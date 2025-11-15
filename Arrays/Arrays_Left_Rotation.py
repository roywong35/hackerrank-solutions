class Solution:
    def rotLeft(self, a, d):
        d %= len(a)
        return a[d:] + a[:d]
solution = Solution()
answer = solution.rotLeft([1,2,3,4,5], 4)
print(answer)