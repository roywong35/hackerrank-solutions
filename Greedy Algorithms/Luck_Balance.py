class Solution:
    def luckBalance(self, k, contests):
        max_luck = 0
        importance = []
        for luck, imp in contests:
            if imp == 0:
                max_luck += luck
            else:
                importance.append(luck)

        importance.sort(reverse=True)

        for j in range(len(importance)):
            if j < k:
                max_luck += importance[j]
            else:
                max_luck -= importance[j]
        return max_luck
solution = Solution()
answer = solution.luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]])
print(answer)