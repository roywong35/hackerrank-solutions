class Solution:
    def getMinimumCost(self, k, c):
        c.sort(reverse=True)
        cost = 0

        for i in range(len(c)):
            multiplier = (i // k) + 1
            cost += c[i] * multiplier

        return cost
solution = Solution()
answer = solution.getMinimumCost(2, [2,5,6,7,8])
print(answer)
