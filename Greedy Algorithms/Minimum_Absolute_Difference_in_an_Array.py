class Solution:
    def minimumAbsoluteDifference(self, arr):
        min_diff, diff = float("inf"), 0
        arr.sort()
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            min_diff = min(min_diff, diff)
        return min_diff

solution = Solution()
answer = solution.minimumAbsoluteDifference([1,-3,71,68,17])
print(answer)
