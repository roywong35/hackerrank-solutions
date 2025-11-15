class Solution:
    def maxMin(self, k, arr):
        arr.sort()
        min_diff = float("inf")
        for i in range(len(arr) - k + 1):
            diff = arr[i + k -1] - arr[i]
            min_diff = min(min_diff, diff)
        return min_diff
solution = Solution()
answer = solution.maxMin(3, [10,100,300,200,1000,20,30])
print(answer)
